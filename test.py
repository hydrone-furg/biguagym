import register  # noqa: F401
import cv2
import gymnasium as gym
import numpy as np

from gymnasium.wrappers import RecordEpisodeStatistics
from core.environments import _PixelObsMixin

_CHANNEL_SENSOR = _PixelObsMixin._CHANNEL_SENSOR


def _active_sensor_names(env) -> set:
    sensors = env.unwrapped.env_cfg['agents'][0]['sensors']
    return {s['sensor_name'] for s in sensors if 'sensor_name' in s}


def _run_episode(env_id: str, pixel_channels: list, render_channel: str | None = None, **make_kwargs):
    print(f"\n{'='*60}")
    print(f"Testing {env_id}  channels={pixel_channels}  render_channel={render_channel}")

    env = gym.make(
        env_id,
        pixel_channels=pixel_channels,
        render_channel=render_channel,
        render_mode='rgb_array',
        **make_kwargs,
    )
    env = RecordEpisodeStatistics(env)

    active = _active_sensor_names(env)
    print(f"  Active sensors in env_cfg: {sorted(active)}")

    # The render channel sensor must be loaded even if not in pixel_channels.
    if render_channel and render_channel in _CHANNEL_SENSOR:
        assert _CHANNEL_SENSOR[render_channel] in active, (
            f"Render channel sensor {_CHANNEL_SENSOR[render_channel]!r} missing from env_cfg"
        )

    record_path = f"episode_{render_channel or 'cameraview'}.mp4"
    env.unwrapped.start_recording(record_path, fps=20)

    obs, _ = env.reset()
    episode_over = False
    total_reward = 0.0
    steps = 0

    while not episode_over and steps < 10:
        action = env.unwrapped.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)

        # Drives the recording — each call appends the current _last_render_frame.
        frame = env.unwrapped.render()
        if frame is not None:
            cv2.imshow(f"render | {render_channel or 'cameraview'}", frame)
            cv2.waitKey(1)

        total_reward += reward
        episode_over = terminated or truncated
        steps += 1

    env.unwrapped.stop_recording()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"  OK — {steps} steps, total_reward={total_reward:.3f}, saved to {record_path}")
    env.close()


if __name__ == '__main__':
    # RGB observation, depth used for rendering/recording.
    # DepthCamera is loaded into the simulator even though it is not in pixel_channels.
    _run_episode('DjiMatriceHover-v1', pixel_channels=['rgb'], render_channel='depth')

    print("\nDone.")
