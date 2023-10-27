from drivers.web.selenium_driver.core.base_selenium import BaseSelenium
from drivers.web.selenium_driver.config.selenium_config import SeleniumConfig
from selenium.webdriver.common.keys import Keys
from typing import Any


class SeleniumDriver(BaseSelenium):
    def __init__(self) -> None:
        ...

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

        try:

            self.driver.quit()
            return True

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def get(self, url: str = "http://www.google.com") -> bool:

        try:

            self.driver.get(url)
            return True

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def forward(self) -> bool:

        try:

            self.driver.forward()
            return True

        except Exception as exp:
            print(exp)
            return False
# --
# ...
# --

    def backward(self) -> bool:

        try:

            self.driver.back()
            self.delay(3)
            return True

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def switch_driver_on_parent(self) -> bool:

        try:

            self.driver = self.driver.switch_to.default_content()
            return True

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def find_elements(self, element: dict) -> list:

        try:

            key, value = element
            self.current_elements = self.driver.find_elements(key, value)
            return self.current_elements

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def find_element(self, element: dict) -> Any:

        try:

            key, value = element
            self.current_element = self.driver.find_element(key, value)
            return self.current_element

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def send_keys(self, text="") -> bool:

        try:

            self.current_element.send_keys(text)
            return True

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def set_text(self, element: dict, text: str, is_clear=True, is_enter=False, is_use_key=False, wait_for_object=10, delay=0.05) -> bool:

        try:

            try:

                self.wait_and_change_element(self).presence_of_element_located(
                    element, wait_for_secound=wait_for_object)

            except Exception as exp:
                print(exp)

            finally:
                self.find_element(element)

            self.delay(delay)

            if is_clear:
                self.current_element.clear()

            if is_enter:
                text += Keys.ENTER

            if is_use_key:
                for chr in text:
                    self.send_keys(chr)

            else:
                self.send_keys(text)

            self.delay(delay)
            return True

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def click(self, element: dict) -> bool:

        try:

            self.find_element(element)
            self.current_element.click()
            return True

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def delete_all_cookies(self) -> bool:

        try:

            self.driver.delete_all_cookies()
            self.delay(3)
            return True

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def get_all_cookies(self) -> tuple:

        try:

            list_alle_cookies = self.driver.get_cookies()
            return True, list_alle_cookies

        except Exception as exp:
            print(exp)
            return False

# --
# ...
# --

    def gat_navbar_item(self, element: dict, is_return_elemnts=True, is_return_text=True) -> tuple:
        self.find_element(element)
        self.current_elements = self.current_element.find_elements(
            "tag name", "li")

        list_navbar_itemt = [
            navbar_item for navbar_item in self.current_elements if navbar_item.text != ""] if is_return_elemnts else []
        list_navbar_item_text = [
            navbar_item.text for navbar_item in self.current_elements if navbar_item.text != ""] if is_return_text else []

        return list_navbar_itemt, list_navbar_item_text

# --
# ...
# --

    def gat_menu_item(self, element: dict, is_return_elemnts=True, is_return_text=True) -> tuple:
        self.find_element(element)
        self.current_elements = self.current_element.find_elements(
            "tag name", "li")

        list_menu_itemt = [
            menu_item for menu_item in self.current_elements if menu_item.text != ""] if is_return_elemnts else []
        list_menu_item_text = [
            menu_item.text for menu_item in self.current_elements if menu_item.text != ""] if is_return_text else []

        return list_menu_itemt, list_menu_item_text
