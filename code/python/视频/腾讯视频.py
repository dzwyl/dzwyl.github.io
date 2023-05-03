import requests
import re
import json
from tqdm import tqdm
from pprint import pprint
url='https://vd6.l.qq.com/proxyhttp'  #m3u8链接在proxyhttp里 cookie要登录账户 cookie和data实时更新容易失效
headers={
    'Cookie': 'RK=+ZmYwdhVZr; ptcz=044852e5b6be4aeda0697f7d84ef6d3f2b243d7f10f747b128e1be9b5178c16e; tvfe_boss_uuid=6736326a108ceeea; pgv_info=ssid=s4407792509; pgv_pvid=9372540680; lv_play_index=40; appuser=AC93A950CE53ABCB; vversion_name=8.2.95; video_omgid=26458cd742c1bfe4; o_minduid=EReYV9UEezG4zlMi9WYxPppqYWRfQlzT; Lturn=705; LKBturn=776; LPVLturn=290; LPLFturn=291; cm_cookie=V1,110064&__M-MZID__&AQEBvxLO_ZNSykPu0szaKBi47wvxjkZaTso0&220728&220728; _qpsvr_localtk=0.9474048797086028; LPPBturn=325; LZTturn=752; ufc=r24_2_1659100097_1659015979; LPSJturn=619; LVINturn=112; LPHLSturn=109; LDERturn=554',
    'Host': 'vd6.l.qq.com',
    'Origin': 'https://v.qq.com',
    'Referer': 'https://v.qq.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}  #data在payload的view source里
data='{"buid":"vinfoad","vinfoparam":"charge=0&otype=ojson&defnpayver=1&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200adi5d10%2Fi0043mc7rqh.html&sphttps=1&encryptVer=8.1&cKey=729DDA83EB728744578A3C6E8D4CDF48BC4D1BF949FC959C504D45374B0FB960796201E12AB2353061ED7A24D04C2D30B15B719550D3883A8577680C291779643EE24FE664A41F714B8A14FDD9BAA53CE0BCBCC1F154EC3CE25988B393CBF8E9B1F85F26D1BB979D2CF2DB55C2F683606CB8BE827EB6A5BA00E9C8F96F35D7F98D7496E1DFCEDEE8D018337DAF627B583F8AC4D1071369F069513E58B6A41199E81ADA6782A2582F1D38D12C85C0917C41910F19EFA6C686154555B8776F33F87792B285E11024F089A238982541A084E5A0B246A8498CB639D452DCA7232F3BC0676E65178F004DEFDABAB06B29CB9A3A5935A4411FEC7992EC8F81C1AB9A67&clip=4&guid=26458cd742c1bfe4&flowid=46e72b673cbe991ac11b985aec18fb85&platform=10201&sdtfrom=v1010&appVer=3.5.57&unid=&auth_from=&auth_ext=&vid=i0043mc7rqh&defn=&fhdswitch=0&dtype=3&spsrt=2&tm=1659017980&lang_code=0&logintoken=%7B%22access_token%22%3A%22FB09FF15796F7AE210702A045917567F%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22cCaeIkHLce6pTz2meV7jFg.N%22%2C%22openid%22%3A%223EC25BC2C9B821D03989502AF0C3FB5F%22%2C%22vuserid%22%3A%22621705977%22%2C%22video_guid%22%3A%2226458cd742c1bfe4%22%2C%22main_login%22%3A%22qq%22%7D&spvvpay=1&spadseg=3&hevclv=16&spsfrhdr=0&spvideo=0&drm=40","adparam":"pf=in&pf_ex=pc&pu=1&pt=0&platform=10201&from=0&flowid=46e72b673cbe991ac11b985aec18fb85&guid=26458cd742c1bfe4&coverid=mzc00200adi5d10&vid=i0043mc7rqh&chid=0&tpid=1&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200adi5d10%2Fi0043mc7rqh.html&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200adi5d10%2Fi0043mc7rqh.html&lt=qq&opid=3EC25BC2C9B821D03989502AF0C3FB5F&atkn=FB09FF15796F7AE210702A045917567F&appid=101483052&uid=621705977&tkn=cCaeIkHLce6pTz2meV7jFg.N&rfid=7d0674173a0eb3ea9c69ea79cf7b9278_1659017964&v=1.4.119&vptag=cn_bing_com%7Cx&ad_type=LD%7CKB%7CPVL&live=0&appversion=1.5.4&ty=web&adaptor=1&dtype=1&resp_type=json"}'
response=requests.post(url=url,headers=headers,data=data)
jsondata=response.json()
#去除引号
vinfo=json.loads(jsondata['vinfo'])
pprint(vinfo)
m3u8=vinfo['vl']['vi'][0]['ul']['m3u8']
m3u8=re.sub('#E.*','',m3u8)
ts_list=m3u8.split()
#print(ts_list)
for ts in tqdm(ts_list):
    ts_url = 'https://apd-57c5d150c8b9788baf40ea4f65feddf8.v.smtcdns.com/moviets.tc.qq.com/A2k4JuW9ATia8thdFQ6y5HWRUGLqAr4L5fk9KFbAUEI8/uwMROfz2r5xgoaQXGdGnC2df64gVTKzl5C_X6A3JOVT0QIb-/doVi4hWq0sqexPo_ylKYxVIJdr9zz2VweWbcY7x70kRnbVNPvBaoTsjwfOq1uojOtsRKJ8r3372HRaTOVg4VyKOFFvzjq2EeMdpleIIyTv0tb-C3CzXmkZz-34hK4Fc-r4mZK55L9W1RqJMpsvrORZr_sqpqvGZrrRq830get0NLJGkeAQ9SBg/' + ts
    video_content=requests.get(url=ts_url,headers=headers).content  #获取二进制数据内容
    with open('视频/video/'+'橘生淮南.mp4',mode='ab') as f:
        f.write(video_content)
print('保存完成')        