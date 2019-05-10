from selenium import webdriver
import time
import unittest
from projects.project2.pages.Loginpage import LoginPage
from projects.project2.pages.Homepage import Homepage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",'..'))
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       cls.driver=webdriver.Chrome()
       cls.driver.maximize_window()
       cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login=LoginPage(self.driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()


        homepage=Homepage(self.driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(5)
        #self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        #self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        #self.driver.find_element_by_name('Submit').click()
        #self.driver.find_element_by_id('welcome').click()
        #self.driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test completed')
if __name__ == '__main__':
    unittest.main()