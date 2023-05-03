import requests
from pprint import pprint
import json
import prettytable as pt
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
driver.find_element_by_css_selector('#J-userName').send_keys('15697881481')
driver.find_element_by_css_selector('#J-password').send_keys('dzw20200202')
driver.find_element_by_css_selector('#J-login').click()

driver.implicitly_wait(10)
driver.find_element_by_css_selector('.btn-primary').click()
driver.find_element_by_css_selector('#link_for_ticket').click()
driver.implicitly_wait(10)
time.sleep(1)
driver.find_element_by_css_selector('#qd-closeDefaultWarningWindowDialog_id').click()
driver.find_element_by_css_selector('#fromStationText').click()
driver.find_element_by_css_selector('#fromStationText').clear()
driver.find_element_by_css_selector('#fromStationText').send_keys('杭州')
driver.find_element_by_css_selector('#fromStationText').send_keys(Keys.ENTER)
driver.find_element_by_css_selector('#toStationText').click()
driver.find_element_by_css_selector('#toStationText').clear()
driver.find_element_by_css_selector('#toStationText').send_keys('鹰潭')
driver.find_element_by_css_selector('#toStationText').send_keys(Keys.ENTER)
driver.find_element_by_css_selector('.inp-w #train_date').click()
driver.find_element_by_css_selector('.inp-w #train_date').clear()
driver.find_element_by_css_selector('.inp-w #train_date').send_keys('2022-10-22')
driver.find_element_by_css_selector('#query_ticket').click()

f=open('city.json',encoding='utf-8')
text=f.read()
json_data=json.loads(text)