import time

import requests
import re
from urllib import parse
import csv
import random


class BaiDuVideo:
    def __init__(self):
        self.url = 'https://haokan.baidu.com/web/search/api?pn={}&type=video&query={}&sfrom=recommend'
        # https://haokan.baidu.com/web/search/api?pn=1&rn=10&type=video&query=
        self.headers = {
            'referer': 'https://haokan.baidu.com/web/search/page?query='.format(parse.quote('古风')),
            # ":authority": "haokan.baidu.com",
            # ":method": "GET",
            # ":path": "/web/search/api?pn=2&type=video&query=%E5%8F%A4%E9%A3%8E%E7%BE%8E%E5%A5%B3&sfrom=recommend",
            # ":scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            'cookie': 'BIDUPSID=6AC65CD8AC19ED079D42E19E88921B0F; PSTM=1641736785; BAIDUID=3B86FEE5256B4C8477D0F2F7A321B2EB:FG=1; BDUSS=p1SllvOXJMcFFyM29SSHltamJZbmJGZktZRktCMkF6eGFjVXBnNUdFNUowUU5pRVFBQUFBJCQAAAAAAAAAAAEAAADfLECQu-zj58qxv9XC1rvYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAElE3GFJRNxhdF; BDUSS_BFESS=p1SllvOXJMcFFyM29SSHltamJZbmJGZktZRktCMkF6eGFjVXBnNUdFNUowUU5pRVFBQUFBJCQAAAAAAAAAAAEAAADfLECQu-zj58qxv9XC1rvYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAElE3GFJRNxhdF; __yjs_duid=1_1cf39a162fcfc92b747ddcaf701173271642084179747; BAIDUID_BFESS=FAD0B6D5EA736DDFD4E936A7D10A95A2:FG=1; hkpcvideolandquery=%u7B80%u5355%u6613%u5B66%u7684%u82B1%u94BF%u6559%u7A0B%uFF0C%u4E00%u770B%u5C31%u4F1A%20%u8C37%u5170%u5316%u5986%u57F9%u8BAD%u5B66%u6821%20%u53E4%u98CE%20%u82B1%u94BF%u5986; BD_SVTK=WteO3EWWnfkYlotW3WZa108dO0tFlj0lf8Phl8fkZWAoQnfD9fP20fl1PltQiOl00kgA1AQaTA59QnfD9tOOJ9l1xJS8lPlKtpPcJ90pP0H7lF0OS0x60flNF0HxpjpeS8OSf8tleWEAQgiY01Y48A1hO0tH1Pivt3PK3lI8kaamB; reptileData=%7B%22data%22%3A%22aa93ae061d35627b92b06882b5727bd940bab9a728c04c44d029e798cdb4bbc2d1a7676b3d422b49a436ab718d92fac2d4751e9c7e981b4a341da60c087592d45fcf3d12edad0dc9238e04f8a3d6efd70dfd7547799458b17244164a8e002901%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%2295e769a3%22%7D; ab_sr=1.0.1_MmJhOWE0NDFkN2EyMzExYTViMTNlYzUwZDYzZDY5Nzk3Mzk1ZGEwMTQzYjc2NDNjYjU1YmM3ZGVmNzYwNjNlYmNhNGVjNTkxMDZjYTM0NjIwYWYyM2UwZDVmNWUwNjdk; BA_HECTOR=25842k0kah0h040gje1guodk60q; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; hkpcSearch=%u53E4%u98CE%24%24%24%u53E4%u98CE%u5973%u795E%24%24%24%u7537%u5B50%u5BB6%u66B4%u59BB%u5B50%u88AB%u62D85%u65E5%24%24%24%u53E4%u98CE%u7F8E%u5973; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1642869221,1642869409,1642870128,1642870909; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1642870935; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=rywfshihi5&ss=kyq0s2dl&sl=t&tt=tqg&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=25ovf',
            "sec-ch-ua": '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests":'1',
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

    def get_html(self, url):
        res = requests.get(url=url, headers=self.headers, verify=False)
        print(res.status_code)
        print(res.url)
        print(res.headers)
        res = res.text
        print(res)
        return res

    def parse_re(self, res):
        regex = '"title":"(.*?)".*?"url":"(.*?)"'
        pattern = re.compile(regex, re.S)
        r_list = []
        for link in pattern.findall(res):
            list = []
            list.append(link[1].replace('\\/', '\\'))
            list.append(link[0])
            r_list.append(list)
        return r_list

    def data_save(self, list, word):
        with open('./{}视频链接.csv'.format(word), 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            for link in list:
                writer.writerow(link)

    def run(self):
        start = time.time()
        word = input('请输入您要查询视频的关键字:')
        result = parse.quote(word)
        num_video = int(input('请输入您要查询的视频页数:'))
        with open(r'D:\Users\Administrator\IdeaProjects\python_爬虫\2022_1_24_requests高级\ip_Pool.csv', 'r') as file:
            ip_list = file.readlines()
            print(ip_list)
        for i in range(num_video):
            url = self.url.format(i + 1, result)
            res = self.get_html(url)
            list = self.parse_re(res)
            if len(list) == 0:
                break
            print(list)
            self.data_save(list, word)
            print('第{}页链接下载完毕！！'.format(i + 1))
            time.sleep(random.randint(1, 2))
        end = time.time()
        print('共用时:{}s'.format(end - start))


if __name__ == '__main__':
    spider = BaiDuVideo()
    spider.run()
