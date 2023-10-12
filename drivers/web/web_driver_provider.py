from drivers.web.selenium_driver.selenium_driver import SeleniumDriver
from drivers.core.base_driver import BaseDriver

#--
#...
#--


class WebDriverProvider(BaseDriver):
    def __init__(self) -> None:
        self.selenium_webdriver = SeleniumDriver().instance
        
        print(f"{__class__.__name__}:{id(self.instance)}")
