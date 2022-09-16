'''
    urlencode示例:百度搜索关键字, 保存关键字.html到本地html文件
'''

from urllib import request, parse

# 1. 拼接url地址
word = input('请输入搜索关键字:')
params = parse.urlencode({'wd': word})
url = 'http://baidu.com/s/?{}'.format(params)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
# 2. 发请求获取响应内容
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
print(res.getcode())
print(res.geturl())
html = res.read().decode()
# 3. 保存到本地文件
with open('./{}.html'.format(word),'w', encoding='utf-8') as file:
        file.write(html)
