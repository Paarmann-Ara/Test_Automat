from typing import Any
from abc import ABC, abstractmethod

# --
# ...
# --
    
class Base(ABC):
    def __init__(self, *args, **kwargs: Any) -> None:
        pass
    
# --
# ...
# --
   
    instance: Any = None
    def __new__(cls, **kwargs: Any):
        
        if cls.instance:
                return cls.instance
                
        else:
            cls.instance = super().__new__(cls)

        print(f"{__class__.__name__}: cls.Instance.id= {id(cls.instance)}")
        return cls.instance