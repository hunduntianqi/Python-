import csv

import requests, re


class proxyPool:
    def __init__(self):
        self.albe_ip_Pool = []
        self.ip_list = []
        self.test_url = 'http://httpbin.org/get'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }

    def get_ip_proxies(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }
        url = 'http://www.kxdaili.com/dailiip/1/{}.html'
        regex = '<tr.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>'
        for i in range(10):
            res = requests.get(url=url.format(i + 1), headers=headers, timeout=3)
            res.encoding = 'utf-8'
            pattern = re.compile(regex, re.S)
            for ip in pattern.findall(res.text):
                # print(ip)
                ip_tuple = (ip[0], ip[1])
                self.ip_list.append(ip_tuple)

    def parse_proxies(self):
        ip_list = []
        for ip in self.ip_list:
            ip_list.append(ip[0] + ':' + ip[1])
        return ip_list

    def get_html(self, proxies):
        res = requests.get(url=self.test_url, timeout=2, headers=self.headers, proxies=proxies)
        return res.text

    def proxy_test(self, proxies):
        try:
            res = self.get_html(proxies=proxies)
            print('\033[31m{}:可用\033[0m'.format(proxies))
            self.albe_ip_Pool.append((proxies['http'], proxies['https']))
        except:
            print('\033[32m{}:不可用\033[0m'.format(proxies))

    def run(self):
        self.get_ip_proxies()
        list = self.parse_proxies()
        print(list)
        for ip in list:
            proxies = {
                'http': 'http://{}'.format(ip),
                'https': 'https://{}'.format(ip)
            }
            self.proxy_test(proxies)
        print(self.albe_ip_Pool)
        with open('./ip_Pool.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.albe_ip_Pool)


if __name__ == '__main__':
    spider = proxyPool()
    spider.run()
