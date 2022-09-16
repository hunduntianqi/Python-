import requests

url = 'http://tva1.sinaimg.cn/large/0076BSS5ly8gyuefa69s6j30u011i777.jpg'
res = requests.get(url)
with open('./test.jpg', 'wb') as file:
    file.write(res.content)