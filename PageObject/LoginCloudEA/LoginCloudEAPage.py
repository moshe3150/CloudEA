from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Driver:
    Cheome = webdriver.Chrome("C:\Python37\chromedriver.exe")

class UserName:

    userName = Driver.Cheome.find_element_by_id("email")

