import torch

import gymnasium as gym

from abc import ABC, abstractmethod

from biguasim.sensors import SensorDefinition

from utils import TensorDeque
from spaces import dict_deque_tensor_space

from .registry import register_task


class BaseTask(ABC):
    @property
    @abstractmethod
    def agent_range_min(self):
        ...
    
    @property
    @abstractmethod
    def agent_range_max(self):
        ...
    
    @property
    @abstractmethod
    def target_range_min(self):
        ...
    
    @property
    @abstractmethod
    def target_range_max(self):
        ...

    @abstractmethod
    def get_observation(self):
        ...

@register_task('hydrone_vision')
class HydroneVisionNavTask(BaseTask):
    config = {
        'agent_type' : "Hydrone",
        'env_type' : "vision_multi_domain"
    }


    def __init__(self, cfg):

        self._sensor = cfg['sensor']
        self._device = cfg['device']
        self._sensor_class = SensorDefinition._sensor_keys_[self._sensor]
        self.obs_buf = TensorDeque(cfg['stack'], self._sensor_class.shape, self._sensor_class.dtype, self._device)

        self.observation_space = dict_deque_tensor_space([self._sensor], self.obs_buf)


    @property
    def agent_range_min(self):
        return (-10, -10, -5)
    
    @property
    def agent_range_max(self):
        return (10, 10, 5)
    
    @property
    def target_range_min(self):
        return (-10, -10, -5)
    
    @property
    def target_range_max(self):
        return (10, 10, 10)
    
    def get_observation(self, state):
        data = state[self._sensor]
        self.obs_buf.append(torch.as_tensor(data, dtype=self._sensor_class.dtype, device=self._device))
