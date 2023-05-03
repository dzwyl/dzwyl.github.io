import requests
from pprint import pprint
import json
#查票
#start_data=input('请输入出发时间：')
#start_city=input('请输入出发城市：')
#end_city=input('请输入到达城市：')
start_data='2022-9-21'
start_city='杭州'
end_city='鹰潭'
f=open('J:/py/py-spider/city.json',encoding='utf-8')
city_json=json.loads(f.read())
print(city_json)
fromstation=city_json[start_city]
tostation=city_json[end_city]
print(fromstation,tostation)
#保存数据
url=f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={start_data}&leftTicketDTO.from_station={fromstation}&leftTicketDTO.to_station={tostation}&purpose_codes=ADULT'
headers={
    'Host': 'kyfw.12306.cn',
    'Cookie': '_uab_collina=165978923031249592631788; JSESSIONID=C533C0C7C9A8408DE411E15058EF4EFA; tk=n1pJzJ7sJ3XRmY41A4jb6P5t4_XANwWa_rdQIoaZ5ok1uBbS36d1d0; BIGipServerotn=1190134282.64545.0000; BIGipServerpool_passport=165937674.50215.0000; RAIL_EXPIRATION=1660074361915; RAIL_DEVICEID=FraPayr7trYZOGe3IoV86KOLJBrR5hd_1iEnCpSxulsbA2XhMHac5uS4XJm4wDki1vDu-spRXH5G_Ah7bQDu3722-ObMvVspZws04pG4WUIk2I6Aprn5hygi3wJfjDJQO0n5V4qALEYmzap8GPVW6Fko1twFG5sq; highContrastMode=defaltMode; guidesStatus=off; cursorStatus=off; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u676D%u5DDE%2CHZH; _jc_save_toStation=%u516D%u76D8%u6C34%2CUMW; _jc_save_toDate=2022-08-06; _jc_save_wfdc_flag=dc; current_captcha_type=Z; uKey=2ff8deec9607d88a2020b2b7240eba7c5e289d9ddd3ea11da4192ccfe4388247; _jc_save_fromDate=2022-08-10',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response=requests.get(url=url,headers=headers)
json_data=response.json()
#pprint(json_data)
train=json_data['data']['result']
print(train)
print(str(train).split("|"))
trainstr=str(train).split("|")
num=0
for str in trainstr:
    print(str,'|',num)
    num+=1
print{
    '车次':train[3],
    '出发站':train[6],
    '到达站':train[7],
    '出发时间':train[8],
    '到达时间':train[9],
    '历时':train[10],
    '商务座':train[32],
    '一等座':train[31],
    '二等座':train[30],
    '软卧':train[23],
    '硬卧':train[],
    '软座':train[],
    '硬座':train[],
    '无座':train[],
}