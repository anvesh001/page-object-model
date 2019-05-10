class startPage():
    def __init__(self,driver):
        self.driver=driver
        self.open_css='#nav-link-accountList > span.nav-line-2'

    def first_page(self):
        self.driver.find_element_by_css_selector(self.open_css).click()