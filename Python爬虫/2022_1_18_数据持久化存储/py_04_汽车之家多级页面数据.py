"""
    爬取汽车之家二手车信息:
        1. 一级页面获取车辆详情链接
"""
import random
import time

import pymongo, re, requests


class CarFamily:
    def __init__(self):
        """定义必要参数"""
        self.list_dict = []
        self.path = "https://www.che168.com"
        self.url = self.path + '/beijing/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179#currengpostion'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400"
        }

    def get_html(self, url):
        """页面数据爬取"""
        res = requests.get(url, headers=self.headers)
        return res.text

    def link_parse(self, html):
        """解析提取二级页面链接"""
        regex = '<li class="cards-li list-photo-li.*?<a href="(.*?)" class="carinfo"'
        pattern = re.compile(regex, re.S)
        link_list = []
        for link in pattern.findall(html):
            link = self.path + link
            link_list.append(link)
        return link_list

    def parse_data(self, html):
        """解析提取二级页面汽车详情信息"""
        regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<p>表显里程.*?<h4>(.*?)</h4>.*?<p>上牌时间</p>.*?<h4>(.*?)</h4>.*?<p>挡位 / 排量</p>.*?<h4>(.*?)</h4>.*?<p>车辆所在地</p>.*?<h4>(.*?)</h4>.*?<div class="brand-price-item">.*?id="overlayPrice">(.*?)<b>万</b><i class="usedfont used-xiajiantou"></i>'
        pattern = re.compile(regex, re.S)
        data_list = pattern.findall(html)
        print(data_list)
        data_dict = {
            'name': data_list[0][0].strip(),
            'mileage': data_list[0][1].strip(),
            'time': data_list[0][2].strip(),
            'gears': data_list[0][3].strip(),
            'location': data_list[0][4].strip(),
            'price': data_list[0][5].strip() + '万'
        }
        return data_dict

    def save_mongo(self, list):
        """存储数据"""
        # 创建数据库链接对象
        conn = pymongo.MongoClient('localhost', 27017)
        # 创建库对象
        db = conn['CayFamily']
        # 创建集合对象
        myset = db['CarData']
        # 集合写入数据
        myset.insert_one(list)

    def run(self):
        """程序入口函数"""
        for i in range(3):
            url = self.url.format(i + 1)
            # 获取一级页面数据
            html = self.get_html(url)
            # 解析提取二级页面链接
            link_list = self.link_parse(html)
            for link in link_list:
                print(link)
                # 获取二级页面数据
                html_second = self.get_html(link)
                # print(html_second)
                # 解析二级页面数据获取汽车信息
                try:
                    data_dict = self.parse_data(html_second)
                    print(data_dict)
                    self.list_dict.append(data_dict)
                    # 数据写入MongoDB数据库
                    self.save_mongo(data_dict)
                except:
                    print(link + '页面信息抓取失败！！')
                time.sleep(3)



if __name__ == '__main__':
    spider = CarFamily()
    spider.run()
