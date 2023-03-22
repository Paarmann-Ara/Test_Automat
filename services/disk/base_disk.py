from typing import Any
from abc import ABC, abstractmethod


# --
# ...
# --
    
class BaseDisk(ABC):
    def __init__(self, **kwarg: Any) -> None:
        pass
    
# --
# ...
# --
   
    instance: Any = None
    def __new__(cls, *args, **kwarg: Any):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)

        return cls.instance
    
# --
# ...
# --

    def __call__(self) -> str:
        return self.instance
