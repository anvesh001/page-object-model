from selenium import webdriver
from projects.project3.pages.login_page import LoginPage
from projects.project3.pages.logout_page import LogoutPage
import unittest
import sys
import os
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__),"..",'..'))
class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.get('https://magento.com/products/magento-open-source')
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(10)
	
	def test_login(self):
		#login page
		login=LoginPage(self.driver)
		login.enter_to_login()
		login.enter_username('anveshkumarnaidu402@gmail.com')
		login.enter_password('Anvesh@402')
		login.click_on_login()
		#self.driver.find_element_by_xpath('//*[@id="block-header"]/ul/li[9]/a').click()
		#self.driver.find_element_by_id('email').send_keys('anveshkumarnaidu402@gmail.com')
		#self.driver.find_element_by_id('pass').send_keys('Anvesh@402')
		#self.driver.find_element_by_id('send2').click()
		#home page
		logout=LogoutPage(self.driver)
		logout.click_logout()
		#self.driver.find_element_by_xpath('//*[@id="screen-page"]/div[3]/div[2]/div[1]/div/div[1]/a').click()
	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print('test finished')
if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F:/projects/project3/report'))