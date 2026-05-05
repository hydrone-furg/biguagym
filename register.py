import gymnasium as gym


gym.register(
    id="BlueBoatNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueBoat',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,0],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueBoatTrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueBoat',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,0],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROV2Dock-v0",
    entry_point="core.environments:DockEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROV2',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROV2Nav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROV2',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROV2TrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROV2',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROVHeavyDock-v0",
    entry_point="core.environments:DockEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROVHeavy',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROVHeavyNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROVHeavy',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROVHeavyTrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROVHeavy',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="DjiMatriceHover-v0",
    entry_point="core.environments:HoverEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'DjiMatrice',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="DjiMatriceLand-v0",
    entry_point="core.environments:LandEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'DjiMatrice',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="DjiMatriceNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'DjiMatrice',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="DjiMatriceTrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'DjiMatrice',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneHover-v0",
    entry_point="core.environments:HoverEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneLand-v0",
    entry_point="core.environments:LandEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneDock-v0",
    entry_point="core.environments:DockEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,0],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneTrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={
        'seed' : 0,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,0],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneTrajectoryFollower-v1",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={
        'seed' : 0,
        'agent_type' : 'Hydrone',
        'observation_type' : ['DynamicsSensor', 'NoiseIMUSensor'],
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,0],
        'rotation' : [0,0,0]
        }
)


gym.register(
    id="ToperdoDock-v0",
    entry_point="core.environments:DockEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'TorpedoAUV',
        'control_abstraction' : 'cmd_rudders_sterns_motor_speed',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="ToperdoNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'TorpedoAUV',
        'control_abstraction' : 'cmd_rudders_sterns_motor_speed',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

# ---------------------------------------------------------------------------
# Pixel variants
# ---------------------------------------------------------------------------

gym.register(
    id="BlueBoatNavPixel-v0",
    entry_point="core.environments:NavPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueBoat',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,0],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueBoatTrajectoryFollowerPixel-v0",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueBoat',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,0],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROV2DockPixel-v0",
    entry_point="core.environments:DockPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROV2',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROV2NavPixel-v0",
    entry_point="core.environments:NavPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROV2',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROV2TrajectoryFollowerPixel-v0",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROV2',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROVHeavyDockPixel-v0",
    entry_point="core.environments:DockPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROVHeavy',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROVHeavyNavPixel-v0",
    entry_point="core.environments:NavPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROVHeavy',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="BlueROVHeavyTrajectoryFollowerPixel-v0",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'BlueROVHeavy',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="DjiMatriceHoverPixel-v0",
    entry_point="core.environments:HoverPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'DjiMatrice',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="DjiMatriceLandPixel-v0",
    entry_point="core.environments:LandPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'DjiMatrice',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="DjiMatriceNavPixel-v0",
    entry_point="core.environments:NavPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'DjiMatrice',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="DjiMatriceTrajectoryFollowerPixel-v0",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'DjiMatrice',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneHoverPixel-v0",
    entry_point="core.environments:HoverPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneLandPixel-v0",
    entry_point="core.environments:LandPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneDockPixel-v0",
    entry_point="core.environments:DockPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,5],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneNavPixel-v0",
    entry_point="core.environments:NavPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,0],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="HydroneTrajectoryFollowerPixel-v0",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={
        'seed' : 0,
        'agent_type' : 'Hydrone',
        'control_abstraction' : 'cmd_motor_speeds',
        'location' : [100,100,0],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="ToperdoDockPixel-v0",
    entry_point="core.environments:DockPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'TorpedoAUV',
        'control_abstraction' : 'cmd_rudders_sterns_motor_speed',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)

gym.register(
    id="ToperdoNavPixel-v0",
    entry_point="core.environments:NavPixelEnv",
    kwargs={
        'seed' : 42,
        'agent_type' : 'TorpedoAUV',
        'control_abstraction' : 'cmd_rudders_sterns_motor_speed',
        'location' : [100,100,-0.2],
        'rotation' : [0,0,0]
        }
)