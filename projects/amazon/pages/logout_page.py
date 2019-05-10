class LogoutPage():
    def __init__(self,driver):
        self.driver=driver
        self.mouse_hover='//*[@id="nav-link-accountList"]/span[2]'
        self.logout_xpath='//*[@id="nav-item-signout"]/span'

    def logout_method(self):
        action=ActionChains(self.driver)
        signout=self.driver.find_element_by_xpath(self.mouse_hover)
        action.move_to_element(signout)
        action.perform()
        self.driver.find_element_by_xpath(self.logout_xpath).click()