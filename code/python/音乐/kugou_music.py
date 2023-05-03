"""
[模块的使用]:
    requests >>> pip install requests 数据请求
    re

win + R 输入cmd 输入安装命令 pip install 模块名
-----------------------------------------
模块安装问题:
    - 如果安装python第三方模块:
        1. win + R 输入 cmd 点击确定, 输入安装命令 pip install 模块名 (pip install requests) 回车
        2. 在pycharm中点击Terminal(终端) 输入安装命令
    - 安装失败原因:
        - 失败一: pip 不是内部命令
            解决方法: 设置环境变量

        - 失败二: 出现大量报红 (read time out)
            解决方法: 因为是网络链接超时,  需要切换镜像源
                清华：https://pypi.tuna.tsinghua.edu.cn/simple
                阿里云：https://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：https://pypi.hustunique.com/
                山东理工大学：https://pypi.sdutlinux.org/
                豆瓣：https://pypi.douban.com/simple/
                例如：pip3 install -i https://pypi.doubanio.com/simple/ 模块名

爬虫案例: 固定思路流程

一. 数据来源分析 (由一个数据 一首歌分析 然后找寻全部歌曲规律)
    1. 确定一下自己需求是什么?
    2. 通过开发者工具进行抓包分析...
        I. 分析音频播放地址 音乐url地址 (如果你想要的数据是音频或者视频 可以选择media)
        II.  分析音频url地址 可以从哪个数据包里面得到 一首歌曲数据包
            通过两个歌曲的数据包对比分析 hash id
从一首歌曲 找 数据包 找 请求参数内容

二. 代码实现步骤
    1. 发送请求, 对于榜单url地址发送请求
    2. 获取数据, 获取服务器返回的数据内容
    3. 解析数据, 提取我们想要 音乐 hash id 这两个参数

    4. 发送请求, 对于音乐数据包发送请求
    5. 获取数据, 获取服务器返回的数据内容
    6. 解析数据, 提取我们想要音乐标题 以及 音频播放地址

    7. 保存数据
"""
# 导入数据请求模块
import requests
# 导入正则
import re
# 导入格式化输出模块
import pprint


home_url = 'https://www.kugou.com/yy/html/rank.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
response = requests.get(url=home_url, headers=headers)
# print(response.text)
urls = re.findall('<a title="(.*?)"  hidefocus="true" href="(.*?)"', response.text)
for title, list_url in urls[11:]:
    print(title, list_url)
    """
    1. 发送请求, 对于榜单url地址发送请求
        Python模拟浏览器去对于url地址发送请求
        user-agent: 用户代理的意思 表示浏览器基本身份信息
        
    """
    # url = 'https://www.kugou.com/yy/html/rank.html'
    # 通过requests里面get请求方法对于url地址发送请求, 并且携带上headers请求参数伪装, 最后用response接收返回数据
    response = requests.get(url=list_url, headers=headers)
    # <Response [200]> 返回response响应的对象  200 表示请求成功
    # 2. 获取数据, 获取服务器返回的数据内容(文本数据内容)
    # print(response.text)
    """
    3. 解析数据, 提取我们想要 音乐 hash id 这两个参数
        正则表达式 re 可以直接对于字符串数据进行提取
        .*? 通配符 可以匹配任意字符(除了\n换行符)
    """
    hash_list = re.findall('"Hash":"(.*?)"', response.text)
    album_id_list = re.findall('"album_id":(.*?),', response.text)
    zip_data = zip(hash_list, album_id_list)  # zip() 函数打包一下
    for Hash, album_id in zip_data:
        # print(Hash, album_id)
        # 4. 发送请求, 对于音乐数据包发送请求
        index_url = 'https://wwwapi.kugou.com/yy/index.php'
        # 如果请求url过长, 可以分开写, url问号前面可以用变量接收, 问号属于请求参数 构建成字典
        # 等号左边都是自定义变量, 你想要data也可以 想params也可以
        params = {
            'r': 'play/getdata',
            'hash': Hash,
            'dfid': '0jJ7pp4NRPlq14bXWB1qUaKJ',
            'appid': '1014',
            'mid': 'efed59987aff73607736bb734a1a732e',
            'platid': '4',
            'album_id': album_id,
            '_': '1649333625329',
        }
        response_1 = requests.get(url=index_url, params=params, headers=headers)
        # print(response_1.json())
        # 5. 获取数据 字典数据 字典取值 键值对取值 根据冒号左边的键, 提取冒号右边的值
        # pprint.pprint(response_1.json())
        # 6. 解析数据
        audio_name = response_1.json()['data']['audio_name']  # 歌曲名字
        play_url = response_1.json()['data']['play_url']
        if play_url: # 判断是否有
            print(audio_name, play_url)
            # 7. 保存数据
            audio_name = re.sub(r'[/\:"?<>|*]', '', audio_name)
            music_content = requests.get(url=play_url, headers=headers).content  # 获取音乐二进制数据内容
            with open('music\\' + audio_name + '.mp3', mode='wb') as f:
                f.write(music_content)

