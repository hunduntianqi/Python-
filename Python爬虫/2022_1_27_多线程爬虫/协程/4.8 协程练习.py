from gevent import monkey
monkey.patch_all()
import gevent, requests, time, openpyxl
from bs4 import BeautifulSoup
from gevent.queue import Queue

start = time.time()
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '豆瓣TOP250'
sheet['a1'] = 'NO.'
sheet['b1'] = '电影名称'
sheet['c1'] = '豆瓣评分'
sheet['d1'] = '推荐语'
sheet['e1'] = '影片链接'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
work = Queue()
url_list = []
for m in range(11):
    url_list.append('https://movie.douban.com/top250?start={}'.format(m * 25))
    print(url_list)
for url in url_list:
    work.put_nowait(url)


def renwu():
    while not work.empty():
        # for url in url_list:
        url = work.get_nowait()
        res = requests.get(url, headers=header)
        soup = BeautifulSoup(res.text, 'html.parser')
        datas = soup.find_all('div', class_="item")
        for j in datas:
            recommends = j.find(class_="inq")
            # print(recommends)
            if recommends != None:
                nums = j.find('em').text
                # print(nums.text)
                names = j.find('span').text
                evalus = j.find(class_="rating_num").text
                recommend = recommends.text
                links = j.find('a', class_="")['href']
                print(nums + '.', names, '豆瓣评分为:' + evalus, '\n', '推荐语:' + recommend, '\n',
                      links)
                sheet.append([nums, names, evalus, recommend, links])
            else:
                recommend = ''
                nums = j.find('em').text
                names = j.find('span').text
                evalus = j.find(class_="rating_num").text
                links = str(j.find('a', class_="")['href'])
                print(nums + '.', names, '豆瓣评分为:' + evalus, '\n', '此影片' + recommend, '\n',
                      links)
                sheet.append([nums, names, evalus, recommend, links])


tasks_list = []
for x in range(10):
    task = gevent.spawn(renwu)
    tasks_list.append(task)
gevent.joinall(tasks_list)
wb.save("协程存储.xlsx")
end = time.time()
print(end - start)
