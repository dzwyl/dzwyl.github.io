from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()  #全屏
driver.get("https://www.douyin.com/user/MS4wLjABAAAAyM4hwISEd8Hy802c15w8-FLvbNEpShmsUyqZNaqLnhI")
#js="var q=document.documentElement.scrollTop=10000"  firefox和ie用 chrome用body
js="var q=document.documentElement.scrollTop=10000"  #js='window.scrollTo(x,y)水平和垂直滚动条
driver.execute_script(js)
time.sleep(3)