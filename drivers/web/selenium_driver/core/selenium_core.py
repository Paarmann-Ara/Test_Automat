from drivers.web.selenium_driver.core.base_selenium import BaseSelenium
from drivers.web.selenium_driver.config.selenium_config import SeleniumConfig
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from typing import Any

#--
#...
#--
class SeleniumCore(BaseSelenium):
    def __init__(self) -> None:
        self.current_object = None
           
#--
#...
#--

    @classmethod
    def get_config_dictionary(cls):
        return SeleniumConfig().instance.dictionary
        
#--
#...
#--

    def quit(self):
        return self.driver.quit()
        
#--
#...
#--

    def get(self, url="http://www.google.com"):
        self.driver.get(url)
        return True

#--
#...
#--

    def set_object(self, object:dict,wait_for_secound=2):
        
        try:
            
            self.current_object = WebDriverWait(self.driver, wait_for_secound).until(
                expected_conditions.presence_of_element_located(object.popitem())
            )
            
        finally:
            pass

#--
#...
#--
        
    def find_elemnt(self, object):
        if 'id' in object:
            self.current_object = self.driver.find_element_by_id(object['id'])
            
        elif 'name' in object:
            self.current_object = self.driver.find_element_by_name(object['name'])
            

#--
#...
#--
        
    def find_elements(self, object):
        Key, Value = object.popitem()
        return self.driver.find_elements(Key, Value)
            
#--
#...
#--
        
    def find_element(self, object):
        Key, Value = object.popitem()
        return self.driver.find_element(Key, Value)
                
#--
#...
#--
            
    def current_object_text(self) -> str:
        if self.current_object:
            print(f"{__class__.__name__}'curent object is:\n\n'{self.current_object.text}")
        print(f"{__class__.__name__}'curent object is None'")
                
#--
#...
#--

    def send_keys(self, text=""):
        return self.current_object.send_keys(text)
