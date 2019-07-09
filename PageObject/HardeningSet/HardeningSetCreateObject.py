class open_configurations():

    def __init__(self, driver):
        self.driver = driver

        self.configurations_page_xpath = "/html/body/ui-root/main/ui-layout/div[2]/ui-sidebar/ul/li[5]"
        self.hardening_set_tab_xpath = "/html/body/ui-root/main/ui-layout/div[2]/main/ui-configurations-main/div/p-tabmenu/div/ul/li[5]/a/span"

    def open_configuration_page(self):
        self.driver.find_element_by_xpath(self.configurations_page_xpath).click()

    def enter_hardening_set_tab(self):
        self.driver.find_element_by_xpath(self.hardening_set_tab_xpath).click()

