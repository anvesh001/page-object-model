from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
class HomePage():
	def __init__(self,driver):
		self.driver=driver
		self.welcome_id='welcome'
		self.logout_xpath='//*[@id="welcome-menu"]/ul/li[2]/a'
	def click_welcome(self):
		self.driver.find_element_by_id('welcome').click()
	def click_logout(self):
		self.driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()

