import gymnasium as gym

from biguasim.sensors import SensorDefinition

from utils import TensorDeque, torch_dtype_range


def dict_deque_tensor_space(sensors : list, deque : TensorDeque):
    return gym.spaces.Dict({ 
            sensor : gym.spaces.Box(
                *torch_dtype_range(deque.dtype),
                shape=deque.shape,
                dtype=deque.dtype
            )
            for sensor in sensors
        })

