from drivers.web.selenium_driver.core.selenium_core import SeleniumCore
from drivers.web.selenium_driver.config.selenium_config import SeleniumConfig
from selenium.webdriver.common.keys import Keys
from typing import Any
from drivers.core.base_driver import BaseDriver

#--
#...
#--

class SeleniumDriver(BaseDriver):
    def __init__(self) -> None:
        self.driver = SeleniumCore().instance
        
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
            
            try:
                args[0].driver.set_object(args[1])
                args[0].driver.current_object = args[0].driver.current_object
                return function(*args, **kwargs)
            except Exception as exp:
                print(exp)
                
        return inner_function
        
#--
#...
#--
    
    def open(self, url):
        self.driver.get(url)
#--
#...
#--
    
    def close(self):
        self.driver.quit()
        
    
#--
#...
#--

    def forward_page(self)->None:
        self.driver.forward()
    
#--
#...
#--

    def backward_page(self)->None:
        self.driver.backward()
        
#--
#...
#--

    @wait_for_availablity
    def set_text(self, object:dict, text:str, IsClear = True, IsEnter = False, IsUseKey = False, MCounter = 3, IsAbsturz = True, delay = 50, IsRaiseException = True):
        
        try:
                       
            if IsClear:
                self.driver.current_object.clear()
                self.delay(1)
                
            if IsUseKey:
                for chr in text:
                    self.driver.send_keys(chr)
                    
            else:
                self.driver.send_keys(text)
            
            if IsEnter:
                self.driver.send_keys(Keys.ENTER)
                self.delay(1)
                
            self.delay(1)
            
            return True
        
        except Exception as exp:
            print(exp)
            return False
        
#--
#...
#--

    def find_element(self, object:dict):
        return self.driver.find_element(object)
        
#--
#...
#--

    def find_elements(self, object:dict):
        return self.driver.find_elements(object)
        
#--
#...
#--

    def delete_all_cookies(self):
        return self.driver.delete_all_cookies()
        
#--
#...
#--
     
    def get_all_cookies(self):
        return self.driver.get_all_cookies()