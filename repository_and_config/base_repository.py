from typing import Any
from abc import ABC, abstractmethod
from repository_and_config.base_dictionary import BaseDictionary

# --
# ...
# --

    
class BaseRepository(ABC):
    def __init__(self, *args, **kwarg: Any) -> None:
        self.dictionary: dict
    
# --
# ...
# --
   
    instance: Any = None
    def __new__(cls,*args:Any, **kwarg: Any):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            
            cls.instance.dictionary = cls.get_dictionary(*args, **kwarg)
            
        cls.instance.dictionary = BaseDictionary(cls.instance.dictionary)
        
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
