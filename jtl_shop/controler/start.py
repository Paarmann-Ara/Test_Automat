import unittest

# --
# ...
# --

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# wd=webdriver.Chrome(service=Service("C:/OneDrive/Manager/WebDrivers/chromedriver.exe"))
# wd.get("https://2-jtl-shop-p-a-7acf6a8f.docker.jtl-software.de/search/?qs=G%C3%BCrtel")
# time.sleep(5)

# elements = wd.find_element(By.CSS_SELECTOR,"#product-list").find_elements("class name", "text-clamp-2")

# for item in elements:
#     print(item.text)
   
module = "jtl_shop.testcase.szenarien.home_page_search_item"
unittest.main(module)



