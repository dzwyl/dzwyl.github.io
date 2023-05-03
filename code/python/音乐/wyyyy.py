import requests
import parsel
import os
import concurrent.futures


def get_response(html_url):
    response = requests.get(url=html_url, headers=headers)
    return response


def get_info(html_url):
    response = get_response(html_url)
    selector = parsel.Selector(response.text)
    lis = selector.css('.chapter__list-box li')
    info_list = []
    for li in list(reversed(lis)):
        chapter_id = li.css('a::attr(data-chapterid)').get()
        chapter_title = li.css('a::text').getall()[-1].strip()
        info_tuple = (chapter_id, chapter_title)
        info_list.append(info_tuple)
    return info_list


def get_img_url(comic_id, chapter_id):
    link = 'https://comic.mkzcdn.com/chapter/content/v1/'
    data = {
        'chapter_id': chapter_id,
        'comic_id': comic_id,
        'format': '1',
        'quality': '1',
        'sign': '3f211d8012cbae79a77164026579b62c',
        'type': '1',
        'uid': '53471616',
    }
    json_data = requests.get(url=link, params=data, headers=headers).json()
    # json_data 字典数据类型, 就可以根据键值对取值
    img_list = json_data['data']['page']
    img_list = [i['image'] for i in img_list]
    return img_list


def save(name, img_url):
    img_content = get_response(img_url).content
    with open(name, mode='wb') as f:
        f.write(img_content)


def get_list_url(html_url):
    html_data = get_response(html_url).text
    selector = parsel.Selector(html_data)
    href = selector.css('.common-comic-item .cover::attr(href)').getall()
    name_id_list = [j.split('/')[1] for j in href]
    name_list = selector.css('.common-comic-item .comic-feature::text').getall()
    list_info = zip(name_id_list, name_list)
    return list_info


def main(home_url):
    list_info = get_list_url(home_url)
    for name_id, name in list_info:
        index_url = f'https://www.mkzhan.com/{name_id}/'
        info_list = get_info(index_url)
        print('正在采集: ', name)
        if not os.path.exists(f'{name}\\'):
            os.mkdir(f'{name}\\')
        for chapter_id, chapter_title in info_list:
            img_list = get_img_url(name_id, chapter_id)
            print(chapter_title)
            page = 1
            for img_url in img_list:
                filename = f'{name}\\{chapter_title}-{page}.jpg'
                save(filename, img_url)
                print(img_url)
                page += 1


if __name__ == '__main__':
    headers = {
        'cookie': '__login_his_sync=0; UM_distinctid=1804ff0bf61af8-097915c0daabb1-6b3e555b-1fa400-1804ff0bf62d60; CNZZDATA1262045698=675826315-1650605442-https%253A%252F%252Fwww.baidu.com%252F%7C1650605442; tourist_expires=1; CNZZDATA1261814609=844855556-1650605900-https%253A%252F%252Fwww.mkzhan.com%252F%7C1650605900; readMode=scroll; redirect_url=%2F212976%2F; cn_1262045698_dplus=%7B%22distinct_id%22%3A%20%221804ff0bf61af8-097915c0daabb1-6b3e555b-1fa400-1804ff0bf62d60%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201650610133%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201650610133%7D',
        'referer': 'https://www.mkzhan.com/category/?is_vip=1&finish=2&page=2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    }
    exe = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    for page in range(1, 6):
        url = f'https://www.mkzhan.com/category/?is_vip=1&finish=2&page={page}'
        exe.submit(main, url)
    exe.shutdown()
