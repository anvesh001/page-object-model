from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from projects.amazon.pages.Start_page import startPage
from projects.amazon.pages.login_page import LoginPage
from projects.amazon.pages.logout_page import LogoutPage
import sys
import os
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__),"..",'..'))
class ClassName(unittest.TestCase):
    @classmethod
    def  setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()

    def test_amazon_page(self):

        self.driver.get('https://www.amazon.in/')
#starting page
        start=startPage(self.driver)
        start.first_page()
#login page
        login=LoginPage(self.driver)
        login.enter_user_name('8867818491')
        login.enter_password('Anvesh@402')
        login.click_submit()
#logout page
        logout=LogoutPage(self.driver)
        logout.logout_method()
        #self.driver.find_element_by_id('ap_email').send_keys('8867818491')
        #self.driver.find_element_by_id('continue').click()
        #self.driver.find_element_by_id('ap_password').send_keys('Anvesh@402')
        #self.driver.find_element_by_id('signInSubmit').click()
        #print(self.driver.title)
        #action=ActionChains(self.driver)
        #signout=self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[2]')
        #action.move_to_element(signout)
        #action.perform()
        #self.driver.find_element_by_xpath('//*[@id="nav-item-signout"]/span').click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F:/projects/amazon/Report'))