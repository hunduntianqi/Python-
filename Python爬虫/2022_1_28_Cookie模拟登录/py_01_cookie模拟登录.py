"""
    session类实现模拟登录:
        requests模块提供了session类, 实现客户端和服务端的会话保持
    原理:
        实例化session对象: s = requests.session()
        session对象发送get()或post请求:
            res = s.post(url=url, data=data, headers=headers)
            res = s.get(url=url, headers=headers)

"""
from requests import session
import requests
import json

# 创建session会话对象
s = session()
# 定义url
url = 'https://t.shuqi.com/'
# 定义请求头避免反爬

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'cna=9tthGuKSFzwCASeV+4HMyRnm; xlly_s=1; imei=9tthGuKSFzwCASeV+4HMyRnm; csrfToken=yT3LtAWjxaVVviizbSwkiSx_; shuqi_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI4MDAwMDAwIiwidXRkaWQiOiIiLCJpbWVpIjoiIiwic24iOiIiLCJleHAiOjE2NDM4NzczNjUsInVzZXJJZCI6IjgwMDAwMDAiLCJpYXQiOjE2NDMzNTg5NjUsIm9haWQiOiIiLCJwbGF0Zm9ybSI6IjAifQ.JMAblvTRg7pqssYdI8nUedxFGTFuNXRxtd20XzlxUTKIZh27ow4gLTv0H9g0T3JRRXAivfiK0-pTC9o1vh-UqQ; shuqi_user_id=8000000; __wpkreporterwid_=71d91d5f-e267-419e-ac2e-0e7b1e376cf3; Hm_lvt_5168aa45c99343e44a3a8ed3019082e3=1643358857,1643358995,1643359073; Hm_lpvt_5168aa45c99343e44a3a8ed3019082e3=1643359077; userid=3188216216; usertoken=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIzMTg4MjE2MjE2IiwidXRkaWQiOiJUMmdBUEJUTTk0MUZ4RmJCamgxVF91R1BiNXNacVEwdFczRmFNVzUzMkthVzFHaDVCSGtQeElPUE54QWhzSVlNS1I4PSIsImltZWkiOiI5dHRoR3VLU0Z6d0NBU2VWKzRITXlSbm0iLCJzbiI6Ijl0dGhHdUtTRnp3Q0FTZVYrNEhNeVJubSIsImV4cCI6MTY0Mzg3NzU0NiwidXNlcklkIjoiMzE4ODIxNjIxNiIsImlhdCI6MTY0MzM1OTE0Niwib2FpZCI6bnVsbCwicGxhdGZvcm0iOiIxNyJ9.FkmXUrvK7jg4iJVdmIC6ttuYnGCGw4waPBdu3J1R7HwBrpf__PMmjdMKUMNBLkSfaMLwwKmLYGVF0EIDOxeU-Q; isg=BOnpxX4MrOsc-JBfUQS2soRH-JVDtt3ophD5goveNlAPUgxk1wcJunUDENbkSnUg',
    'referer': 'https://www.shuqi.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36',
}

res = s.get(url=url, headers=headers)
res.encoding = 'utf-8'
# print(res.text)
# 获取cookies对象
cookies = s.cookies
# 将cookie转换为字典
cookies_dict = requests.utils.dict_from_cookiejar(cookies)
print(cookies_dict)
# 调用json模块的dump函数，把cookies从字典再转成字符串
cookies_str = json.dumps(cookies_dict)
# 将cookies信息写入文件存储
with open('./书旗小说登录cooikes.txt', 'w', encoding='utf-8') as file:
    file.write(cookies_str)