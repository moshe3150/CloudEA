from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from Links import Link

import time
from selenium import webdriver


class LoginTheCloudEA(unittest.TestCase):
        try:
            element = WebDriverWait(Link.Chrome, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        finally:
            Link.Chrome.get(Link.URL.url111)

        Link.Chrome.maximize_window()
        Link.Chrome.implicitly_wait(20)
        WebDriverWait.until(EC.presence_of_element_located((By.ID, 'email')))

        def test(self):
            user = Link.Chrome
            if WebDriverWait(Link.Chrome, 1).until(EC.presence_of_element_located((By.ID, "email"))):
                return user
            else:
                return False
        time.sleep(3000)
        UserName = Link.LoginCloudEAObject.UserLogin.UserNameObj
        UserName.send_keys(Link.LoginCloudEAObject.UserLogin.username)

        Password = Link.LoginCloudEAObject.UserLogin.PasswordObj
        Password.send_keys(Link.LoginCloudEAObject.password)

        LoginButton = Link.LoginCloudEAObject.UserLogin.LoginButtonObj
        LoginButton.click()
        try:
            element = WebDriverWait(Link.Chrome, 10).until(
                EC.url_to_be(("https://10.81.4.111/pages/dashboard")))
        finally:
            Link.Chrome.quit()


webdriver.Chrome.quit()





