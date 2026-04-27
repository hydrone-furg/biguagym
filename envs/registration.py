import gymnasium as gym


def register_envs():
    gym.register(
        id="Navigation-v0",
        entry_point="biguagym.envs.environments:NavEnv",
    )