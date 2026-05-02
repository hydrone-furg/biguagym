import register  # noqa: F401  # registers DjiMatriceHover-v0
import gymnasium as gym
import numpy as np

from gymnasium.wrappers import RecordEpisodeStatistics

if __name__ == '__main__':
    env = gym.make('HydroneHover-v0', show_viewer=True)

    env = RecordEpisodeStatistics(env)

    observation, info = env.reset()
    episode_over = False
    total_reward = 0

    while not episode_over:
        # Choose an action: 0 = push cart left, 1 = push cart right
        action =  np.zeros(4) # Random action for now - real agents will be smarter!

        # Take the action and see what happens
        observation, reward, terminated, truncated, info = env.step(action)

        # reward: +1 for each step the pole stays upright
        # terminated: True if pole falls too far (agent failed)
        # truncated: True if we hit the time limit (500 steps)

        total_reward += reward
        episode_over = terminated or truncated

    print(f"Episode finished! Total reward: {total_reward}")
    print(info)
    env.close()
