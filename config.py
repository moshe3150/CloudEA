from PageObject.HardeningSet import HardeningSetCreateTest
from PageObject.LoginCloudEA import LoginCloudEATest
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                      'CompressionLevel': '9'}

config['bitbucket.org']={}
# class run():
#     def __init__(self, driver):
#         self.driver = driver
#
#     def run_file(self):
#         LoginCloudEATest.LoginTheCloudEA(self.driver)
#         HardeningSetCreateTest.open_configurations(self.driver)

