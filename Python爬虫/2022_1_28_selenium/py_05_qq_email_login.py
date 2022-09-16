"""
    使用selenium登录qq邮箱
"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


# 配置浏览器启动属性
options = ChromeOptions()
# 设置窗口最大化
options.add_argument('--start-maximized')
# 避免被检测
options.add_argument('--disable-infobars')
# 设置隐身模式
options.add_argument('--incognito')
# 禁用JavaScript
options.add_argument('--disable-javascript')
# 无头浏览器
# options.add_argument('--headless')
# 创建Chrome浏览器对象
web = Chrome(options=options)
# 启动浏览器
web.get('https://mail.qq.com/')

xf = web.find_element_by_xpath('//*[@id="login_frame"]')
web.switch_to.frame(xf)
web.find_element_by_xpath('//*[@id="u"]').send_keys(input('请输入您的qq账号:'))
web.find_element_by_xpath('//*[@id="p"]').send_keys(input('请输入您的登录密码:'))
web.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(2)
# 获取html页面结构源码
print(web.page_source)
# 获取登陆后页面标题
print(web.title)
# 获取登陆后页面url
print(web.current_url)
time.sleep(5)
# web.switch_to.default_content()
web.close()

