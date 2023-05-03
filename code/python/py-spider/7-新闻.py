from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
from selenium import webdriver
driver=webdriver.Chrome()
urls=set()
url='https://news.sina.com.cn/china/'
driver.get(url)
data=driver.page_source
soup=BeautifulSoup(data,"html.parser")
for news in soup.select('.feed-card-item'):
    if(len(news.select('h2'))>0):
        a=news.select('a')[0]['href']
        print(a)  #链接
        print(news.select('a')[0].text)  #标题
        urls.add(a)