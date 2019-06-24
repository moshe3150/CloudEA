from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from Links import *
import time
from selenium import webdriver


class LoginTheCloudEA(unittest.TestCase):
        try:
            element = WebDriverWait(Chrome, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        finally:
            Chrome.get(URL.URL111)

        Chrome.maximize_window()
        Chrome.implicitly_wait(20)
        WebDriverWait.until(EC.presence_of_element_located((By.ID, 'email')))

        def test(self):
            user = Chrome
            if WebDriverWait(Chrome, 1).until(EC.presence_of_element_located((By.ID, "email"))):
                return user
            else:
                return False
        time.sleep(3000)
        UserName = LoginCloudEAObject.UserLogin.UserNameObj
        UserName.send_keys(LoginCloudEAObject.UserLogin.username)

        Password = LoginCloudEAObject.UserLogin.PasswordObj
        Password.send_keys(LoginCloudEAObject.password)

        LoginButton = LoginCloudEAObject.UserLogin.LoginButtonObj
        LoginButton.click()
        try:
            element = WebDriverWait(Chrome, 10).until(
                EC.url_to_be(("https://10.81.4.111/pages/dashboard")))
        finally:
            Chrome.quit()


webdriver.Chrome.quit()





