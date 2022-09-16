"""F12抓取移动端有道翻译"""

import requests
from bs4 import BeautifulSoup
while True:
    word = input('请输入要翻译的单词(exit退出):')
    if word == 'exit':
        break
    fromdata = {
        'inputtext': word,
        'type': 'AUTO'
    }

    url = 'http://m.youdao.com/translate'

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Referer': 'http://m.youdao.com/translate?vendor=fanyi.web',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    res = requests.post(url=url, data=fromdata, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find(id="translateResult").find('li').text
    print(data)