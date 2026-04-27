import biguasim

import numpy as np

from gymnasium import Env

from utils import TensorDeque

class BiguaGymEnv(Env):
    def __init__(self, cfg, show_viewport):
        super().__init__()

        self._env = biguasim.make(scenario_cfg=cfg, show_viewport=show_viewport)
        self._rng = np.random.default_rng(seed=42)

        self._agents = []
        self._sensors = []
        self._action_repeat = 1



    def _get_observation(self, actions):
        state = self._env.step(actions, self._action_repeat)

        

    def reset(self, seed = None, options = None):
        if seed:
            self._rng = np.random.default_rng(seed=seed)

        return self._env.reset()
        

        