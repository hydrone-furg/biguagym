import gymnasium as gym


gym.register(
    id="DjiMatriceHover-v0",
    entry_point="core.environments:StateEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'DjiMatrice',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [0,0,0],
        'rotation' : [0,0,0]
        }
)