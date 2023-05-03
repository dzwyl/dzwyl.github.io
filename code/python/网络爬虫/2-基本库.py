#2.1 urllib  实现HTTP请求的发送  request请求模块 error异常处理模块 parse工具模块-拆分、解析、合并url 
#robotparse识别网站的robots.txt文件，判断哪些网站可以爬
from email import header
from pickletools import read_long1
from unittest import result
import urllib.request
from jmespath import search

from soupsieve import match
response=urllib.request.urlopen('https://m.runoob.com/python3/')
print(response.read().decode('utf-8'))
print(response.status) #响应状态码
print(response.getheaders()) #响应头信息
print(response.getheader('Server'))  #server值

#urlopen方法的API  传递data参数用post请求方式  timeout设置超时时间(未响应报错)  context指定SSL设置  cafile-CA证书  capath路径
import urllib.parse
data=bytes(urllib.parse.urlencode({'name':'wenyu'}),encoding='utf-8')
response=urllib.request.urlopen('https://www.httpbin.org/post',data=data,timeout=1)
print(response.read().decode('utf-8'))

#2.2 requests
import requests
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
}
data={'name':'wenyu','age':'23'}  #params传入data数据
response=requests.get('https://www.httpbin.org/get',params=data,headers=headers,timeout=3) #timeout超时设置 永久None
files={'file':open('D:/VSCODE/音乐/wymusic/绿色.mp3','rb')}  #上传文件  verify=False不验证SSL证书
qq=requests.post('https://www.httpbin.org/post',data=data,headers=headers,files=files,verify=False)
print(response)  #响应状态
print(response.text)  #自动构造"url": "https://www.httpbin.org/get?name=wenyu&age=23"
print(response.json())  #转为json数据格式，字典形式  图片、音视频是二进制数据
print(type(response.headers),response.headers)

from requests.packages import urllib3  #忽略警告
urllib3.disable_warnings()
from requests.auth import HTTPBasicAuth #身份校验
q=requests.get('url',auth=('445722658@qq.com','dzw2020020'))

#proxies代理设置 

#保存数据
s=requests.Session()  #相同cookie，在同一浏览器中打开同一站点的不同页面
r=s.get('https://pic2.zhimg.com/v2-de75f35d8741b7dabcef43b5fb7ba9a5_r.jpg')
print(type(r.url),r.url) #类型和数据 status_code  cookie  headers  history
print(r.content)  #前面带b说明是bytes数据
with open('富士山.jpg','wb') as f:
    f.write(r.content)


#2.3  正则表达式
#\w 字母数字下划线  \W 不是字母数字下划线的字符  \s任意空白字符 = [\t\n\r\f]  \S 任意非空字符  \D 非数字字符
#\z 匹配字符串结尾，存在换行还会匹配换行符  \Z  匹配字符串结尾，存在换行匹配到换行前字符
#\G  匹配最后完成匹配的位置  \n  匹配一个换行符  \t 制表符  ^开头  $结尾  .任意字符除了换行符
#[...]一组字符  [^...]不在[]中字符  *  0个或多个表达式  +  一个或多个表达式
# ?匹配0或1个前面的正则表达式片段，非贪婪方式  {n}精确匹配n个前面的表达式  a|b  （）括号内表达式

#非贪婪匹配 .*?  re.S匹配换行符在内的所有字符  re.I忽略大小写  re.L 本地化识别匹配  re.M  多行匹配影响^和$
#re.U根据unicode字符集解析字符，影响\w、\W、\b、\B  re.X  更易于理解
#1.match  从字符串开头开始匹配
import re
content='www.baidu.com'  #转义匹配  前面加\
result=re.match('\w{3}\.\w{5}\.\w{3}',content,re.S)
content='hello 12345 world_this is a regex demo'
result=re.match('^he.*(\d+).*demo$',content,re.S)  #贪婪.*会匹配更多字符
res=re.match('^he.*?(\d+).*?demo$',content)  #加?非贪婪匹配  \d+匹配12345
print(result)
print(result.group())  #输出完整匹配结果
print(result.group(1))  #第一个被()包围的结果 5
print(result.span())  #匹配值的下标  字符串长度
#2.search  扫描整个字符串，返回第一个匹配到的
html='''<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>'''
results=re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
#3.findall  匹配所有相匹配的字符串，返回列表
for result in results:
    print(result)
    print(result[0],result[1])
#4.sub  修改文本
content=re.sub('\d+','',content) #删除数字
print(content)
str.strip() #去除字符串两边空格  lstrip左边空格  rstrip右边空格
#5.compile  将字符串编译成正则表达式对象
content='2022-7-31 22:35'
pattern=re.compile('\d{2}:\d{2}')
result=re.sub(pattern,'',content)
print(result)



#2.4  httpx的使用  requests不支持HTTP/2.0时  hyper和Httpx  pip3 install 'httpx[http2]'
import httpx
response=httpx.get('https://www.httpbin.org/get')
print(response.status_code)
print(response.headers)
print(response.text)

url='https://www.bilibili.com'
client=httpx.Client(httpx2=True)  #默认支持HTTP/1.1
response=client.get(url)

#client参数
headers={'user-agent':'my-app/0.0.1'}
with httpx.Client(headers=headers) as client:
    r=client.get(url)
    print(r.json)