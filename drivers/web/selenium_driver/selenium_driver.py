from drivers.core.base_driver import BaseDriver
from drivers.web.selenium_driver.core.selenium_core import SeleniumCore
from drivers.web.selenium_driver.config.selenium_config import SeleniumConfig
from selenium.webdriver.common.keys import Keys
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

    # decorator
    # run set_object befor all methode
    def wait_for_availablity(function):
        
        def inner_function(*args, **kwargs):
            args[0].selenium_driver.set_object(args[1])
            args[0].current_object = args[0].selenium_driver.instance.current_object
            return function(*args, **kwargs)
        
        return inner_function
        
#--
#...
#--
    
    def open(self, url):
        self.selenium_driver.get(url)
#--
#...
#--
    
    def close(self):
        self.selenium_driver.quit()
        
#--
#...
#--

    @wait_for_availablity
    def set_text(self, object:dict, text:str, IsClear = True, IsEnter = False, IsUseKey = False, MCounter = 3, IsAbsturz = True, delay = 50, IsRaiseException = True):
        
        try:
                       
            if IsClear:
                self.current_object.clear()
                self.delay(1)
                
            if IsUseKey:
                for chr in text:
                    self.selenium_driver.send_keys(chr)
                    
            else:
                self.selenium_driver.send_keys(text)
            
            if IsEnter:
                self.selenium_driver.send_keys(Keys.ENTER)
                self.delay(1)
                
            self.delay(1)
            
        except Exception as exp:
            print(exp)
            return False
        
#--
#...
#--

    @wait_for_availablity
    def find_elemnts(self, object:dict):
        self.selenium_driver.find_elemnts(object)