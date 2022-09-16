"""
selenium:自动化测试工具,可以打开浏览器,然后像人一样操作浏览器
         程序员可以从selenium中直接提取网页上的各种信息
环境搭建:
 1.安装selenium模块:pip install selenium
 2.下载浏览器驱动
 3.把浏览器驱动文件放在python解释器所在的文件夹下

"""
from selenium.webdriver import Chrome  # 导入模块,根据浏览器驱动类型选择模块
import time

# 创建浏览器对象
web = Chrome()

# 让浏览器打开百度网址
web.get('http://www.baidu.com')
web.find_element_by_xpath('//*[@id="kw"]').send_keys('青春美少女')
web.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)
web.maximize_window()
time.sleep(3)


