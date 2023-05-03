#4-1 TXT文本文件  r只读打开 r+读写 b二进制 w写入 w+读写存在则覆盖  a追加方式 存在指针在结尾  a+读写
from cgitb import text
import requests
from pyquery import PyQuery as pq
import re
url='https://ssr1.scrape.center/'
html=requests.get(url).text
doc=pq(html)
items=doc('.el-card').items()
file=open('movies.txt','w',encoding='utf-8')
for item in items:
    name=item.find('a>h2').text()
    file.write(f'名称：{name}\n')


#4-2  JSON文件  {}包围的内容-键值对
import json
str='''
[{
    "name":"wenyu",
    "gender":"man",
    "birthday":"1999-09-16"
},{
    "name":"jingchaun",
    "gender":"woman",
    "birthday":"1998-08-15"
}]
'''  #json数据用双引号
print(type(str))
data=json.loads(str)  #字符串转为列表
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))
data=json.load(open('data.json',encoding='utf-8')) 
with open('data.json','w',encoding='utf-8') as f:
    f.write(json.dumps(data,indent=2,ensure_ascii=False))  #调用dumps将json转为字符串写入文本,indent缩进2,ensure输入中文


#4-3  CSV文件