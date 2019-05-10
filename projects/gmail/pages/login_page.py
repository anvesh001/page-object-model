from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
class LoginPage():
	def __init__(self,driver):
		self.driver=driver
		self.username_text_box='txtUsername'
		self.password_text_box='txtPassword'
		self.login_buttom_id='Submit'
	def enter_username(self,username):
		self.driver.find_element_by_id(self.username_text_box).clear()
		self.driver.find_element_by_id(self.username_text_box).send_keys(username)
	def enter_password(self,password):
		self.driver.find_element_by_id(self.password_text_box).clear()
		self.driver.find_element_by_id(self.password_text_box).send_keys(password)
	def click_login(self):
		self.driver.find_element_by_name('Submit').click()