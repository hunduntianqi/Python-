# 无头浏览器:浏览器在后台运行,直接拿到数据

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select  # 导入模块,处理select标签
import time

# 设置无头浏览器
opt = Options()  # 创建Options对象
opt.add_argument('--headless')  # 设置参数为无头
opt.add_argument('--disable-gpu')  # 设置参数为不使用显卡
web = Chrome(options=opt)  # 将设置的浏览器参数传入要创建的浏览器对象
web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

# # 定位下拉列表
# sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# # 对元素进行包装,包装成下拉菜单
# sel = Select(sel_el)
# # 让浏览器选择不同选项
# for i in range(len(sel.options)):  # 此时的i为每一个下拉框选项的索引位置
#     sel.select_by_index(i)  # 按照索引进行切换
#     time.sleep(2)
#     table = web.find_element_by_xpath('//*[@id="TableList"]/table').text
#     print(table)
time.sleep(2)
# 拿到selenium加载后的页面代码Elements(是经过数据加载以及js执行后的结果的html内容)
print(web.page_source)
