from drivers.web.selenium_driver.selenium_driver import SeleniumDriver

#--
#...
#--


class WebDriverProvider:
    def __init__(self) -> None:
        self.selenium_webdriver = SeleniumDriver().instance
