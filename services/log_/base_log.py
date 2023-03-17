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
        
        if hasattr(cls, 'instanceArgs'):
            if cls.instanceArgs != kwarg:
                cls.instance = None
                
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            
            cls.instanceArgs = kwarg
            
            cls.instance.template_dictionary = cls.get_template_dictionary()
            cls.instance.config_dictionary = cls.get_config_dictionary()
            
            if 'template' in kwarg:
                cls.instance.log_template = cls.instance.template_dictionary[kwarg['template']]
            else: 
                cls.instance.log_template = ''
                
            cls.instance.log_config = cls.instance.config_dictionary[kwarg[__name__.split('.')[1]]]
                   
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