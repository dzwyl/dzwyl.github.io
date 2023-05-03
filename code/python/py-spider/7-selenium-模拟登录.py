from numpy import source
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
browser=webdriver.Chrome()
browser.get('http://www.taobao.com/')
#print(browser.page_source)   #打印网页源代码
search1=browser.find_element_by_id("q")    #查找id是q单个元素
print(search1)
lis=browser.find_elements_by_css_selector("li")     #查找css类名是li多个元素
#lis_c=browser.find_elements(By.CSS_SELECTOR,"li")
#print(lis)

from selenium import webdriver
from selenium.webdriver import ActionChains  #鼠标-交互操作
import time
browser=webdriver.Chrome()
browser.get('http://www.taobao.com/')
search1=browser.find_element_by_id("q") 
search1.send_keys("apple")   #  交互操作  输入内容apple
button=browser.find_element_by_class_name("btn-search")
button.click()       #查找按钮并点击
time.sleep(8)

browser.switch_to.frame("iframeResult")
source=browser.find_element_by_id("draggable")   #确定拖拽目标起点和终点
target=browser.find_element_by_id("droppable")
actions=ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()

from selenium import webdriver    #执行Javascript脚本，进度条拉倒最大并弹出提示框
browser=webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
browser.execute_script("alert('To Button')")

from selenium import webdriver         #获取元素信息
browser=webdriver.Chrome()
browser.get("https://mail.qq.com/")
logo=browser.find_element_by_id("wxLoginTab")
print(logo) 
print(logo.get_attribute("class"))   #获取元素class属性信息、文本内容、id、位置、标签名、大小
print(logo.text)   
print(logo.id)
print(logo.location)
print(logo.tag_name)
print(logo.size)

from selenium import webdriver         #获取元素信息
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser=webdriver.Chrome()
browser.get("https://www.taobao.com")
browser.implicitly_wait(8)         #隐式等待
wait=WebDriverWait(browser,10)     #显式等待
input=wait.until(EC.presence_of_element_located((By.ID,"q")))
button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".btn-search")))
print(input,button)

from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://www.bilibili.com")
browser.get("https://www.taobao.com")
browser.get("https://www.baidu.com")
browser.back()  #后退
time.sleep(2)
browser.forward()#前进

from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.bilibili.com")
print(browser.get_cookies())         #获取所有cookies
browser.add_cookie({"name":"biubiu","value":"germey"})    #添加cookies
print(browser.get_cookies())
browser.delete_all_cookies()    #清空cookies
print(browser.get_cookies())

from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://www.bilibili.com")
browser.execute_script("window.open()")   #打开新页面
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])   #切换页面
browser.get("https://www.baidu.com")
time.sleep(2)
browser.switch_to_window(browser.window_handles[0])    #切换页面
browser.get("https://python.org")

