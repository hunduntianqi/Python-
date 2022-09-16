"""
    bs4解析:
        解析原理:
            1. 实例化一个BeautifulSoup对象, 并且将页面源码加载到该对象中
            2. 通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
        解析步骤:
            1. 实例化BeautifulSoup对象
                from bs4 import BeautifulSoup
                1.1 将本地的html文档中的数据加载到该对象:
                    fp = open('./本地html文件', 'r', encoding='utf-8')
                    soup = BeautifulSoup(fp, 'lxml')
                1.2 将互联网上获取到的页面源码加载到该对象中:
                    response = requests.get(url)
                    soup = Beautiful(response.text, 'lxml')
            2. 调用Beautiful对象提供的方法和属性:
                2.1 soup.tagName: 获取第一个对应标签的全部内容
                2.2 soup.find(’tagName‘): 类似于soup.tagName
                    soup.find(class_='类名'): 返回第一个对应类名的标签
                    soup.find('tagName', class_='类名'): 返回对应标签中嵌套的满足类名的第一个标签
                    注意: class定位属于属性定位, class也可以换做id等其他标签属性
                2.3 soup.find_all(): 与find()方法使用一致, 不过是返回所有满足条件的标签, 以列表形式
                2.4 soup.select(’某种选择器‘): 表示使用选择器定位标签, 包括类选择器, id选择器, 标签选择器等
                                            返回的是满足所有条件的标签, 以列表形式
                        层级选择器代码格式:
                            soup.select('层级1 > 层级二 > 层级三 > 层级4....'): 每个层级可以使用不同形式的
                                                                             选择炁进行定位
                            soup.select('层级1 > 层级二  层级4....'): 每个层级可以使用不同形式的选择炁进行定位
                            注意:
                                层级选择器中: '>' 表示一个层级, ’ ‘(空格)表示间隔多个层级
                2.5 获取标签之间的文本数据:tagName.text/string/get_text():
                    text/get_text(): 可以获取一个标签下的全部文本内容(包括该标签嵌套标签中的文本内容)
                    string: 只能获取该标签下的文本内容, 不能获取嵌套标签中的文本内容
                2.6 获取标签中的属性值:
                    soup.tagName['对应属性名']
"""
# 案例实战:彼岸美图4k图片爬取
import time
import os
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 创建文件夹存储下载的图片
try:
    os.mkdir('./images')
except:
    print('文件夹已存在！！')
# 第一页链接与其他页面链接不同, 先定义初始url地址
start_url = 'https://pic.netbian.com/4kmeinv/index.html'

# 定义请求头
herders = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__yjs_duid=1_2499ddfc44072a5783ae4d3a3349ad351644156254053; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1644156246; zkhanecookieclassrecord=%2C54%2C66%2C53%2C; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1644156679',
    'if-modified-since': 'Sat, 05 Feb 2022 17:38:14 GMT',
    'referer': 'https://pic.netbian.com/4kmeinv/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': str(UserAgent().random)
}

i = 1
flag = True
while flag:
    # if判断是否为第一页
    if i == 1:
        url = start_url
    else:
        url = 'https://pic.netbian.com/4kmeinv/index_{}.html'.format(i)
    # 获取页面所有图片源码信息
    response_source_text = requests.get(url=url)
    response_source_text.encoding = 'gbk'
    print(response_source_text.text)
    # 实例化Beautiful对象, 解析图片详情链接
    soup_source = BeautifulSoup(response_source_text.text, 'lxml')
    pic_link_list = soup_source.find('ul', class_="clearfix").find_all('a')
    for pic_link in pic_link_list:
        # 拼接图片详情链接
        pic_data = 'https://pic.netbian.com' + pic_link['href']
        print(pic_data)
        # 获取图片详情页面源码信息
        response_pic = requests.get(pic_data)
        response_pic.encoding = 'gbk'
        # 实例化beautiful对象解析图片大图链接
        soup_pic = BeautifulSoup(response_pic.text, 'lxml')
        pic_url = 'https://pic.netbian.com' + soup_pic.find(id="img").find('img')['src']
        pic_name = soup_pic.find('div', class_="photo-hd").text
        # 请求获取图片信息
        pic_source = requests.get(pic_url)
        content = pic_source.content
        # 保存图片
        with open('./images/{}.jpg'.format(pic_name), 'wb') as file:
            file.write(content)
        print(pic_name + '下载完毕')
    print('第{}页图片下载完毕！！'.format(i))
    time.sleep(1)
    i += 1
    if '下一页' not in response_source_text.text:
        flag = False
    else:
        pass
