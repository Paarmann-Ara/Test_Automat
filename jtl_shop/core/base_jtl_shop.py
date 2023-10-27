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
            cls.instance.elements = cls.instance.get_elements()
            
            temp_selenium_driver = WebDriverProvider().selenium_driver
            
            for methode in dir(temp_selenium_driver):
                if (methode[0:1]!='_') and (methode[0:2]!='__'):
                    setattr(cls.instance, methode, getattr(temp_selenium_driver, methode))
                    
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
    def get_elements(cls) -> str:
        return None