import csv
import random
import time

from lxml import etree
import requests


address = input('请输入您要查询二手车的地址(完整拼音):')
num = int(input('请输入您要查询的页数:'))
path = 'https://www.che168.com'
url = path + '/{}/a0_0msdgscncgpi1ltocsp{}exx0/'
            # /zhengzhou/a0_0msdgscncgpi1ltocsp2exx0/?pvareaid=102179#currengpostion

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Referer': 'https://www.che168.com/{}/a0_0msdgscncgpi1ltocsp1exx0/'.format(address),
    'Host': 'www.che168.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie': 'fvlid=1642595339493nNWs9Mr1iInF; sessionid=f26971a6-bf92-40e5-a80f-1921c8c4f675; che_sessionid=4E58735F-8760-4616-BD11-5F7B0A813A8A%7C%7C2022-01-19+20%3A29%3A06.526%7C%7Cwww.autohome.com.cn; listuserarea=110100; sessionip=106.34.164.195; area=411528; sessionvisit=12313ffc-1fe2-41ef-b634-5970df85331d; sessionvisitInfo=f26971a6-bf92-40e5-a80f-1921c8c4f675|www.autohome.com.cn|100533; Hm_lvt_d381ec2f88158113b9b76f14c497ed48=1642595340,1642595493,1642601716,1642920264; che_sessionvid=FC3B2D42-58A0-49CF-94E0-AFB47D8F7132; UsedCarBrowseHistory=0%3A42821725%2C0%3A42710923%2C0%3A41882558%2C0%3A42529073%2C0%3A42809189%2C0%3A42852967%2C0%3A42639140%2C0%3A41631683%2C0%3A42892248; userarea=110000; ahpvno=6; showNum=34; Hm_lpvt_d381ec2f88158113b9b76f14c497ed48=1642920388; ahuuid=DEFB7B2F-A7E2-4768-8B3B-8F57179C85D3; v_no=23; visit_info_ad=4E58735F-8760-4616-BD11-5F7B0A813A8A||FC3B2D42-58A0-49CF-94E0-AFB47D8F7132||-1||-1||23; che_ref=www.autohome.com.cn%7C0%7C100533%7C0%7C2022-01-23+14%3A46%3A37.265%7C2022-01-19+20%3A29%3A06.526; sessionuid=f26971a6-bf92-40e5-a80f-1921c8c4f675'
}
data_list = []
tuple_header = ('车辆品牌', '表显里程', '上牌时间', '挡位', '排量', '车辆所在地', '定价(万)')
data_list.append(tuple_header)
for i in range(1, num + 1):
    url = url.format(address, i)
    res_link = requests.get(url, headers=headers)
    tree = etree.HTML(res_link.text)
    link_list = tree.xpath('//*[@id="goodStartSolrQuotePriceCore0"]/ul/li')
    print(link_list)
    print(len(link_list))
    for num_link in range(1, len(link_list) - 1):
        # print(link_list[num_link].xpath('./a/@href'))
        link = path + link_list[num_link].xpath('./a/@href')[0]
        res_data = requests.get(link, headers=headers)
        tree_data = etree.HTML(res_data.text)
        name = tree_data.xpath('/html/body/div[5]/div[2]/h3/text()')[0].strip()
        mileage = tree_data.xpath('/html/body/div[5]/div[2]/ul/li[1]/h4/text()')[0]
        time = tree_data.xpath('/html/body/div[5]/div[2]/ul/li[2]/h4/text()')[0]
        gears = tree_data.xpath('/html/body/div[5]/div[2]/ul/li[3]/h4/text()')[0].split('/')[0].strip()
        displacement = tree_data.xpath('/html/body/div[5]/div[2]/ul/li[3]/h4/text()')[0].split('/')[1].strip()
        local = tree_data.xpath('/html/body/div[5]/div[2]/ul/li[4]/h4/text()')[0]
        price = tree_data.xpath('//*[@id="overlayPrice"]/text()')[0]
        tuple_car = (name, mileage, time, gears, displacement, local, price)
        print(tuple_car)
        data_list.append(tuple_car)

with open('./汽车之家{}二手车信息.csv'.format(address), 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_list)