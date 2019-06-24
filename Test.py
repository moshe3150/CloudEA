from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from Links import *


class OpenTheCloudEA(unittest.TestCase):
    Browser.Chrome.maximize_window()
    Browser.Chrome.get(UrlFile.URL.url111)
    assert "https://10.81.4.111/pages/login" in Browser.Chrome.current_url

    def Test(self):
        user = Browser.Chrome
        if WebDriverWait(Browser.Chrome, 1).until(EC.presence_of_element_located((By.ID, "email"))):
            return user
        else:
            return False
        
    UserName = Browser.Chrome.find_element_by_id("email")
    UserName.send_keys(UserLogin.username)
    Password = Browser.Chrome.find_element_by_id("password")
    Password.send_keys(UserLogin.password)
    LoginButton = Browser.Chrome.find_element_by_xpath("/html/body/ui-root/main/ui-login/button")
    LoginButton.click()

    try:
        element = WebDriverWait(Browser.Chrome, 10).until(
            EC.url_to_be(("https://10.81.4.111/pages/dashboard")))
    finally:
        Browser.Chrome.quit()
