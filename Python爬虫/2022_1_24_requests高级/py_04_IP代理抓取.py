import csv
import random
import time

import requests, re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
url = 'http://www.kxdaili.com/dailiip/1/{}.html'
regex = '<tr.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>'
ip_list = []
for i in range(10):
    res = requests.get(url=url.format(i + 1), headers=headers, timeout=3)
    res.encoding = 'utf-8'
    pattern = re.compile(regex, re.S)
    for ip in pattern.findall(res.text):
        print(ip)
        ip_tuple = (ip[0], ip[1])
        ip_list.append(ip_tuple)
    with open('./ip_data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(ip_list)
    ip_list.clear()
    print('\033[31m第{}页数据抓取完毕\033[0m'.format(i + 1))
    time.sleep(random.randint(1, 2))