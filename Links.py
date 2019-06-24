from PageObject.LoginCloudEA import LoginCloudEAObject
from PageObject.URL.UrlFile import *
from selenium import webdriver
import json


class Browser:
    Chrome = webdriver.Chrome()


class UrlFile:
    URL = UrlFile

#
# class LoginCloudEAPage:
#     LoginCloudEAPage = LoginCloudEAObject


class UserLogin:
    with open(r'PageObject/LoginCloudEA/UserLogin.json') as f:
        UserLoginFile = json.load(f)
        username = UserLoginFile["username"]
        password = UserLoginFile["password"]
