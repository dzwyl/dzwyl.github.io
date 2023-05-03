import requests
from pprint import pprint
import json
import prettytable as pt
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-10-30&leftTicketDTO.from_station=HGH&leftTicketDTO.to_station=YKG&purpose_codes=ADULT'
headers={
    'Cookie': '_uab_collina=166610700851802091293417; JSESSIONID=63A9C34A6F02D9A79906F7D5BCB83402; BIGipServerotn=1274020362.38945.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1666449915018; RAIL_DEVICEID=iZsuVtAI2vog2BbWbR7Lnf6-vcjDY1xxWNj-I1TRmHa7VMb0VUL0A3fmThsHpiVL-CU_lq4XrJORkV9a9TAuf6T5Ll6843b-GnsJvNSJt6nk0yyoocAd7xXE87vzFENn27vH2RJx9DdoSEAbWarZL5L3r_jsqgHn; BIGipServerpool_passport=199492106.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u676D%u5DDE%u4E1C%2CHGH; _jc_save_toStation=%u9E70%u6F6D%u5317%2CYKG; _jc_save_fromDate=2022-10-19; _jc_save_toDate=2022-10-18; _jc_save_wfdc_flag=dc',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
response=requests.get(url=url,headers=headers)
jsondata=response.json()
#print(jsondata)
ticket=jsondata['data']['result']
tb=pt.PrettyTable()
tb.field_names=[
    '序号',
    '车次',
    '出发时间',
    '到达时间',
    '耗时',
    '特等座',
    '一等座',
    '二等座',
    '软卧',
    '硬卧',
    '硬座',
    '无座',
]
page=0
for i in ticket:
    index=i.split('|')
    num=index[3]  #车次
    starttime=index[8]  #出发时间
    endtime=index[9]
    usetime=index[10]
    topclass=index[32]
    firstclass=index[31]
    secondclass=index[30]
    softsleep=index[28]
    hardsleep=index[29]
    hardseat=index[26]
    noseat=index[23]

    dit={
        '序号':page,
        '车次':num,
        '出发时间':starttime,
        '到达时间':endtime,
        '耗时':usetime,
        '特等座':topclass,
        '一等座':firstclass,
        '二等座':secondclass,
        '软卧':softsleep,
        '硬卧':hardsleep,
        '硬座':hardseat,
        '无座':noseat,
    }
    tb.add_row([page,
                num,
                starttime,
                endtime,
                usetime,
                topclass,
                firstclass,
                secondclass,
                softsleep,
                hardsleep,
                hardseat,
                noseat,
                ])
    page+=1
print(tb)