import requests
import execjs

class Music163():

    def __init__(self):
        self.headers = {
            'cookie': '_ntes_nnid=3c313a7a2316c853c478bc79c43ac9b4,1657627730924; _ntes_nuid=3c313a7a2316c853c478bc79c43ac9b4; NMTID=00O5EDQsYoqTMauUUAgtV6D0BbIHnwAAAGB8k_l6w; WNMCID=qtrwkx.1657627731340.01.0; WEVNSM=1.0.0; WM_TID=tVflU2Uo3xBABQVVVEaBV74cMf%2F91et0; _iuqxldmzr_=32; __csrf=ff859472a8473546581241624d33c4a7; MUSIC_U=ef63db2826f2c58d750719abd63a4be1e2ca9e577d1b503998bc2e21c7523572993166e004087dd39b7cd34a94d0c20cac95c5692e7cb97d290a29e290f6160e94359c2a70715816a0d2166338885bd7; __remember_me=true; ntes_kaola_ad=1; vinfo_n_f_l_n3=4601f89712fd3223.1.0.1658555827103.0.1658555915573; WM_NIKE=9ca17ae2e6ffcda170e2e6ee86fc69bba8a0b1b24683928ea3c15f879b8e83d54483b286ccd533b18b8982dc2af0fea7c3b92a869e8c84c5428cba99b6bc6da6bc969bf060b6a9fe8eee79f4e7a185f439a29faa8cfb5e878de1d3cc3ef38d81acf97291a6afa3cf538592a3d2cd809b9097a6e667a299a9b1e85afc9fadd6cc6b8bbc8bd3ca5cf487fc91b260948c8cabf272a592febbe16182969f8fea3fb390bfd0f17f93abfebac97cbc9a9989d13cb1a782b9ee37e2a3; WM_NI=FBDcFJHfWU9gfdZzmTvw2mos09odq3bAfkxVES%2F2I61SOKzzSzaBLYGNm1NtYPYEgmbGgPeR8Ac5IaIdE2KP0Y4p3TPTDJszgN2ZbkBJQnk5qPq%2FruQu2YJpxFWhR0syNXo%3D; JSESSIONID-WYYY=NKDtwKyHWm5hiB5eWjIf%2BgW0gMsDjPOIccIy4oKnomyiVQzu7mjhDxFdhbf7OQptOYPjqhpH%2Fb56b0UJdCQoUSyzCiOzker57UqNa3oPBYxsvBg4a%5COwm%5C6lieKTJysM%2BczScTGIKF1ygRppPZB8CbyxNabiRxTZbVBQenA%5ClqFIrpm0%3A1658582200774',
            'origin': 'https://music.163.com',
            'referer': 'https://music.163.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }
        self.ctx = execjs.compile(open('网易云音乐/demo.js', mode='r', encoding='utf-8').read())

    def getMusic(self, id):
        """
        获取音乐链接
        :param id: 音乐id
        :return: 音乐接口
        """
        url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=ff859472a8473546581241624d33c4a7'
        result = self.ctx.call('music', id)
        data = {
            'params': result['encText'],
            'encSecKey': result['encSecKey']
        }
        music_url = requests.post(url=url, data=data, headers=self.headers).json()['data'][0]['url']
        return music_url

    def searchMusic(self, songName):
        """
        搜索功能
        :param songName: 歌曲名称
        :return: 歌曲信息
        """
        url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token=ff859472a8473546581241624d33c4a7'
        result = self.ctx.call('search', songName)
        data = {
            'params': result['encText'],
            'encSecKey': result['encSecKey']
        }
        json_data = requests.post(url=url, data=data, headers=self.headers).json()
        songs = json_data['result']['songs']
        song_list = []
        for song in songs:
            name = song['name']
            id = song['privilege']['id']
            song_list.append([id, name])
        return song_list

    def getComment(self, id, pageNo):
        """
        获取评论
        :param id: 歌曲id
        :param pageNo: 页码
        :return: 评论列表
        """
        url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=ff859472a8473546581241624d33c4a7'
        result = self.ctx.call('comment', id, pageNo)
        data = {
            'params': result['encText'],
            'encSecKey': result['encSecKey']
        }
        json_data = requests.post(url=url, data=data, headers=self.headers).json()
        comments = json_data['data']['comments']
        commentList = []
        for comment in comments:
            content = comment['content']
            commentList.append(content)
        return commentList


    def getLyrics(self, id):
        """
        获取歌词
        :param id: 歌曲id
        :return: 歌词文本
        """
        url = 'https://music.163.com/weapi/song/lyric?csrf_token=ff859472a8473546581241624d33c4a7'
        result = self.ctx.call('lyrics', id)
        data = {
            'params': result['encText'],
            'encSecKey': result['encSecKey']
        }
        json_data = requests.post(url=url, data=data, headers=self.headers).json()
        lyric = json_data['lrc']['lyric']
        return lyric

    def getMv(self, mvId):
        """
        获取mv
        :param mvId
        :return: mv链接
        """
        url = 'https://music.163.com/weapi/song/enhance/play/mv/url?csrf_token=ff859472a8473546581241624d33c4a7'
        result = self.ctx.call('mv_info', mvId)
        data = {
            'params': result['encText'],
            'encSecKey': result['encSecKey']
        }
        json_data = requests.post(url=url, data=data, headers=self.headers).json()
        mvUrl = json_data['data']['url']
        return mvUrl

if __name__ == '__main__':
    music = Music163()
    info_list = music.searchMusic("林俊杰")
    for info in info_list:
        print(music.getMusic(info[0]))
        # print(music.getComment(info[0], '1'))
        print(music.getLyrics(info[0]))
    #print(music.getMv('372296'))