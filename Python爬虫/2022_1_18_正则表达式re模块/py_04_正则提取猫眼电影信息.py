"""
    抓取目标:
        猫眼电影TOP100的电影名称, 主演, 上映时间
"""
import random
import re
import time
from urllib import request, parse


class MaoYanSpider:
    def __init__(self):
        """定义参数"""
        self.url = 'https://www.maoyan.com/board/4?timeStamp=1642512746095&channelId=40011&index=4&signKey=b1c267ab9b024451ebe7546857d1203a&sVersion=1&webdriver=false&offset={}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

    def get_html(self, url):
        """获取响应内容"""
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        print(html)
        print(res.geturl())
        return html
    def parse(self, html):
        """数据解析函数"""
        # 定义正则匹配规则
        regex = '<div class="movie-item-info">.*?title="(.*?)" .*?class="star">.*?(.*?).*?class="releasetime">(.*?)'
        pattern = re.compile(regex, re.S)
        # r_list = [(name, star, time), (), ()....]
        r_list = pattern.findall(html)
        return r_list
    def save_html(self, r_list):
        """数据处理函数"""
        item = {}
        for r in r_list:
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()
            print(item)
    def run(self):
        """程序入口函数"""
        for offset in range(0, 10):
            url = self.url.format(offset * 10)
            html = self.get_html(url)
            r_list = self.parse(html)
            self.save_html(r_list)
            time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    maoyan = MaoYanSpider()
    maoyan.run()
