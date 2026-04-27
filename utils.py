import torch

import numpy as np


def numpy_dtype_range(dtype):
    dtype = np.dtype(dtype)

    if np.issubdtype(dtype, np.integer):
        info = np.iinfo(dtype)
        return info.min, info.max

    if np.issubdtype(dtype, np.floating):
        # if dtype precision is higher than float32 → unbounded
        if np.dtype(dtype).itemsize > np.dtype(np.float32).itemsize:
            return -np.inf, np.inf

        info = np.finfo(dtype)
        return info.min, info.max

    raise TypeError(f"Unsupported dtype: {dtype}")

def torch_dtype_range(dtype_or_tensor):
    # Accept torch.dtype OR tensor
    dtype = (
        dtype_or_tensor.dtype
        if isinstance(dtype_or_tensor, torch.Tensor)
        else dtype_or_tensor
    )

    if not isinstance(dtype, torch.dtype):
        raise TypeError(f"Unsupported dtype: {dtype}")

    # Floating types
    if dtype.is_floating_point:
        info = torch.finfo(dtype)

        # Higher precision than float32 → unbounded
        if info.bits > torch.finfo(torch.float32).bits:
            return -torch.inf, torch.inf

        return info.min, info.max

    # Integer types
    info = torch.iinfo(dtype)
    return info.min, info.max

def tensor_rand(lower, upper, shape, generator, device,
                cloned_batch=False, to_numpy=False, to_list=False):

    lower = torch.as_tensor(lower, device=device, dtype=torch.float32)
    upper = torch.as_tensor(upper, device=device, dtype=torch.float32)

    # --- sampling ---
    if cloned_batch:
        tensor = (upper - lower) * torch.rand((1, *shape[1:]),
                                              generator=generator,
                                              device=device) + lower
        tensor = tensor.expand(*shape)
    else:
        tensor = (upper - lower) * torch.rand(shape,
                                              generator=generator,
                                              device=device) + lower

    # --- remove batch dim if shape == (1, N, ...) ---
    if tensor.shape[0] == 1:
        tensor = tensor.squeeze(0)

    # --- output conversions ---
    if to_numpy:
        return tensor.detach().cpu().numpy()

    if to_list:
        return tensor.tolist()

    return tensor

def get_dtype(data, key):
    value = data[key]

    if isinstance(value, np.ndarray):
        return value.dtype

    if isinstance(value, (list, tuple)) and len(value) > 0:
        first = value[0]
        if isinstance(first, np.ndarray):
            return first.dtype

    raise TypeError(f"No numpy array found under key '{key}'")

class TensorDeque:
    __slots__ = ("capacity", "buffer", "head", "size")

    def __init__(self, capacity, element_shape, *, dtype=torch.float32, device=None):
        self.capacity = int(capacity)
        self.buffer = torch.zeros((capacity, *element_shape), dtype=dtype, device=device)
        self.head = 0
        self.size = 0

    @property
    def dtype(self):
        return self.buffer.dtype
    
    @property
    def shape(self):
        return self.buffer.shape

    def append(self, x: torch.Tensor):
        self.buffer[self.head] = x
        self.head = (self.head + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def clear(self):
        self.head = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def to_tensor(self):
        """Chronological order tensor view."""
        if self.size < self.capacity:
            return self.buffer[:self.size]
        return torch.cat((self.buffer[self.head:], self.buffer[:self.head]), dim=0)

    # ----- container behavior -----

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        if idx >= self.size:
            raise IndexError("index out of range")
        real_idx = (self.head - self.size + idx) % self.capacity
        return self.buffer[real_idx]

    def __iter__(self):
        for i in range(self.size):
            yield self[i]

    def __repr__(self):
        return f"TensorDeque(size={self.size}, capacity={self.capacity}, shape={tuple(self.buffer.shape[1:])})"