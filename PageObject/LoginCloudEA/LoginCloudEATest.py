from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from Links import *


class LoginTheCloudEA(unittest.TestCase):

        Link.Chrome.maximize_window()
        Link.Chrome.implicitly_wait(20)
        Link.Chrome.get(Link.URL.URL111)
        WebDriverWait.until(EC.presence_of_element_located((By.ID, 'email')))

        def Test(self):
            user = Link.Chrome
            if WebDriverWait(Link.Chrome, 1).until(EC.presence_of_element_located((By.ID, "email"))):
                return user
            else:
                return False
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





