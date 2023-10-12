from typing import Any
from abc import ABC, abstractmethod
from drivers.web.web_driver_provider import WebDriverProvider

# --
# ...
# --
    
class BaseJtlShop(ABC):
   
# --
# ...
# --
   
    def __new__(cls, **kwargs: Any):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            
            cls.instance.config_dictionary = cls.get_config_dictionary()
            cls.instance.objects = cls.instance.get_objects()
            
            tempdriver = WebDriverProvider().selenium_webdriver
            
            for item in dir(tempdriver):
                if (item[0:1]!='_') and (item[0:2]!='__'):
                    setattr(cls.instance, item, getattr(tempdriver, item))
                    
        return cls.instance
    
# --
# ...
# --
    
    def __init__(self, *args, **kwargs: Any) -> None:
        pass
    
# --
# ...
# --
    
    @classmethod
    def get_config_dictionary(cls) -> str:
        return None
    
# --
# ...
# --
    
    @classmethod
    def get_objects(cls) -> str:
        return None