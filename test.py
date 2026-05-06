import register  # noqa: F401
import gymnasium as gym

from gymnasium.wrappers import RecordEpisodeStatistics


def _active_sensor_types(env) -> set:
    sensors = env.unwrapped.env_cfg['agents'][0]['sensors']
    return {s['sensor_type'] for s in sensors}


def _run_pixel_episode(env_id: str, pixel_channels: list, render_channel: str | None = None, **make_kwargs):
    print(f"\n{'='*60}")
    print(f"[pixel] {env_id}  channels={pixel_channels}  render_channel={render_channel}")

    env = gym.make(
        env_id,
        pixel_channels=pixel_channels,
        render_channel=render_channel,
        render_mode='rgb_array',
        **make_kwargs,
    )
    env = RecordEpisodeStatistics(env)

    obs, _ = env.reset()
    episode_over = False
    total_reward = 0.0
    steps = 0

    while not episode_over and steps < 10:
        action = env.unwrapped.action_space.sample()
        obs, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        episode_over = terminated or truncated
        steps += 1

    print(f"  obs keys : {list(obs.keys())}")
    print(f"  OK — {steps} steps, total_reward={total_reward:.3f}")
    env.close()


def _run_range_episode(env_id: str, **make_kwargs):
    print(f"\n{'='*60}")
    print(f"[range] {env_id}")

    env = gym.make(env_id, **make_kwargs)
    env = RecordEpisodeStatistics(env)

    active_types = _active_sensor_types(env)
    has_range  = 'RangeFinderSensor' in active_types
    has_sonar  = 'ProfilingSonar'    in active_types

    agent_type = env.unwrapped._agent_type
    print(f"  agent_type      : {agent_type}")
    print(f"  RangeFinderSensor loaded : {has_range}")
    print(f"  ProfilingSonar    loaded : {has_sonar}")
    print(f"  observation_space: {env.observation_space}")

    # Validate domain-sensor assignment
    from core.environments import DOMAIN
    if agent_type in DOMAIN['aereo']:
        assert has_range and not has_sonar, "Aerial should use only RangeFinderSensor"
    elif agent_type in DOMAIN['underwater']:
        assert has_sonar and not has_range, "Underwater should use only ProfilingSonar"
    else:
        assert has_range and has_sonar, "Surface/multi-domain should use both sensors"

    obs, _ = env.reset()
    assert obs.shape == env.observation_space.shape, "obs shape mismatch on reset"

    episode_over = False
    total_reward = 0.0
    steps = 0

    while not episode_over and steps < 10:
        action = env.unwrapped.action_space.sample()
        obs, reward, terminated, truncated, _ = env.step(action)
        assert obs.shape == env.observation_space.shape, f"obs shape mismatch at step {steps}"
        total_reward += reward
        episode_over = terminated or truncated
        steps += 1

    print(f"  obs shape: {obs.shape}")
    print(f"  OK — {steps} steps, total_reward={total_reward:.3f}")
    env.close()


if __name__ == '__main__':
    # --- Pixel envs (v1) ---
    # _run_pixel_episode('DjiMatriceHover-v1', pixel_channels=['rgb'])

    # --- Range/sonar envs (v2) ---
    # Aerial: RangeFinderSensor only (+10 dims)
    # _run_range_episode('DjiMatriceNav-v2')
    # _run_range_episode('DjiMatriceTrajectoryFollower-v2')

    # Underwater: ProfilingSonar only (+100 dims)
    # _run_range_episode('BlueROV2Nav-v2', show_viewer=True)
    # _run_range_episode('BlueROV2TrajectoryFollower-v2')

    # Surface: both sensors (+110 dims)
    # _run_range_episode('BlueBoatNav-v2',show_viewer=True)
    # _run_range_episode('BlueBoatTrajectoryFollower-v2')

    # Multi-domain: both sensors (+110 dims)
    _run_range_episode('HydroneNav-v2', show_viewer=True)
    # _run_range_episode('HydroneTrajectoryFollower-v2', show_viewer=True)

    print("\nAll tests passed.")
