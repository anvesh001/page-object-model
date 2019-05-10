class LoginPage():
	def __init__(self,driver):
		self.driver=driver
		self.click_login_entry='//*[@id="block-header"]/ul/li[9]/a'
		self.username_id='email'
		self.password_id='pass'
		self.click_login='send2'
	def enter_to_login(self):
		self.driver.find_element_by_xpath(self.click_login_entry).click()
	def enter_username(self,username):
		self.driver.find_element_by_id(self.username_id).clear()
		self.driver.find_element_by_id(self.username_id).send_keys(username)
	def enter_password(self,password):
		self.driver.find_element_by_id(self.password_id).clear()
		self.driver.find_element_by_id(self.password_id).send_keys(password)
	def click_on_login(self):
			self.driver.find_element_by_id(self.click_login).click()




