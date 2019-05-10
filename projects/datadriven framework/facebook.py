import selenium
import XLUtils
from selenium import webdriver
#username=str(input('enter your username:'))
#password=str(input('enter your passowrd:'))
driver=webdriver.Chrome()
driver.get('http://www.facebook.com/')
driver.maximize_window()
path='F:/testdata.xlsx'
rows=XLUtils.getROwCount(path,'Sheet1')
#columns=getCOlumnCount(path,'Sheet1')
print(rows)
#print(columns)
for r in range(2,rows+1):
    username=XLUtils.readData(path,'Sheet1',r,1)
    password=XLUtils.readData(path,'Sheet1',r,2)
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_name('pass').send_keys(password)
    driver.find_element_by_xpath('//*[@id="u_0_2"]').click()
    if driver.title=='Facebook – log in or sign up':
        print('username&password valid')
        XLUtils.writeData(path,"Sheet1",r,3,'passed')
    else:
       print('username&passowrd inavalid')
       XLUtils.writeData(path,"Sheet1",r,3,'falied')
driver.close()