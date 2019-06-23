from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import unittest
import time
from Links import *

class LoginTheCloudEA(unittest.TestCase):

        def openCloudEA(self):
                Browser.Chrome.maximize_window()
                Browser.Chrome.implicitly_wait(20)
                Browser.Chrome.get(URL.URL111)
                WebDriverWait.until(EC.presence_of_element_located((By.ID, 'email')))

class Login():
        LoginCloudEAPage.UserName.send_keys("cpmadmin")
        LoginCloudEAPage.Password.send_keys("Welcome!")


webdriver.Chrome.quit()