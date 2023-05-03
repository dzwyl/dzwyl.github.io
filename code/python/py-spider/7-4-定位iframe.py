#多层框架iframe switch_to.frame(iframe的id)
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://mail.qq.com")            
browser.switch_to.frame('login_frame')         #id属性为btlogin，定位到其所在iframe框架
browser.switch_to.default_content()      #切回主文档
#browser.switch_to_frame(browser.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe'))
#iframe里没有id或者name  两种方法
#browser.switch_to_frame(browser.find_element_by_xpath("//iframe[contains(@src,'//accounts.douban.com/passport/login_popup?login_source=anony')]"))