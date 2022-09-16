"""
    requests模块:
        作用:类似于urllib, 向网站发送请求获取响应
"""

import requests

url = 'https://baidu.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400"
}

res = requests.get(url=url, headers=headers)
print(res.text)