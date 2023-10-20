from drivers.web.selenium_driver.core.base_selenium import BaseSelenium
from drivers.web.selenium_driver.config.selenium_config import SeleniumConfig
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from typing import Any

# --
# ...
# --


class SeleniumDriver(BaseSelenium):
    def __init__(self) -> None:
        self.current_object = None

# --
# ...
# --

    @classmethod
    def get_config_dictionary(cls):
        return SeleniumConfig().instance.dictionary

# --
# ...
# --

    def quit(self) -> bool:
        self.driver.quit()
        return True

# --
# ...
# --

    def get(self, url: str = "http://www.google.com") -> bool:
        self.driver.get(url)
        return True


# --
# ...
# --

    def forward(self) -> bool:
        self.driver.forward()
        return True

# --
# ...
# --

    def backward(self) -> bool:
        self.driver.back()
        self.delay(3)
        return True

# --
# ...
# --

    def set_object(self, object: dict, wait_for_secound=2):

        try:

            self.current_object = WebDriverWait(self.driver, wait_for_secound).until(
                expected_conditions.presence_of_element_located(object)
            )

        finally:
            pass

# --
# ...
# --

    def find_elements(self, object):
        Key, Value = object
        return self.driver.find_elements(Key, Value)

# --
# ...
# --

    def find_element(self, object):
        Key, Value = object
        return self.driver.find_element(Key, Value)

# --
# ...
# --

    def send_keys(self, text=""):
        self.driver.send_keys(text)
        return True

# --
# ...
# --

    def click(self):
        self.driver.click()
        return True

# --
# ...
# --

    def delete_all_cookies(self):

        try:

            self.driver.delete_all_cookies()
            self.delay(3)
            return True

        except Exception as exp:
            print(exp)

# --
# ...
# --

    def get_all_cookies(self):
        list_alle_cookies = self.driver.get_cookies()
        return list_alle_cookies

# --
# ...
# --

    def set_text(self, object: dict, text: str, IsClear=True, IsEnter=False, IsUseKey=False, MCounter=3, IsAbsturz=True, delay=50, IsRaiseException=True):
        ...
