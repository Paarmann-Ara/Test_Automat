from drivers.core.base_driver import BaseDriver
from drivers.web.selenium_driver.core.selenium_core import SeleniumCore
from drivers.web.selenium_driver.config.selenium_config import SeleniumConfig
from typing import Any

#--
#...
#--

class SeleniumDriver(BaseDriver):
    def __init__(self) -> None:
        self.selenium_driver = SeleniumCore().instance
        
        
#--
#...
#--

    @classmethod
    def get_config_dictionary(cls):
        return SeleniumConfig().instance.dictionary
        
#--
#...
#--
    
    def open(self, url):
        self.selenium_driver.get(url)

#--
#...
#--

    def set_text(self, object:dict, text:str):
        self.selenium_driver.set_object(object)
        self.selenium_driver.send_keys(text)
