from gevent import monkey
monkey.patch_all()
import time, requests, gevent, openpyxl
from bs4 import BeautifulSoup
from gevent.queue import Queue
start=time.time()
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='食物热量信息'
sheet['A1']='食物名称'
sheet['B1']='食物热量'
sheet['C1']='薄荷网链接'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
url_list = []
for x in range(11):
    for y in range(11):
        url1 = 'http://www.boohee.com/food/group/{}?page={}'.format(x + 1, y + 1)
        url_list.append(url1)
for a in range(10):
    url2 = 'http://www.boohee.com/food/view_menu?page={}'.format(a + 1)
    url_list.append(url2)
print(url_list)
work = Queue()
for url in url_list:
    work.put_nowait(url)
def paqushuju():
    while not work.empty():
        url=work.get_nowait()
        res=requests.get(url,headers=header)
        print(res.status_code)
        soup=BeautifulSoup(res.text,'html.parser')
        #print(soup)
        foods=soup.find_all(class_="text-box pull-left")
        for i in foods:
            name_foods=i.find('a')['title']
            quantity_foods=i.find('p').text
            links_foods='http://www.boohee.com/'+i.find('a')['href']
            print(name_foods)
            print(links_foods)
            print(quantity_foods)
            datas=[name_foods,quantity_foods,links_foods]
            sheet.append(datas)
task_list=[]
for e in range(10):
    task=gevent.spawn(paqushuju)
    task_list.append(task)
gevent.joinall(task_list)
wb.save('食物热量信息.xlsx')
end=time.time()
print(end-start)
