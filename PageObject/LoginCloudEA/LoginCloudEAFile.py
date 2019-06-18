from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import Links
from Links import LoginCloudEAPage



# class OpenTheCloudEA(unittest.TestCase):
LoginCloudEAPage.Driver.Chrome.maximize_window()
LoginCloudEAPage.Driver.Chrome.implicitly_wait(20)
LoginCloudEAPage.Driver.Chrome.get(Links.UrlPage.URL.url111)

try:
        element = WebDriverWait(LoginCloudEAPage.Driver.Chrome, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
        )
        print(element)
        time.sleep(3000)
finally:
        LoginCloudEAPage.Driver.Chrome.quit()
        # Links.LoginCloudEAPage.UserName.userName(Links.UserLogin.User.usercpmadmin)
        # try:
        #         UrlCurrent = driver.current_url
        #         UrlPage.URL.url111 = UrlCurrent
        # except:
        #         print("The System Not OPen")

        UrlCurrent = Links.LoginCloudEAPage.Driver.Chrome.current_url
        print(UrlCurrent)
        # time.sleep(1000)

unittest.main()