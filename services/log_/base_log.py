from typing import Any
from abc import ABC, abstractmethod

# --
# ...
# --
    
class BaseLog(ABC):
    def __init__(self, **kwarg: Any) -> None:
        pass
    
# --
# ...
# --
   
    instance: Any = None
    def __new__(cls, **kwarg: Any):
        
        if hasattr(cls, 'instance_args'):
            if cls.instance_args != kwarg:
                cls.instance = None
                
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            
            cls.instance_args = kwarg
            
            cls.instance.template_dictionary = cls.get_template_dictionary()
            cls.instance.config_dictionary = cls.get_config_dictionary()
                               
        return cls.instance
    
# --
# ...
# --
    
    @classmethod
    def get_template_dictionary(cls) -> str:
        return ''
    
# --
# ...
# --
    
    @classmethod
    def get_config_dictionary(cls) -> str:
        return ''
    
# --
# ...
# --

    def __call__(self) -> str:
        return self.template