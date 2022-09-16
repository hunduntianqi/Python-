"""
    动态加载网站特点:
        1. 查看页面源代码无具体数据
        2. 滚动鼠标滑轮或其他动作时数据才会加载
        3. 页面局部刷新
    动态加载数据分析抓取流程:
        1. F12打开控制台, 执行页面动作开始抓取网络数据包
        2. 抓取返回json文件的网络数据包
        4. XHR: 异步加载的网络数据包
        5. General->Request URL: 返回json数据的URL地址
        6. QueryStringParameters(查询参数) - 观察规律
    注意:请求头中如果带有文件压缩命令, 抓取到的数据会是乱码
    json模块:
      1. json.loads(参数为json格式的字符串)
        把json格式的字符串转为python数据类型
        html = json.loads(res.text)
      2. json.dump(python, file, ensure_ascii=False)
        把python的数据类型转为json格式的字符串并存入文件
        参数1: python类型的数据(字典, 列表等)
        参数2: 文件对象
        参数3: ensure_ascii=False序列化时编码
      3. json.dumps(python数据类型)
        把python数据类型转为json格式的字符串
      4. json.load(json格式的字符串)
        将json文件读取, 并转为python类型
"""
import random
import time

import requests, json

# url = 'https://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 't_id=noimeiweb_fef193f5-bffb-4f45-b992-d4ac4b7bf5ca; __utma=127562001.408224649.1643201935.1643201935.1643201935.1; __utmc=127562001; __utmz=127562001.1643201935.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_765fefc2c357bae3970cea72e714811b=1643201934,1643202243,1643202393; Hm_lpvt_765fefc2c357bae3970cea72e714811b=1643202399; JSESSIONID=653FF5D16FB05FFB35F545F03DEAD385; __utmb=127562001.22.10.1643201935',
    'referer': 'https://app.mi.com/category/2',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

app_list = []
for id in range(10):
    for i in range(3):
        url = 'https://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'.format(i, id)
        res = requests.get(url=url, headers=headers)
        # res = json.loads(res.text)
        # print(res.status_code)
        # print(res.url)
        # print(res.json())
        for app in res.json()['data']:
            # print(app)
            app_dict = {}
            app_dict['name'] = app['displayName']
            app_dict['level1CategoryName'] = app['level1CategoryName']
            app_dict['packageName'] = 'https://app.mi.com/details?id=' + app['packageName']
            app_list.append(app_dict)
            print(app_dict)
        print('====================')
        time.sleep(random.randint(1, 2))
print(app_list)
with open('./app.js', 'w', encoding='utf-8') as file:
    json.dump(app_list, file, ensure_ascii=False)
