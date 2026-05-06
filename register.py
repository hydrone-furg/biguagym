import gymnasium as gym

# Convention
# ----------
# -v0  State-based observation (default: DynamicsSensor).
# -v1  Pixel-based observation (default: pixel_channels=['rgb']).
#
# Observation composition is defined by the user at gym.make() time via the
# observation_type (v0) or pixel_channels / frame_stack / frame_size (v1) kwargs.

# ---------------------------------------------------------------------------
# BlueBoat  (surface)
# ---------------------------------------------------------------------------

gym.register(
    id="BlueBoatNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueBoat', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 0], 'rotation': [0, 0, 0]},
)
gym.register(
    id="BlueBoatNav-v1",
    entry_point="core.environments:NavPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueBoat', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 0], 'rotation': [0, 0, 0]},
)

gym.register(
    id="BlueBoatTrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueBoat', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 0], 'rotation': [0, 0, 0]},
)
gym.register(
    id="BlueBoatTrajectoryFollower-v1",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueBoat', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 0], 'rotation': [0, 0, 0]},
)

# ---------------------------------------------------------------------------
# BlueROV2  (underwater)
# ---------------------------------------------------------------------------

gym.register(
    id="BlueROV2Dock-v0",
    entry_point="core.environments:DockEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROV2', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)
gym.register(
    id="BlueROV2Dock-v1",
    entry_point="core.environments:DockPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROV2', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)

gym.register(
    id="BlueROV2Nav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROV2', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)
gym.register(
    id="BlueROV2Nav-v1",
    entry_point="core.environments:NavPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROV2', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)

gym.register(
    id="BlueROV2TrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROV2', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)
gym.register(
    id="BlueROV2TrajectoryFollower-v1",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROV2', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)

# ---------------------------------------------------------------------------
# BlueROVHeavy  (underwater)
# ---------------------------------------------------------------------------

gym.register(
    id="BlueROVHeavyDock-v0",
    entry_point="core.environments:DockEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROVHeavy', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)
gym.register(
    id="BlueROVHeavyDock-v1",
    entry_point="core.environments:DockPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROVHeavy', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)

gym.register(
    id="BlueROVHeavyNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROVHeavy', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)
gym.register(
    id="BlueROVHeavyNav-v1",
    entry_point="core.environments:NavPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROVHeavy', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)

gym.register(
    id="BlueROVHeavyTrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROVHeavy', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)
gym.register(
    id="BlueROVHeavyTrajectoryFollower-v1",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'BlueROVHeavy', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)

# ---------------------------------------------------------------------------
# DjiMatrice  (aerial)
# ---------------------------------------------------------------------------

gym.register(
    id="DjiMatriceHover-v0",
    entry_point="core.environments:HoverEnv",
    kwargs={'seed': 42, 'agent_type': 'DjiMatrice', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)
gym.register(
    id="DjiMatriceHover-v1",
    entry_point="core.environments:HoverPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'DjiMatrice', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)

gym.register(
    id="DjiMatriceLand-v0",
    entry_point="core.environments:LandEnv",
    kwargs={'seed': 42, 'agent_type': 'DjiMatrice', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)
gym.register(
    id="DjiMatriceLand-v1",
    entry_point="core.environments:LandPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'DjiMatrice', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)

gym.register(
    id="DjiMatriceNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={'seed': 42, 'agent_type': 'DjiMatrice', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)
gym.register(
    id="DjiMatriceNav-v1",
    entry_point="core.environments:NavPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'DjiMatrice', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)

gym.register(
    id="DjiMatriceTrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={'seed': 42, 'agent_type': 'DjiMatrice', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)
gym.register(
    id="DjiMatriceTrajectoryFollower-v1",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'DjiMatrice', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)

# ---------------------------------------------------------------------------
# Hydrone  (multi-domain)
# ---------------------------------------------------------------------------

gym.register(
    id="HydroneHover-v0",
    entry_point="core.environments:HoverEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)
gym.register(
    id="HydroneHover-v1",
    entry_point="core.environments:HoverPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)

gym.register(
    id="HydroneLand-v0",
    entry_point="core.environments:LandEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)
gym.register(
    id="HydroneLand-v1",
    entry_point="core.environments:LandPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)

gym.register(
    id="HydroneDock-v0",
    entry_point="core.environments:DockEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)
gym.register(
    id="HydroneDock-v1",
    entry_point="core.environments:DockPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 5], 'rotation': [0, 0, 0]},
)

gym.register(
    id="HydroneNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 0], 'rotation': [0, 0, 0]},
)
gym.register(
    id="HydroneNav-v1",
    entry_point="core.environments:NavPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 0], 'rotation': [0, 0, 0]},
)

gym.register(
    id="HydroneTrajectoryFollower-v0",
    entry_point="core.environments:TrajectoryEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 0], 'rotation': [0, 0, 0]},
)
gym.register(
    id="HydroneTrajectoryFollower-v1",
    entry_point="core.environments:TrajectoryPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'Hydrone', 'control_abstraction': 'cmd_motor_speeds',
            'location': [100, 100, 0], 'rotation': [0, 0, 0]},
)

# ---------------------------------------------------------------------------
# TorpedoAUV  (underwater)
# ---------------------------------------------------------------------------

gym.register(
    id="TorpedoDock-v0",
    entry_point="core.environments:DockEnv",
    kwargs={'seed': 42, 'agent_type': 'TorpedoAUV', 'control_abstraction': 'cmd_rudders_sterns_motor_speed',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)
gym.register(
    id="TorpedoDock-v1",
    entry_point="core.environments:DockPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'TorpedoAUV', 'control_abstraction': 'cmd_rudders_sterns_motor_speed',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)

gym.register(
    id="TorpedoNav-v0",
    entry_point="core.environments:NavEnv",
    kwargs={'seed': 42, 'agent_type': 'TorpedoAUV', 'control_abstraction': 'cmd_rudders_sterns_motor_speed',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)
gym.register(
    id="TorpedoNav-v1",
    entry_point="core.environments:NavPixelEnv",
    kwargs={'seed': 42, 'agent_type': 'TorpedoAUV', 'control_abstraction': 'cmd_rudders_sterns_motor_speed',
            'location': [100, 100, -0.2], 'rotation': [0, 0, 0]},
)
