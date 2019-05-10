from selenium import webdriver
import time
import unittest
from projects.gmail.pages.login_page import LoginPage
from projects.gmail.pages.home_page import HomePage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",'..'))
#print('test completed')
class test_login(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(10)
		
	def test_login(self):
		self.driver.get('https://opensource-demo.orangehrmlive.com/index.php/dashboard')
		#login page method
		login=LoginPage(self.driver)
		login.enter_username('Admin')
		login.enter_password('admin123')
		login.click_login()
		#Home page methods
		home=HomePage(self.driver)
		home.click_welcome()
		home.click_logout()
		#self.driver.find_element_by_id('txtUsername').clear()
		#self.driver.find_element_by_id('txtUsername').send_keys('Admin')
		#self.driver.find_element_by_id('txtPassword').clear()
		#self.driver.find_element_by_id('txtPassword').send_keys('admin123')
		#self.driver.find_element_by_id('btnLogin').click()
		#self.driver.find_element_by_partial_link_text('Admin').click()
		#self.driver.find_element_by_id('welcome').click()
		#self.driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print('test completed')
if __name__ == '__main__':
	unittest.main()