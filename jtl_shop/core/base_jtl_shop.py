from typing import Any
from abc import ABC, abstractmethod
from drivers.web.web_driver_provider import WebDriverProvider

# --
# ...
# --
    
class BaseJtlShop(ABC):
    def __init__(self, *args, **kwargs: Any) -> None:
        pass
    
# --
# ...
# --
   
    instance: Any = None
    def __new__(cls, **kwargs: Any):
        
        if hasattr(cls, 'instance_args'):
            if cls.instance_args != kwargs:
                cls.instance = None
                
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            
            cls.instance_args = kwargs
            
            cls.instance.config_dictionary = cls.get_config_dictionary()
            
            tempdriver = WebDriverProvider().selenium_webdriver
            
            for item in dir(tempdriver):
                if (item[0:1]!='_') and (item[0:2]!='__'):
                    setattr(cls.instance, item, getattr(tempdriver, item))
            
        return cls.instance
    
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
