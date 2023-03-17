from typing import Any
from abc import ABC, abstractmethod


# --
# ...
# --
    
class BaseDBConnection(ABC):
    def __init__(self, *args, **kwarg: Any) -> None:
        pass
    
# --
# ...
# --
   
    instance = None
    def __new__(cls, **kwarg: Any):
        
        if hasattr(cls, 'instanceArgs'):
            if cls.instanceArgs != kwarg:
                cls.instance = None
            
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instanceArgs = kwarg
            connectionstring = cls.create_connection_string(**kwarg)
            cls.instance.connection = cls.get_connection(connectionstring)
        
        return cls.instance
    
# --
# ...
# --
    
    @classmethod
    def create_connection_string(cls, **kwarg) -> str:
        return ''
    
# --
# ...
# --
    
    @classmethod
    def get_connection(cls, connectionstring: str) -> Any:
        return ''
    
# --
# ...
# --

    def __call__(self):
        return self.connection
