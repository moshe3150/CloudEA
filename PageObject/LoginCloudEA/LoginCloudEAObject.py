class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "email"
        self.password_textbox_id = "password"
        self.login_button_xpath = "/html/body/ui-root/main/ui-login/button"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

