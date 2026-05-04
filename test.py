import register  # noqa: F401
import gymnasium as gym
import numpy as np

from gymnasium.wrappers import RecordEpisodeStatistics

if __name__ == '__main__':
    env = gym.make('HydroneTrajectoryFollower-v0', show_viewer=True,
                   target_trajectory='spiral', render_mode='rgb_array')

    env = RecordEpisodeStatistics(env)

    observation, info = env.reset()
    episode_over = False
    total_reward = 0

    # Start manual recording — frames are collected on each render() call.
    env.unwrapped.start_recording('episode.mp4', fps=20)

    while not episode_over:
        action = 150 * np.ones(4)
        observation, reward, terminated, truncated, info = env.step(action)

        # Pull the latest CameraView frame (also appends to the recording buffer).
        frame = env.unwrapped.render()

        total_reward += reward
        episode_over = terminated or truncated

    env.unwrapped.stop_recording()

    print(f"Episode finished! Total reward: {total_reward}")
    print(info)
    env.close()
