from selenium import webdriver
import unittest
import HtmlTestRunner
class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_search_automation_stepbystep(self):
        self.driver.get('http://www.google.com')
        self.driver.find_element_by_name('q').send_keys('Automation step by step')
        self.driver.find_element_by_name('btnK').click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test completed')
if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F:/project/Reports'))

