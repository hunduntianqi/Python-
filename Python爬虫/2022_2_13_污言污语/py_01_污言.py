"""
    污言污语爬取:
        根据页面规则, 多次对页面发送请求, 获取不同的响应数据, 解析污言污语

"""
import requests
from lxml import etree

url = 'https://www.nihaowua.com/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

# 定义正则表达式
regex = '<section> <div id="post15" class="post15"> <q>(.*?)</q> </div> </section>'
num = int(input('请输入请求次数:'))
with open('./污言污语.txt', 'w', encoding='utf-8', newline='') as file:
    for i in range(num):
        source = requests.get(url, headers=headers).content.decode()
        # 实例化etree对象
        tree = etree.HTML(source)
        data = tree.xpath('/html/body/div[1]/section//text()')[2]
        print(data + '\n')
        file.write(data + '\n')