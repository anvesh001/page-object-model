class Homepage():
	def __init__(self,driver):
		self.driver=driver
		self.welcome_id='welcome'
		self.logout_xpath='//*[@id="welcome-menu"]/ul/li[2]/a'
	def click_welcome(self):
		self.driver.find_element_by_id(self.welcome_id).click()


	def click_logout(self):
		self.driver.find_element_by_xpath(self.logout_xpath).click()

