import biguasim
import json
import torch

import numpy as np

from gymnasium import Env

from biguasim.util import gpu
from biguasim.sensors import SensorDefinition

from utils import TensorDeque, tensor_rand, get_dtype
from tasks.registry import make_task

class BaseEnv(Env):
    def __init__(self, task, tasf_cfg, batch_size, seed, show_viewport):

        self._device = torch.device('cuda:'+ str(gpu()) if torch.cuda.is_available() else 'cpu')
        self._idxs = torch.arange(batch_size, device=self._device)
        
        self._rew_buf = torch.zeros((batch_size,), device=self._device).double()
        self._terminated_buf = torch.ones((batch_size,), device=self._device)
        self._truncated_buf = torch.ones((batch_size,), device=self._device)
        self._episode_length_buf = torch.zeros((batch_size,), device=self._device)

        self._torch_rng = torch.Generator(device=self._device)
        self._torch_rng.manual_seed(seed)

        self._batch_size = batch_size
        self._sensors = list()

        tasf_cfg['device'] = self._device
        self._task = make_task(task, tasf_cfg)
        
        biguasim_cfg = self._load_scenario_config(f'hover_{self._task.config['env_type']}')
        biguasim_cfg['agents'][0]['agent_type'] = self._task.config['agent_type']
        biguasim_cfg['agents'][0]['batch_size'] = batch_size

        self._env = biguasim.make(scenario_cfg=biguasim_cfg, show_viewport=show_viewport)
        action_shape = self._env.action_space.shape

        self._actions = torch.zeros((batch_size, *action_shape), device=self._device).double()
        self._last_actions = torch.zeros_like(self._actions)

        
        

    def _set_dtype(self, sensors : list):
        self._dtype = {sensor : None for sensor in sensors}

    def _load_scenario_config(self, scenario : str) -> dict:
        with open(f"./configs/{scenario}.json") as f:
            cfg = json.load(f)
        return cfg
    

    def _resample_agent(self, agent_name : str = 'main' , same_batch_location : bool = True, same_batch_rotation : bool =True):
        if same_batch_location:
            location = tensor_rand(self.agent_range_min, 
                                   self.agent_range_max, 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device, 
                                   cloned_batch=True, 
                                   to_list=True)
        else:
            location = tensor_rand(self.agent_range_min, 
                                   self.agent_range_max, 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device, 
                                   to_list=True)
            
        if same_batch_rotation:
            rotation = tensor_rand((0,0,-180), 
                                   (0,0,180), 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device, 
                                   cloned_batch=True, 
                                   to_list=True)
        else:
            rotation = tensor_rand((0,0,-180), 
                                   (0,0,180), 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device, 
                                   to_list=True)
            
        idxs = range(self._idxs.shape[0]) if self._idxs.shape[0] > 1 else 0
        self._env.move_agent(agent_name, location, rotation, idxs)



    def _reset(self, seed : int = None) -> dict:
        self._last_actions[self._idxs] = 0.0
        self._episode_length_buf[self._idxs] = 0
        self._terminated_buf[self._idxs] = True
        self._truncated_buf[self._idxs] = True
        if seed:
            self._torch_rng.manual_seed(seed)

        state = self._env.reset()
        state.pop('t')
        return state
    

class NavEnv(BaseEnv):
    def __init__(self, task, tasf_cfg, batch_size, seed, show_viewport):
        super().__init__(task, tasf_cfg, batch_size, seed, show_viewport)

    def _resample_target(self, same_batch_location : bool = False, same_batch_rotation : bool =False):
        if same_batch_location:
            location = tensor_rand(self.agent_range_min, 
                                   self.agent_range_max, 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device, 
                                   cloned_batch=True)
        else:
            location = tensor_rand(self.agent_range_min, 
                                   self.agent_range_max, 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device)
            
        if same_batch_rotation:
            rotation = tensor_rand((0,0,-180), 
                                   (0,0,180), 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device, 
                                   cloned_batch=True)
        else:
            rotation = tensor_rand((0,0,-180), 
                                   (0,0,180), 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device)
            
        self._target_buf = torch.cat([location, rotation], dim=1)

    def reset(self, *args, seed = None, options = None):
        
        state = self._process_state(self._reset(seed=seed))
        if args[0]:
            self._resample_target(*args[1:])

        return state









































        

class HoverEnv(BaseEnv):
    sensors = [
        'DynamicsSensor',
        'DenoiseIMUSensor'
        'NoiseIMUSensor'
    ]

    def __init__(self, agent_type, env_type, sensors, batch_size, seed, show_viewport):
        biguasim_cfg = self._load_scenario_config(f'hover_{env_type}')
        biguasim_cfg['agents'][0]['agent_type'] = agent_type
        biguasim_cfg['agents'][0]['batch_size'] = batch_size

        super().__init__(batch_size, seed, self.sensors, biguasim_cfg, show_viewport)

        self._sensors = sensors

        self.obs_buf = None
        self._target_buf = torch.zeros((batch_size, 6), device=self._device)

    def _resample_target(self, same_batch_location= False, same_batch_rotation=False):
        if same_batch_location:
            location = tensor_rand(self.agent_range_min, 
                                   self.agent_range_max, 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device, 
                                   cloned_batch=True)
        else:
            location = tensor_rand(self.agent_range_min, 
                                   self.agent_range_max, 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device)
            
        if same_batch_rotation:
            rotation = tensor_rand((0,0,-180), 
                                   (0,0,180), 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device, 
                                   cloned_batch=True)
        else:
            rotation = tensor_rand((0,0,-180), 
                                   (0,0,180), 
                                   (self._batch_size, 3), 
                                   self._torch_rng, 
                                   self._device)
            
        self._target_buf = torch.cat([location, rotation], dim=1)

    def _process_state(self, state : dict):
        stack = []
        if len(self._sensors) > 1:
            for sensor in self._sensors:
                if self._dtype[sensor] is None:
                    self._dtype[sensor] = get_dtype(state, sensor)
                stack.append(torch.as_tensor(state[sensor], device=self._device, dtype=self._dtype[sensor]))

            return torch.cat(stack, dim=1)
        
        sensor = self._sensors[0]
        if self._dtype[sensor] is None:
            self._dtype[sensor] = get_dtype(state, sensor)
        
        return torch.as_tensor(state[sensor], device=self._device, dtype=self._dtype[sensor])


    def reset(self, *args, seed = None, options = None):
        
        state = self._process_state(self._reset(seed=seed))
        if args[0]:
            self._resample_target(*args[1:])

        return state

        

        





    
    
