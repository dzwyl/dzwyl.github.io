from selenium import webdriver
import time
import shutil,os
browser=webdriver.Chrome()
browser.get("https://mail.qq.com")
#browser.find_element_by_xpath('//*[@id="wxLoginTab"]').click()  #微信登录
#time.sleep(2)
#browser.find_element_by_xpath('//*[@id="qqLoginTab"]').click()   #QQ登录
#browser.find_element_by_xpath('//*[@id="auto_login_qq"]').click() #自动登录
browser.switch_to.frame("login_frame")
browser.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
browser.find_element_by_xpath('//*[@id="u"]').send_keys("445722658@qq.com")
browser.find_element_by_xpath('//*[@id="p"]').send_keys("dzw20200202")
browser.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(3)
browser.save_screenshot('qqmail.png')   #抓拍登录网站后图片
aa=os.getcwd()
name='qqmail.png'
respath=os.path.join(aa,name)
targetpath=r'D:/VSCODE/py-spider/'
shutil.move(respath,targetpath)
