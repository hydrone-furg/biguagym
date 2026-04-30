import biguasim

import numpy as np

from typing import List
from numpy.typing import NDArray
from operator import itemgetter
from gymnasium import spaces
from pathlib import Path

from .base_env import BiguaGymEnv
from .space import DATA_REGISTRY

CONFIG = f'{Path(__file__).resolve().parent.parent}/config'


class StateEnv(BiguaGymEnv):
    """State-observation BiguaGym env.

    Selects the underlying gym task via ``env_params["env_id"]``.
    ``num_envs`` is accepted for pipeline compatibility but ignored (BiguaGym
    is single-instance).

    Register as ``BiguaGymState-v0``; use via YAML ``name: BiguaGymState-v0``.
    """

    def __init__(
        self,
        seed: int,
        agent_type: str,
        control_abstraction: str,
        location: list,
        rotation: list,
        batch_size: int = 1,
        observation_type: str | List[str] = "DynamicsSensor",
        show_viewer: bool = False,
        timestep: bool = False,
        action_stack: int = 1,
        target_factor: int = 1,
    ) -> None:
        output_mode = "timestep" if timestep else "gym"

        self._agent_type = agent_type
        self._location = location
        self._rotation = rotation
        self._batch_size = batch_size
        self._control_abstraction = control_abstraction
        self._observation_type = observation_type
        self._action_repeat = action_stack
        self._target_factor = target_factor
        self._timestep = timestep

        env_params, obs_params = self._build_params()

        keys = tuple(obs_params.keys())
        # itemgetter with a single arg returns a scalar, not a tuple — wrap so
        # downstream code can always treat the result as an iterable of values.
        _raw_getter = itemgetter(*keys)
        if len(keys) == 1:
            self._getter = lambda d: (_raw_getter(d),)
        else:
            self._getter = _raw_getter

        self._dynamics = None
        self._last_norm = None
        self._episode_steps = 0
        self._on_target = False
        self._on_target_buf = 0  # cross-episode success counter (drives target_factor curriculum)
        self._target = None

        # action_stack_shape requires the underlying env's action dim, which is
        # only known after _build_env(). Initialize without it, then inject.
        super().__init__(seed, env_params, obs_params, output_mode, show_viewer, None)


        if timestep:
            from .base_env import ActionStack
            self._action_stack = ActionStack(
                (action_stack, int(self._env.action_space.shape[0]))
            )

    def _build_params(self):
        env_params: dict = self._load_config(f"{CONFIG}/state.json")

        _id = self._agent_id(env_params, 'robot0')

        env_params['agents'][_id]['agent_type'] = self._agent_type
        env_params['agents'][_id]['control_abstraction'] = self._control_abstraction
        env_params['agents'][_id]['location'] = self._location
        env_params['agents'][_id]['rotation'] = self._rotation
        env_params['agents'][_id]['dynamics']['batch_size'] = self._batch_size

        loc = np.asarray(self._location, dtype=np.float32)
        self._bounds = np.array([loc - 10.0, loc + 10.0])
        # Keep z-min above ground.
        self._bounds[0, 2] = max(float(self._bounds[0, 2]), 0.1)

        if isinstance(self._observation_type, str):
            self._observation_type = [self._observation_type]

        obs_params = {
            obs_type: np.zeros(DATA_REGISTRY[obs_type]).ravel().shape
            for obs_type in self._observation_type
        }

        return env_params.copy(), obs_params.copy()

    @property
    def max_episode_steps(self) -> int:
        return 1000  # BiguaGym default

    def _build_env(self):
        return biguasim.make(scenario_cfg=self.env_cfg, show_viewport=self.show_viewer)

    def _wrap_state(self, state: dict) -> NDArray:
        return np.concatenate([
            np.asarray(v, dtype=np.float32).ravel()
            for v in self._getter(state)
        ])

    def _reset(self):
        state = self._env.reset()
        self._dynamics = state['RPYDynamicsSensor']
        self._episode_steps = 0
        self._last_norm = None
        self._on_target = False

        if self._on_target_buf % self._target_factor == 0:
            self._target = self.rng.uniform(low=self._bounds[0], high=self._bounds[1])

        return self._wrap_state(state), {}

    def _init_spaces(self) -> None:
        total_dim = sum(int(np.prod(shape)) for shape in self.obs_cfg.values())
        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(total_dim,),
            dtype=np.float32,
        )
        self.action_space = spaces.Box(
            low=float(self._env.action_space.get_low()[0]),
            high=float(self._env.action_space.get_high()[0]),
            shape=(int(self._env.action_space.shape[0]),),
            dtype=np.float32,
        )

    def _reward(self):
        target = self._target
        pos = np.asarray(self._dynamics[6:9])
        ang_vel = np.asarray(self._dynamics[12:15])
        rpy = np.asarray(self._dynamics[15:])

        norm = np.linalg.norm(target - pos)

        self._on_target = abs(norm) <= 0.15
        if self._on_target:
            self._on_target_buf += 1

        norm_reward = np.exp(-2.0 * norm)

        if self._last_norm is None:
            self._last_norm = norm

        smooth_reward = 3 * (self._last_norm - norm)
        self._last_norm = norm

        rpy_magnitude = np.linalg.norm(rpy[:2])
        rpy_ratio = np.clip(rpy_magnitude / np.radians(35), 0.0, 1.0)
        stable_reward = -(rpy_ratio ** 2) * 3.0

        yaw_rate = abs(ang_vel[2])
        spin_reward = -yaw_rate * 0.2

        return norm_reward + smooth_reward + stable_reward + spin_reward

    def _step(self, action: NDArray) -> tuple:
        self._episode_steps += self._action_repeat

        flat = np.asarray(action, dtype=np.float32).ravel()
        if self._batch_size > 1:
            action_arg = np.tile(flat, (self._batch_size, 1)).tolist()
        else:
            action_arg = flat.tolist()

        state = self._env.step(action_arg, action_repeat=self._action_repeat)
        self._dynamics = state['RPYDynamicsSensor']
        obs = self._wrap_state(state)

        pos = np.asarray(self._dynamics[6:9])
        r, p, _ = np.asarray(self._dynamics[15:])

        truncated = self._episode_steps >= self.max_episode_steps

        out_of_bounds = bool(
            np.any((pos < self._bounds[0]) | (pos > self._bounds[1]))
        )
        terminated = bool(
            (abs(r) > np.radians(15))
            or (abs(p) > np.radians(15))
            or out_of_bounds
            or self._on_target
        )

        reward = 3.0 * abs(self._reward()) if self._on_target else self._reward()
        info = {"reached_goals": int(self._on_target_buf)}
        return obs, float(reward), terminated, truncated, info

    def update_target_factor(self, factor: int) -> None:
        self._target_factor = abs(int(factor))
