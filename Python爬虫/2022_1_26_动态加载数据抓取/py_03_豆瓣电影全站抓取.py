import csv

import requests
import random
import time
from bs4 import BeautifulSoup
import os


class DouBanMovie:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'bid=Vz8T-TK2F2k; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1643281009%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DwNmKjm7l-G5XD5EXi3kIEI7qaQvyICNJUJwzSBFJchn0CD0NJYGUIe_CnTj0ryIR%26wd%3D%26eqid%3Da132c494000c85040000000361f27a73%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.481721897.1643281009.1643281009.1643281009.1; __utmb=30149280.0.10.1643281009; __utmc=30149280; __utmz=30149280.1643281009.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.420692598.1643281009.1643281009.1643281009.1; __utmb=223695111.0.10.1643281009; __utmc=223695111; __utmz=223695111.1643281009.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=919064da54d5225f.1643281009.1.1643281119.1643281009.',
            'Host': 'movie.douban.com',
            'Referer': 'https://www.baidu.com/link?url=wNmKjm7l-G5XD5EXi3kIEI7qaQvyICNJUJwzSBFJchn0CD0NJYGUIe_CnTj0ryIR&wd=&eqid=a132c494000c85040000000361f27a73',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36',
        }
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'

    def get_type(self):
        url_type = 'https://movie.douban.com/chart'
        res = requests.get(url=url_type, headers=self.headers)
        # print(res.text)
        # bs4解析获取电影类型
        data = BeautifulSoup(res.text, 'lxml')
        types = data.find('div', class_='types').find_all('a')
        types_list = []
        for i in types:
            # print(i['href'].split('='))
            # print(i['href'].split('=')[1].split('&')[0], i['href'].split('=')[2].split('&')[0])
            types_list.append(
                {i['href'].split('=')[1].split('&')[0]: i['href'].split('=')[2].split('&')[0]})
        # print(types_list)
        return types_list

    def get_html(self, url):
        res = requests.get(url=url, headers=self.headers)
        return res

    def parse(self, res):
        dict_json = res.json()
        movie_list = []
        for data in dict_json:
            print((data['title'], data['types'], data['regions'], data['release_date'], data['score'], data['actors'],
                   data['actor_count']), data['url'])
            types = data['types']
            type = ''
            for type_movie in types:
                if type_movie != types[len(types) - 1]:
                    type += type_movie + '/'
                else:
                    type += type_movie
            regions = data['regions']
            region = ''
            for region_movie in regions:
                if region_movie != regions[len(regions) - 1]:
                    region += region_movie + '/'
                else:
                    region += region_movie
            actors = data['actors']
            actor = ''
            for actor_movie in actors:
                if actor_movie != actors[len(actors) - 1]:
                    actor += actor_movie + '/'
                else:
                    actor += actor_movie
            print((data['title'], type, region, data['release_date'], data['score'], actor,
                   data['actor_count'], data['url']))
            movie_list.append(
                (data['title'], type, region, data['release_date'], data['score'], actor,
                 data['actor_count'], data['url']))
        return movie_list

    def get_count(self, type):
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type)
        res = requests.get(url=url, headers=self.headers)
        print(res.json())
        count = res.json()['total']
        print(count)
        if count % 20 != 0:
            count = int(count / 20) + 1
        else:
            count = int(count / 20)
        return count

    def run(self):
        try:
            os.mkdir('./豆瓣电影信息')
        except:
            print('文件夹已存在！！')
        movie_list = [('title', 'types', 'regions', 'release_date', 'score', 'actors', 'actor_count', 'url')]
        list_type = self.get_type()
        print('电影类型有:', tuple(list_type))
        kw = input('请输入您要查询的电影类型:')
        for type_movie in list_type:
            for key in type_movie.keys():
                if kw == key:
                    with open('./豆瓣电影信息/{}.csv'.format(kw), 'w', encoding='utf-8', newline='') as file:
                        write = csv.writer(file)
                        count = self.get_count(type_movie[kw])
                        for i in range(count):
                            url = self.url.format(type_movie[kw], i * 20)
                            res = self.get_html(url)
                            movie_list.extend(self.parse(res))
                            write.writerows(movie_list)
                            movie_list.clear()
                            time.sleep(random.randint(1, 2))
                    return
        else:
            print('您输入的电影类型不存在！！')


if __name__ == '__main__':
    spider = DouBanMovie()
    spider.run()
