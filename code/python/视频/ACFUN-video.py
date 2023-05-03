#m3u8视频格式会分成很多小片段
import requests
import re
from selenium import webdriver
import pprint
import json
url='https://www.acfun.cn/v/ac34841217'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response=requests.get(url=url,headers=headers)
#pprint.pprint(response.text)
acfun=response.text
title=re.findall('<title >(.*?) - AcFun弹幕视频网',acfun)[0]
#print(title)
htmldata=re.findall('window.pageInfo = window.videoInfo = (.*?);',acfun)[0]
print(htmldata)
m3u8=json.loads(json_data)
for ts in m3u8:
    tsurl=''+ts
    ts.content=requests.get(url=tsurl,headers=headers).content
    with open('video\\'+title+'.mp4',mode='wb') as f:
        f.write(ts.content)
        print(title,'保存完成')