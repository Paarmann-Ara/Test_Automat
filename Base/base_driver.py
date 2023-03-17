from typing import Any
from abc import ABC, abstractmethod
from log_all.log import Log

# --
# ...
# --

    
class BaseDriver(ABC):
    def __init__(self, *args, **kwarg: Any) -> None:
        pass
    
# --
# ...
# --
   
    instance: Any = None
    def __new__(cls,*args:Any, **kwarg: Any):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.log_info = Log(template='Pipeline',config='Pipeline').instance
            cls.instance.log_error = Log(template='Error',config='Error').instance
            
        return cls.instance