#encoding:utf-8
'''
@author: guanyf
@contact:guanyf3@lenovo.com
@tel :18837121280
'''
'''
##############################
#                             #
#           开发者中心        #
#                            #
#############################
'''
from selenium import webdriver
import time
import unittest
from fiox.firefox_test import data
class test_center(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.get(data.url)
        time.sleep(2)
        self.driver.find_element_by_xpath(data.Bro_dev_Center).click()
        time.sleep(2)
        for i in self.driver.window_handles:
            if i != self.driver.current_window_handle:
                self.driver.switch_to_window(i)
                print(i + u"跳转成功")
    def tearDown(self):
        self.driver.quit()