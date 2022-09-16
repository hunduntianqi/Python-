'''
    网站判定请求数据来源--请求头(headers)--user-Agent:
        测试网站:http://httpbin.org/get
        向测试网站发请求, 会返回请求头内容
    重构User-Agent:
        urllib.request.Request()方法:
            作用: 包装请求头, 包装完成后使用urlopen()方法发送请求
            参数:
                url:请求的网络地址
                headers:添加请求头, 类型为字典headers = {'User-Agent':'伪装的浏览器请求头'}
    请求头使用构造流程:
        1. 构造请求对象: req = request.Request(url=url, headers=headers)
        2. 获取响应对象: res = request.urlopen(req)
        3. 获取响应内容: html = res.read().decode()
    随机生成UA:
        from fake_useragent import UserAgent模块
            UserAgent().random:每次调用时随机生成一个UA
                UserAgent().random 可以获取任意浏览器的请求头
                UserAgent().Chrome 可以获取谷歌浏览器的请求头
                UserAgent().firefox 可以获取火狐浏览器的请求头
                使用方法:
                headers = {
                    'User-Agent':str(UserAgent().random)
                }
'''

from urllib import request

# res = request.urlopen('http://httpbin.org/get')
# html = res.read().decode('utf-8')
# print(html)
url = 'http://httpbin.org/get'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
# 包装请求头
req = request.Request(url=url, headers=headers)
# 获取响应对象
res = request.urlopen(req)
# 获取响应内容
html = res.read().decode()
# 打印输出
print(html)