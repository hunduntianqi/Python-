'''
    urllib.1_request模块-python标准库:
        作用:向网站发出请求
        urlopen()-获取一个响应对象:
            作用:向网站发出请求并获取响应对象
            参数:
                url:需要爬取的网站地址
                timeout:设置等待超时时间, 指定时间内未响应抛出超时异常
            相应对象方法:
                1. read():返回数据类型为bytes, 需要使用decode()方法转换为字符串
                2. geturl(): 返回实际数据的url地址
                3. getcode(): 返回http响应码

'''
# 导入模块
from urllib import request

res = request.urlopen(url="http://www.baidu.com/", timeout=3000)
# 响应对象方法read()
html = res.read().decode('utf-8')
print(html)
print(res.geturl())
print(res.getcode())

