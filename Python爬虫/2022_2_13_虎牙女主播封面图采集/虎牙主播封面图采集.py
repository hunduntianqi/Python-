import re
import os
import requests
from fake_useragent import UserAgent
try:
    os.mkdir('./虎牙直播封面')
except:
    pass

headers = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Host': 'www.huya.com',
    'Referer': 'https://www.huya.com/g/4079',
    'Cookie': 'SoundValue=0.50; alphaValue=0.80; huya_ua=webh5&0.1.0&websocket; isInLiveRoom=; udb_guiddata=9ab1809ae84d4029af74b1558684b686; udb_deviceid=w_564172682180108288; Hm_lvt_51700b6c722f5bb4cf39906a596ea41f=1649245226; __yamid_tt1=0.18895777248778023; __yasmid=0.18895777248778023; __yamid_new=C9C675FE72300001C0CC11A93F001F1E; _yasids=__rootsid%3DC9C675FE727000017EF61B9018771B96; game_did=0tnEv6Q1hq-2fsb5EGm9tF6e-Od3DSWadYu; udb_passdata=3; udb_anouid=1463873763674; huya_flash_rep_cnt=5; Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f=1649245911; huya_web_rep_cnt=458',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
}
page = 1
flag = True
while flag:
    url = 'https://www.huya.com/cache.php?' \
          'm=LiveList&do=getLiveListByPage&gameId=4079&tagAll=0' \
          '&callback=getLiveListJsonpCallback&page={}'.format(page)
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    print(response.text)
    total_page_regex = '"data":{"page":.*?,"pageSize":120,"totalPage":(.*?),"totalCount"'
    img_regex = '"screenshot":"(.*?).jpg?'
    total_page = re.compile(total_page_regex, re.S).findall(response.text)[0][0]
    print(total_page)
    for img_url in re.compile(img_regex, re.S).findall(response.text):
        img_url = img_url.replace('\\', '').replace('?', '') + '.jpg'
        img_name = img_url.replace('\\', '').replace('?', '').split('/')[-1]
        print(img_name, img_url)
        response_img = requests.get(img_url)
        with open('./虎牙直播封面/{}'.format(img_name), 'wb') as file:
            print(response_img.content)
            file.write(response_img.content)
    page += 1
    if page > int(total_page):
        flag = False

