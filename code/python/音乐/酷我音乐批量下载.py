import requests
import re
import os
import random
key = '梁静茹' #请输入你要搜索的歌曲或者歌手名
if not os.path.exists(f'F:/music/{key}'):
    os.mkdir(f'F:/music/{key}') #创建目录
    os.mkdir(f'F:/dzw9.github.io/music/{key}')
for i in range(4):
    url1=f'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={key}&pn={i+1}&rn=30&httpsStatus=1&reqId=e83a5051-0cf5-11ed-bc32-15ed49d9574c'
    headers={
        'Cookie': '_ga=GA1.2.506250583.1682771633; _gid=GA1.2.785699681.1682771633; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1682771635; uname3=Virgo; t3kwid=237439976; userid=237439976; websid=372970670; pic3="http://q.qlogo.cn/qqapp/100243533/30EADEB08D3BAB9E64E18D943A55149E/100"; t3=qq; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1682771868; kw_token=96D5ZBKRO9W',
        'csrf': '96D5ZBKRO9W',
        'Host': 'www.kuwo.cn',
        'Referer': 'https://www.kuwo.cn/play_detail/83001418',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    response=requests.get(url=url1,headers=headers)
    print(response)
    json_data=response.json()  #字典类型数据  text字符串文本  content二进制数据
    data_list=json_data['data']['list']
    for data in data_list:
        rid=data['rid']
        artist=data['artist']
        name1=data['name']
        name=re.findall('[\w\u4e00-\u9fa5]+',name1)[0]
        print(rid,name,artist)
        info_url=f'https://www.kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=convert_url3&br=320kmp3'
        music_url=requests.get(url=info_url).json()['data']['url']
        music_data=requests.get(music_url).content
        n=random.randint(0,99)
        if os.path.exists(f'F:/music/{key}/{name}.mp3'):
            with open(f'F:/music/{key}/{name}{n}.mp3',mode='wb') as f:
                n+=1
                f.write(music_data)
                print('保存完成')
        else:
            with open(f'F:/music/{key}/{name}.mp3',mode='wb') as f:
                f.write(music_data)
                print('保存完成')