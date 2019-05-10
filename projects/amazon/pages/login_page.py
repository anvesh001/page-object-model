class LoginPage():
   def __init__(self,driver):
        self.driver=driver
        self.user_name_id='ap_email'
        self.pass_xpath='//*[@id="ap_password"]'
        self.login_id='signInSubmit'
        self.username='8867818491'
        self.password='Anvesh@402'

   def enter_user_name(self,username):
        self.driver.find_element_by_id(self.user_name_id).clear()
        self.driver.find_element_by_id(self.user_name_id).send_keys(username)
   def enter_password(self,password):
        self.driver.find_element_by_xpath(self.pass_xpath).clear()
        self.driver.find_element_by_xpath(self.pass_xpath).send_keys(self.password)
   def click_submit(self):
        self.driver.find_element_by_id(self.login_id).click()