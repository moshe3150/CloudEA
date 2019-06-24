from Links import *
import json
from selenium import webdriver

Chrome = webdriver.Chrome()

class UserLogin:
    UserNameObj = Chrome.find_element_by_id("email")
    PasswordObj = Chrome.find_element_by_id("password")
    LoginButtonObj = Chrome.find_element_by_xpath("/html/body/ui-root/main/ui-login/button")

    with open(r'PageObject/LoginCloudEA/UserLogin.json') as f:
        UserLoginFile = json.load(f)
        username = UserLoginFile["username"]
        password = UserLoginFile["password"]
