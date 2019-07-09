from PageObject.HardeningSet.HardeningSetCreateObject import open_configurations
import unittest
import time

class create_hardening_set(unittest.TestCase):

    def test_open_configurations_page(self):
        driver = self.driver
        configurations = open_configurations(driver)
        time.sleep(10)
        configurations.open_configuration_page()
        configurations.enter_hardening_set_tab()