import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

driver.get('https://www.naukri.com/nlogin/login')
path='F:/selenium/anvesh2.xlsx'
rows=XLUtils.getROwCount(path,'Sheet1')
driver.maximize_window()
for r in range(2,rows+1):
	username=XLUtils.readData(path,'Sheet1',r,1)
	password=XLUtils.readData(path,'Sheet1',r,2)
	driver.find_element(By.ID,'usernameField').send_keys(username)
	driver.find_element_by_id('passwordField').send_keys(password)
	driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/div/button').click()

	print(driver.title)
	if driver.title=='Home | Mynaukri':
		print('test passed')
		XLUtils.writeData(path,"Sheet1",r,3,'passed')
		XLUtils.writeData(path,"Sheet1",r,3,'passed')
	else:
		print('test filed')
		XLUtils.writeData(path,"Sheet1",r,3,'Failed')
	

	