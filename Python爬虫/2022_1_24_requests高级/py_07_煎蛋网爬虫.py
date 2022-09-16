import random

import requests
import os
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class SpiderJianDan:

    def __init__(self):
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36',
            'User-Agent': str(UserAgent().random)
        }

    def get_html(self, url):
        """请求浏览器函数"""
        res = requests.get(url=url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'lxml')
        return soup

    def get_next_page(self, soup):
        """获取下一页页面url"""
        # 获取下一页控件标签
        next_page_tag = soup.find(class_="previous-comment-page")
        # 获取href属性拼接下一页url
        next_url = 'http:' + next_page_tag.get('href')
        return next_url

    def get_img(self, soup):
        """获取图片原图链接函数"""
        img_list = soup.find_all(class_="view_img_link")
        # 循环遍历获取每张图片url
        url_list = []
        for href in img_list:
            url = 'http:' + href.get('href')
            url_list.append(url)
        return url_list

    def img_download(self, url_list, mkdir):
        """图片下载函数"""
        for a in url_list:
            name = a.split('/')[-1]
            with open('./{}/煎蛋_女装_id_{}'.format(mkdir, name), 'wb') as file:
                res_img = requests.get(url=a, headers=self.headers)
                file.write(res_img.content)

    def run(self):
        # 创建资源存储文件夹
        try:
            os.mkdir('./煎蛋女装')
        except:
            print('文件夹已存在！！')
        # 定义初始url链接
        one_url = 'http://i.jandan.net/girl/MjAyMjAxMjktMTAw'
        url = one_url
        down_page = int(input('请输入下载页数:'))
        for i in range(down_page):
            # 向浏览器发送请求
            soup = self.get_html(url)
            # 解析获取图片链接
            url_list = self.get_img(soup)
            print(url_list)
            # 下载图片
            self.img_download(url_list, mkdir='煎蛋女装')
            # 获取下一页链接
            next_page = self.get_next_page(soup)
            url = next_page
            print('第{}页图片下载完毕！！'.format(i + 1))
            time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    spider = SpiderJianDan()
    spider.run()
