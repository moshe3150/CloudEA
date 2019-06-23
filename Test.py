from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import unittest
# import time
#
#
# class OpenTheCloudEA(unittest.TestCase):
#
#     Chrome = webdriver.Chrome("C:\Python37\chromedriver.exe")
#     url111 = "https://10.81.4.111/pages/login"
#
#     Chrome.maximize_window()
#     Chrome.get(url111)
#     assert "https://10.81.4.111/pages/login" in Chrome.current_url
#     WebDriverWait(Chrome, 1).until(EC.presence_of_element_located((By.ID, "email")))
#     UserName = Chrome.find_element_by_id("email")
#     UserName.send_keys("cpmadmin")
#     Password = Chrome.find_element_by_id("password")
#     Password.send_keys("Welcome1!")
#     LoginButton = Chrome.find_element_by_xpath("/html/body/ui-root/main/ui-login/button")
#     LoginButton.click()
#     time.sleep(3000)
#     assert "https://10.81.4.111/pages/dashboard" in Chrome.current_url
#     Chrome.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://10.81.4.111")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
finally:
    driver.quit()