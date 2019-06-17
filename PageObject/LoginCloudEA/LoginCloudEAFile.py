from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time
import Links

class OpenTheCloudEA(unittest.TestCase):

        Links.LoginCloudEAPage.Driver.Cheome.get(Links.UrlPage.URL.url111)
        Links.UserLogin.User.write(Links.UserLogin.User.usercpmadmin)
        # try:
        #         UrlCurrent = driver.current_url
        #         UrlPage.URL.url111 = UrlCurrent
        # except:
        #         print("The System Not OPen")

        UrlCurrent = Links.LoginCloudEAPage.Driver.Cheome.current_url
        print(UrlCurrent)
        time.sleep(1000)

unittest.main()