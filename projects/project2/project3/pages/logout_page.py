class LogoutPage():
	def __init__(self,driver):
		self.driver=driver
		self.logout_link='Log Out'
	def click_logout(self):
		self.driver.find_element_by_partial_link_text(self.logout_link).click()