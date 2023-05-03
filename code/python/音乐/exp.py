from urllib import response
import requests
import re
key = '梁静茹' #请输入你要搜索的歌曲或者歌手名
url = f'https://music.163.com/#/search/m/?s={key}&type=1'
headers={
    'cookie': '_ntes_nnid=4efd500a26799b64ce6fb989d686ccd5,1661867232064; _ntes_nuid=4efd500a26799b64ce6fb989d686ccd5; WEVNSM=1.0.0; WNMCID=pbiejd.1661867232260.01.0; WM_TID=ChUTtEgPvj5FAAUFEBKUTPy6QVaHM54T; NMTID=00OphuYj-bKIWAgQUWxuFB2g1rsl-gAAAGC7wGWGA; __snaker__id=Q9uD1jgLSLIRl3Tw; YD00000558929251%3AWM_TID=VCfhMr%2FhJKtAQFEAUEKUCxifoDAmnf%2BO; _9755xjdesxxd_=32; ntes_kaola_ad=1; _ga=GA1.1.1143133197.1665671986; Qs_lvt_382223=1665671986; _clck=1k609u4|1|f5o|0; Qs_pv_382223=2189565176053380000%2C2706358348359543300%2C2178262175050269700; _ga_C6TGHFPQ1H=GS1.1.1665675606.2.1.1665677010.0.0.0; P_INFO=15697881481|1676297057|1|netease_buff|00&99|null&null&null#zhj&330100#10#0|&0||15697881481; WM_NI=0JxKTNGspTT2AMz0bxRQGhrGOFd5kc1m%2FdupJvEt4G7zFA8YfKvQgCxa0esZQpT37pyn%2BU6gLXROXp609wXntvXzD%2BL5GEERGtLLjOniSD25HdthOmRJbfG0L2NM6sKISlg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee88e24197b8ab8cc9708e8e8bb6d55b868b8aadc46be999b9d0b77cb8969b9af52af0fea7c3b92af496b8acd74685adc0b5d73a8393b6d1e174928f8989f14d8d9aacd6ea69f3b3e185f87c8aaa8b95b74df5a68aa2bb53a695bab2e649bcbf0086f25293b09cd4b67cbbb2e5b6b56d90889eb0db7cf6f0f798db66b8aa989bc72190eb89a6c85a85ac84ade945aeb79da5b13f8cbcbc89ce679296ae87c63c90ee82aeb57989979d8de637e2a3; YD00000558929251%3AWM_NI=rYGpinAoQUBa%2FnB%2FVG2GEk%2B9NhkfFg%2BVgRFeL1J8Y0m1Te43snIhWEJBFTD7lb9wqK5A1LkKHHxdspa15WN0LvgRPpv11QFl%2B5L9HVwtkdgdNiQckPWZrXkxRiamziH0eU0%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee88b752f3a9fa96e45fbc928ba6d85b868a9aacc848b689b9d0f37cf7b6bed5b22af0fea7c3b92ab2878991ec6683b19fb6c16bedb28ed0d54df2998b8caa338eb8a587c56de98aa9b3c56f90ef86d9dc3cafef9c86b739b1b28789d64f8a9e8ab5c73db0bef798f441f79fffadea418c98b885f27ca3effbb8cd3c90aaa9b3d37cb6efffb2c568e9eb84dacb5eb5aca585e6708eb79f84ea5c9586beb9ea7492b7af8ef9638cf0abb6b337e2a3; JSESSIONID-WYYY=aIPFkDkTB42MahtVdg0lld17SiZ0NiZ7x5H7kkevp%2FH5mtFfFAWphKlAY4rSHwsg1UWsKKmT%5CBOvJnWwyWcAEklc8kDfvYc0TBidEjhc4FWKOfCrs2WqV%2BURAWWqUHUhvcFsDJ0bH1hIiu0h7cAmr9dpsN7hesn5yzB042XAYMhuOuiV%3A1682827802738; _iuqxldmzr_=33; gdxidpyhxdE=1fgHg%2BzvaK78lz49swUC%2BmSTJokOMXj2rqG4urhqQcadTVU4%5C%2FTLpwuk%2FXabAkNDYmtgJxznn16egh52GmGK2gvAIRPvay8NeVtI2WoV9lMcqRdVqT87R%2FIfeS3MzUoPBt68JS2BQIsoUUNnx7n3pIcaTg63vgN%5C9s8HlZP78d89NS9d%3A1682826925896; MUSIC_U=64f36e48b464229a866601ea879de3094e8a66bd4fd7f62d3af526c739df987fc84e8a4f4ba4f13ef347b3237e3023e4292ecf92ef11667b4a13fca2519080389471f70aced29acda0d2166338885bd7; __csrf=a528be19c2023a64cc8b739960fe6610; __remember_me=true; playerid=28611251',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'referer': 'https://music.163.com/search/'
}
response=requests.post(url=url,headers=headers)
#print(response.text) #搜索audio所在包
html_data=response.text
info_list=re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>',html_data) #匹配？加\
print(info_list)
url1 ='https://m704.music.126.net/20230430125824/189a8d5afac90d6957cfef0cf6d76c83/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14096608092/84a1/c30f/6f80/6218e741b4c4929a0807239478665a21.m4a?authSecret=00000187d06fdc131ea30aaba51e2b30'
response1=requests.post(url=url1,headers=headers)
print(response1.text)