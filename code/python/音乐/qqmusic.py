import requests
import re
import execjs
headers={
    'cookie': '_ntes_nnid=e69bf98be8c89fc35491bb3685fe28f7,1658577712726; _ntes_nuid=e69bf98be8c89fc35491bb3685fe28f7; NMTID=00OfGAny-LkJEPtvUwzjFSEPaCltbwAAAGCKu99fQ; WNMCID=iojlpy.1658577712863.01.0; WEVNSM=1.0.0; WM_TID=MNpSWm2gnxZEARFVEQbAGA3M7K8%2BrGqJ; WM_NIKE=9ca17ae2e6ffcda170e2e6eebbb125a98d84d9cc6887b08eb6d14a868f9b87d86092eeadd7e133e9ab8cd0d02af0fea7c3b92afcb1008ded3ba39dbda3d36283a89790b260b2f0beb9ed79b1b0a885cf67f5b79fd7bb44fcbb9889cc39b7a7a1b1b83bacb18692c5638feefda3bc42939c9eaef666edb7fc9beb6f8788fc8be74da993f88bd23cf3b3af9bdb65a8b8a594c174abf09eb2b633f8eaa385fb7b93afbca6c434fc988ad0f95ae98b9897f954baeb839bea37e2a3; WM_NI=8o0ln1aCsBPjAxYo3Tr0rXnssphdLm7iQ68H8eXhI3uyoP51hoJqFiM23B9JQDRMwn%2Fi4zheEX4jdGkM8jS01mazXodhksBxi0RQ7946mdxqQqtEA88HF%2FzR%2BUXvzXz5Mzk%3D; MUSIC_U=64f36e48b464229a866601ea879de30920ed0d8d990cd39377c70cf0e48073cac84e8a4f4ba4f13ef2b95c14bb5013871f3c441dbd6a64054a13fca2519080389471f70aced29acda0d2166338885bd7; __csrf=e51865d2e8679acad9b964523456285e; __remember_me=true; ntes_kaola_ad=1; JSESSIONID-WYYY=sP6xReM%5CYppOSMw7Cc%5CMMrjqx1%2BVPwIXURde01ptRTw6razxw2InHknkJ8jyq%2BZPrzNM009%5C7P6w5wAYxeZ6jEORn%5Co%2FiNkOpzoXN%5CEUdMmABtp4wC%5ClClJ%5CvE6uUOUtc6u9RCesN%5CAea0c2%2BlGg4l%5C54fV1ebqjA%2F%2BCbclq0bMuT0q%2F%3A1658586479392; _iuqxldmzr_=33nm-gcore-status: 1',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/my/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
f=open('music163.js',mode='r',encoding='utf-8').read()
ctx=execjs.compile(f)
url='https://music.163.com/discover/toplist?id=3779629'
response=requests.get(url)
print(response)
html_data=response.text
info_list=re.findall('',html_data)
print(info_list[0][0])
for info in info_list:
    music_url='https://music.163.com/song/media/outer/url?id='+str(info[0])
    print(music_url,info[1])
    music_data=requests.get(music_url).content
