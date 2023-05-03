#网页源代码搜索playinfo
#发送请求-获取数据-解析数据-保存数据
from urllib import response
import requests
import re
import json
from pprint import pprint
url='https://www.bilibili.com/video/BV14f4y1R7uS'
headers={
    'referer': 'https://www.bilibili.com/v/dance/otaku?tag=284857',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response=requests.get(url=url,headers=headers)
print(response.text)
title=re.findall('property="og:title" content="(.*?)_哔哩哔哩',response.text)[0]
print(title)
html_data=re.findall('<script>window.__playinfo__=(.*?)</script>',response.text)[0]
json_data=json.loads(html_data)
pprint(json_data)
audio_url=json_data['data']['dash']['audio'][0]['baseUrl']
video_url=json_data['data']['dash']['video'][0]['baseUrl']
audio_data=requests.get(url=audio_url,headers=headers).content
video_data=requests.get(url=video_url,headers=headers).content
with open('视频/'+title+'.mp3',mode='wb') as f:
    f.write(audio_data)
#with open('视频/'+title+'.mp4',mode='wb') as g:
#    g.write(video_data)