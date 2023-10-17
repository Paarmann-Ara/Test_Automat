from drivers.core.base_driver import BaseDriver
from selenium import webdriver
from typing import Any
from selenium.webdriver.chrome.service import Service

#--
#...
#--

class BaseSelenium(BaseDriver):
    def __new__(cls, **kwargs: Any):
        if not hasattr(cls, 'instance'):        
            cls.instance = super().__new__(cls)
            
            cls.instance.config_dictionary = cls.get_config_dictionary()
            cls.instance.delay = cls.delay
            
            cls.driver = webdriver.Chrome(service=Service(cls.instance.config_dictionary['selenium_chrom_webdriver_path']))
                                          
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
            return ''