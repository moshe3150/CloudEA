import unittest
from selenium.webdriver import Chrome
from PageObject.LoginCloudEA.LoginCloudEAObject import LoginPage

class LoginTheCloudEA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome(executable_path="C:/automation/CloudEA/driver/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.set_page_load_timeout(10)

    def test_login(self):
        driver = self.driver
        driver.get("https://10.81.4.111:4432/pages/login")
        login = LoginPage(driver)
        login.enter_username("cpmadmin")
        login.enter_password("Welcome1!")
        login.click_login()
        driver.set_page_load_timeout(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()
