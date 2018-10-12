# encoding: utf-8
'''
@author: guanyf
@contact:guanyf3@lenovo.com
@tel :18837121280
'''
from fiox.firefox_test.browser_Page_jump import browser_developer_center
import test_login
class test_account_setting(browser_developer_center.test_center):
    @test_login.test_1
    def test_setting(self):
        print("sss")
