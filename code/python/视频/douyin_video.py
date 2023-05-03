import requests  #导入数据请求模块
import re
import json
import pprint
import time
from selenium import webdriver
#1.创建浏览器对象
driver=webdriver.Chrome()
#2.输入一个网址
driver.get("https://www.douyin.com/user/MS4wLjABAAAAyM4hwISEd8Hy802c15w8-FLvbNEpShmsUyqZNaqLnhI")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login-pannel"]/div[2]').click()
for y in range(10):
    js="window.scrollBy(0,10000)"  #js='window.scrollTo(x,y)水平和垂直滚动条
    driver.execute_script(js)
    time.sleep(0.5)
#3.提取所有li标签  返回列表
lis=driver.find_elements_by_css_selector('.ECMy_Zdt')
#print(lis)
for li in lis:
    url=li.find_element_by_css_selector('a').get_attribute('href')
    print(url)
    headers={
    'cookie': 'douyin.com; __ac_nonce=062d38796008b071e7f5c; __ac_signature=_02B4Z6wo00f01qKKlOwAAIDDwYBUhqBQPnKiqpBAAMp942; ttwid=1%7CFN3VIZ1iYsv8ZR2A0yXfIodjEteNsZTeyHJoPT_Vd-w%7C1658029974%7C24f1c43c8eb22fcf673d31c20e01a24906e70179d71800be2e1c5d75d09941e8; home_can_add_dy_2_desktop=%220%22; strategyABtestKey=1658029975.412; s_v_web_id=verify_l5os8l2f_CbtAzRce_3ScZ_4Pn6_8cPZ_MvSIGi37yHcn; passport_csrf_token=907e5ddc623cca3349a9baf449235eee; passport_csrf_token_default=907e5ddc623cca3349a9baf449235eee; msToken=657VSh7rlzf76EYbQb2Ej8IenyzWcFl7Mp8qkM_tSBaGtj8VBYZoOWFyu41h1jm2nfA-CpFqWWYEhXccO-dVBpSXGpq7lvdgp83CYGXgtywN; msToken=KvJ71UYU8dSW_zR_3ELXjeQPL1f87w1v6a5zZSAeYLHVKWkY7plIB89oAdolhkHDOhxtZ_z3PWtVQQbaUFI4gMEE0OcwfbBjz4woHYEDpe-ZHUhIXsbQh11buhpDGcQ=; ttcid=80f7e521e8724381842711f92527011c38; tt_scid=m8qfIyNMAYCoGehZ.oHL9OKEeHPNMSvK2t4XwsTxSJXG3YXtT.e2urgMFWrNULlnc5d1; THEME_STAY_TIME=%2219500%22',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }     #用户代理，浏览器基本身份标识，伪装成浏览器,绕过验证码自动登录
    response=requests.get(url=url,headers=headers).text
    #print(response)
    title=re.findall('<title data-react-helmet="true">(.*?)</title>',response)[0]  #正则匹配都是列表，取第一个元素
    #print(title)
    video_url=re.findall('type="application/json">(.*?)</script>',response)[0]
    #print(video_url)
    video_url=requests.utils.unquote(video_url)
    #print(video_url)    #打印字典数据，输出一行
    json_data=json.loads(video_url)
    pprint.pprint(json_data)    #打印格式化效果
#    with open('视频/'+title+'.txt',mode='w') as f:
#        f.write(json.dumps(json_data))  #方便查找url地址
    video_url='https:'+json_data['75']['aweme']['detail']['video']['bitRateList'][0]['playAddr'][0]['src']
    #print(video_url)
    #4.保存视频
    video_content=requests.get(url=video_url,headers=headers).content  #获取二进制数据内容
    with open('视频/video/'+title+'.mp4',mode='wb') as f:
        f.write(video_content)
        print(title,'保存完成')

