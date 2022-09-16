"""
    proxies:代理IP参数:
        定义:代替自己原来的IP地址去对接网络的IP地址
        作用:隐藏自身真实IP, 避免被网站封掉
        语法格式:proxies = {'协议':'协议://IP:端口号'}
            示例:
                proxies = {
                    'http':'http://IP:端口号',
                    'https':'https://IP:端口号'
                }
        高匿代理: web站点只能看到代理IP
        普通代理: Web站点知道请求是通过代理IP访问的, 但是不知道用户真实IP
        透明代理: Web站点既能看到代理IP, 又能看到用户真实IP
    通过代理IP网站获取代理IP
        私密代理和独享代理:
            使用需要用户名和密码的认证, 用户名和密码在对应代理IP网站上查找:
            语法格式:
                proxies = {
                    '协议':'协议://用户名:密码@IP:端口号'
                }

"""
import requests

url = 'http://httpbin.org/get'
proxies = {
    'https': 'https://183.173.140.145:10080',
    'http': 'http://183.173.140.145:10080'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
res = requests.get(url=url, proxies=proxies, verify=False, timeout=3, headers=headers)
print('\033[35m{}\033[0m'.format(res.text))
