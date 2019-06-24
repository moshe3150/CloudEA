from Links import *
import json


class UserLogin:

    UserNameObj = Link.Chrome.find_element_by_id("email")
    PasswordObj = Link.Chrome.find_element_by_id("password")
    LoginButtonObj = Link.Chrome.find_element_by_xpath("/html/body/ui-root/main/ui-login/button")

    with open(r'PageObject/LoginCloudEA/UserLogin.json') as f:
        UserLoginFile = json.load(f)
        username = UserLoginFile["username"]
        password = UserLoginFile["password"]
