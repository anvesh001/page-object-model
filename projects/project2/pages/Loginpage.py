class LoginPage():
	def __init__(self,driver):
		self.driver=driver
		self.username_textbox_id='txtUsername'
		self.password_textbox_id='txtPassword'
		self.login_buttom_id='Submit'
	def enter_username(self,username):
		self.driver.find_element_by_name(self.username_textbox_id).clear()
		self.driver.find_element_by_name(self.username_textbox_id).send_keys(username)
	def enter_password(self,password):
		self.driver.find_element_by_name(self.password_textbox_id).clear()
		self.driver.find_element_by_name(self.password_textbox_id).send_keys(password)
	def click_login(self):
		self.driver.find_element_by_name('Submit').click()
