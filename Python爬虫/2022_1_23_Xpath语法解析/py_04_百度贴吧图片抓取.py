import random
import time

from lxml import etree
import requests
from urllib import parse
import re, os

word = input('请输入您要查找的贴吧名称:')
num = int(input('请输入您要查询的页数:'))
try:
    os.mkdir('./{}'.format(word))
except:
    print('文件夹已存在！！')
result = parse.quote(word)
url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
headers = {
    'Cookie': 'BIDUPSID=6AC65CD8AC19ED079D42E19E88921B0F; PSTM=1641736785; BAIDUID=3B86FEE5256B4C8477D0F2F7A321B2EB:FG=1; BDUSS=p1SllvOXJMcFFyM29SSHltamJZbmJGZktZRktCMkF6eGFjVXBnNUdFNUowUU5pRVFBQUFBJCQAAAAAAAAAAAEAAADfLECQu-zj58qxv9XC1rvYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAElE3GFJRNxhdF; BDUSS_BFESS=p1SllvOXJMcFFyM29SSHltamJZbmJGZktZRktCMkF6eGFjVXBnNUdFNUowUU5pRVFBQUFBJCQAAAAAAAAAAAEAAADfLECQu-zj58qxv9XC1rvYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAElE3GFJRNxhdF; __yjs_duid=1_1cf39a162fcfc92b747ddcaf701173271642084179747; STOKEN=16b07488234f7b0a5d95effe37f7b7c5d137f0507ded090bd13122efecefae7b; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=F0EB99F7F5637C7DA0FBC4C46982787B:FG=1; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=a06ppbwe9rf&ss=kyqvrlis&sl=h&tt=lk8&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4y75&ul=576g&hd=578j"; BDRCVFR[710W695qCWt]=LpDQ8KNdUpDUhGBrHT8mvqV; H_PS_PSSID=31254_26350; BAIDU_WISE_UID=wapp_1642941973933_957; USER_JUMP=-1; st_key_id=17; 2420124895_FRSVideoUploadTip=1; video_bubble2420124895=1; wise_device=0; BDRCVFR[VBH4JnM-Vd0]=LpDQ8KNdUpDUhGBrHT8mvqV; BA_HECTOR=ag84ag05a1058gakmk1guqkqh0r; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1642429211,1642942102,1642943317,1642946016; tb_as_data=092a99020837ce9936f014c1556500f8fc091321768380d0b4ba94619d12282a2225636e6f304507a7e4bad160b1fdec9f70c6db5669afa43452fe6ecff7dbccb3ad6bc6d420260599f1783dfd0539a1e7585ae0f4f745a646d002beb710564fd37a37dfea358a575f60ae021dd5dab2; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1642946025; ab_sr=1.0.1_ZjM3NDM5MGM1YWE5MmVhYjFiZjI2NDYwOTNmYWVkMzM4NTA4MWI1ZDRjMDYxNDMwMjg2ZTQ3MDIzZWY2YTMwMWNkYTRjZDA3ZTFiNzY0NGUzNzczZjk3NjQ0NTQ2NGM2ZTdmYmJlZmE3YmZmZjc4YjY2YmM3YmJhMWQ4ZGY0NTE=; st_data=196d007e1bb5ac64665dfe3851003ed439f4761ac137b78a1cfda643f983b0caf7a76c3229188ce675d9533db4b2f7edeb92fe42060d2dadac12be956be25a90b943d90c46fc0961cf5de106aabc6ef4f8367046a2709c33b710690b52e3f899; st_sign=50186c12',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'https://tieba.baidu.com/f?kw=%E7%BD%91%E6%81%8B&fr=index',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}
regex1 = '<li class=" j_thread_list clearfix thread_item_box".*?<a rel="noreferrer" href="(.*?)"'
regex2 = '<img class="BDE_Image" src="(.*?)"'
for i in range(num):
    res = requests.get(url=url.format(result, i * 50), headers=headers)
    res.encoding = 'utf-8'
    # print(res.text)
    pattern = re.compile(regex1, re.S)
    r_list = pattern.findall(res.text)
    print(r_list)
    if len(r_list) == 0:
        break
    for link in r_list:
        link = 'https://tieba.baidu.com/' + link
        res_pic = requests.get(url=link, headers=headers)
        for pic_link in re.compile(regex2, re.S).findall(res_pic.text):
            print(pic_link)
            name = pic_link.split('/')[-1]
            print(name)
            pic = requests.get(pic_link, headers=headers)
            with open('./{}/{}'.format(word, name), 'wb') as file:
                file.write(pic.content)
    print('第{}页数据抓取完毕'.format(i + 1))
    time.sleep(random.randint(1, 2))
