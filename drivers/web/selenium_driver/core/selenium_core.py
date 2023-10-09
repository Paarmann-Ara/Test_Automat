from selenium import webdriver
from drivers.core.base_driver import BaseDriver
from drivers.web.selenium_driver.config.selenium_config import SeleniumConfig
from selenium.webdriver.common.keys import Keys
from typing import Any

#--
#...
#--

class SeleniumCore(BaseDriver):
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(self.config_dictionary['chrom_webdriver_path'])
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

    def set_object(self, object:dict):
        if 'id' in object:
            self.current_object = self.driver.find_element_by_id(object['id'])
        elif 'name' in object:
            self.current_object = self.driver.find_element_by_name(object['name'])
        elif 'class_name' in object:
            self.current_object = self.driver.find_elements_by_class_name(object['class_name'])
        elif 'tag_name' in object:
            self.current_object = self.driver.find_element_by_tag_name(object['tag_name'])
        elif 'xpath' in object:
            self.current_object = self.driver.find_elements_by_xpath(object['xpath'])
        elif 'css_selector' in object:
            self.current_object = self.driver.find_elements_by_css_selector(object['css_selector'])
        elif 'link_text' in object:
            self.current_object = self.driver.find_elements_by_link_text(object['link_text'])
                
#--
#...
#--

    def send_keys(self, text=""):
        return self.current_object.send_keys(text)
