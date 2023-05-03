import requests
import re
from tqdm import tqdm
from pprint import pprint
headers = {
    'cookie': 'QC005=4373300b624fb2713eb2769da1fc1302; QC006=e9f422b801e51ffc7588d431c530ed85; QP0030=1; T00404=bf7b376b27d114a2cb4cd4ca219ab751; TQC030=1; QC173=0; QP0034=%7B%22v%22%3A1%2C%22dm%22%3A%7B%22wv%22%3A1%7D%2C%22m%22%3A%7B%22wm-vp9%22%3A1%2C%22wm-av1%22%3A1%7D%7D; P00004=.1659758426.a566958a8a; P111114=1659758432; QY_PUSHMSG_ID=4373300b624fb2713eb2769da1fc1302; T00700=EgcI9L-tIRABEgcI58DtIRABEgcI67-tIRAEEgcIq8HtIRABEgcIrcHtIRABEgcI8L-tIRABEgcIz7-tIRAB; QP008=60; QYABEX={"mergedAbtest":"1707_B,1550_B,4580_B","PCW-Home-List":{"value":"1","abtest":"1707_B"},"pcw_home_hover":{"value":"1","abtest":"1550_B"},"PCW_1_qyhome_recommend_sources":{"value":"1","abtest":"4580_B"}}; P00001=1aOm24GwOEhgE7uBndsprMRuHAwZjo7ki75tdrhV7vBWsGRm1bSauY5OwWYJ74dm1VyGCd2; P00007=1aOm24GwOEhgE7uBndsprMRuHAwZjo7ki75tdrhV7vBWsGRm1bSauY5OwWYJ74dm1VyGCd2; P00003=3072029217643904; P00002=%7B%22uid%22%3A3072029217643904%2C%22pru%22%3A3072029217643904%2C%22user_name%22%3A%22156****1481%22%2C%22nickname%22%3A%22%5Cu4e95%5Cu5ddd%5Cu6587%5Cu5c7f%22%2C%22pnickname%22%3A%22%5Cu4e95%5Cu5ddd%5Cu6587%5Cu5c7f%22%2C%22type%22%3A11%2C%22email%22%3A%22%22%7D; P00010=3072029217643904; P01010=1659888000; P00PRU=3072029217643904; QC160=%7B%22type%22%3A2%2C%22conformLoginType%22%3A0%7D; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A1659869125826%7D; QC170=1; QC179=%7B%22vipTypes%22%3A%221%22%2C%22userIcon%22%3A%22%2F%2Fimg7.iqiyipic.com%2Fpassport%2F20220807%2Fd7%2F94%2Fpassport_3072029217643904_165985829719798_130_130.png%22%2C%22iconPendant%22%3A%22%22%2C%22uid%22%3A3072029217643904%2C%22bannedVip%22%3Afalse%2C%22allVip%22%3Atrue%7D; QC163=1; QP0013=1; QP0037=0; QP0033=1; QP0025=1; QP0035=5; QC008=1659758381.1659869102.1659884437.3; nu=0; QP0027=7; QC159=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A1%2C%22hideRoleTip%22%3A1%2C%22isOpen%22%3A1%2C%22speed%22%3A10%2C%22density%22%3A40%2C%22opacity%22%3A86%2C%22isFilterColorFont%22%3A1%2C%22isOpenMask%22%3A0%2C%22proofShield%22%3A0%2C%22forcedFontSize%22%3A24%2C%22isFilterImage%22%3A1%2C%22defaultSwitch%22%3A0%2C%22hadTip%22%3A1%7D; __dfp=a001dc8d2afd7548a6bcd24887365e845e19ff7c545320273620df4c9f86730948@1661054380931@1659758381931; QY00001=3072029217643904; QP0036=202287%7C15.538; QC007=https%25252525253A%25252525252F%25252525252Fcn.bing.com%25252525252F; QC010=233522714; IMS=IggQABj_wr-XBiorCiA2ZmE3NTE5NjE1MzMzNGMyYjc3NTdmNzhiOTg4OTA0YxAAIgAotAEwBTAAMAAwADAAciQKIDZmYTc1MTk2MTUzMzM0YzJiNzc1N2Y3OGI5ODg5MDRjEACCAQCKASQKIgogNmZhNzUxOTYxNTMzMzRjMmI3NzU3Zjc4Yjk4ODkwNGM',
    'origin': 'https://www.iqiyi.com',
    'referer': 'https://www.iqiyi.com/v_zxdr0bdmto.html?vfrm=pcw_home&vfrmblk=712211_cainizaizhui&vfrmrst=712211_cainizaizhui_image1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}
url = 'https://cache.video.iqiyi.com/dash?tvid=3522811592304800&bid=600&vid=3918f0f6807671b7ba95b9c98d5ebf58&src=01010031010000000000&vt=0&rs=1&uid=3072029217643904&ori=pcw&ps=1&k_uid=4373300b624fb2713eb2769da1fc1302&pt=0&d=0&s=&lid=&cf=&ct=&authKey=43adb6bf0f5c278e92a48a8d59050fe3&k_tag=1&dfp=a001dc8d2afd7548a6bcd24887365e845e19ff7c545320273620df4c9f86730948&locale=zh_cn&prio=%7B%22ff%22%3A%22f4v%22%2C%22code%22%3A2%7D&pck=1aOm24GwOEhgE7uBndsprMRuHAwZjo7ki75tdrhV7vBWsGRm1bSauY5OwWYJ74dm1VyGCd2&k_err_retries=0&up=&qd_v=2&tm=1659884454306&qdy=a&qds=0&k_ft1=706436220846084&k_ft4=1161084347621380&k_ft5=262145&bop=%7B%22version%22%3A%2210.0%22%2C%22dfp%22%3A%22a001dc8d2afd7548a6bcd24887365e845e19ff7c545320273620df4c9f86730948%22%7D&ut=1&vf=d9e95cdfe73b44bfdbeba9d6e80d9127'
response = requests.get(url=url, headers=headers)
#print(response)
json_data = response.json()
#pprint(json_data)
m3u8 = json_data['data']['program']['video'][0]['m3u8']  #在dash里
ts_list = re.sub('#E.*', '', m3u8)
ts_list = ts_list.split()
for ts in tqdm(ts_list):
    ts_data = requests.get(ts).content
    with open('天才基本法第5集.mp4', mode='ab') as f:
        f.write(ts_data)