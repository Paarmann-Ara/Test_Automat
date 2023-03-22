from typing import Any
from abc import ABC, abstractmethod
from config_dictionary.defualt_dictionary import DefaultDictionary

# --
# ...
# --

    
class BaseDictionary(ABC):
    def __init__(self, *args, **kwarg: Any) -> None:
        self.dictionary: dict
    
# --
# ...
# --
   
    instance: Any = None
    def __new__(cls,*args:Any, **kwarg: Any):
        
        if hasattr(cls, 'instance_args') or hasattr(cls, 'instance_kwarg'):
            if cls.instance_kwarg != kwarg or cls.instance_args != args :
                cls.instance = None
                
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)

            cls.instance_args = args
            cls.instance_kwarg = kwarg
              
            cls.instance.dictionary = cls.get_dictionary(*args, **kwarg)
            
        cls.instance.dictionary = DefaultDictionary(cls.instance.dictionary)
        
        return cls.instance
    
# --
# ...
# --
    
    @classmethod
    def get_dictionary(cls, *args, **kwarg) -> dict:
        return {}
    
# --
# ...
# --

    def __call__(self, key: str, value: str = '') -> str:

        if value:
            self.dictionary[key] = value
        return self.dictionary[key]
