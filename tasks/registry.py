TASK_REGISTRY = {}


def register_task(name):
    def wrapper(cls):
        TASK_REGISTRY[name] = cls
        return cls
    return wrapper


def make_task(name : str, task_cfg : dict):
    if name not in TASK_REGISTRY:
        raise ValueError(f"Unknown task: {name}")
    return TASK_REGISTRY[name](task_cfg)