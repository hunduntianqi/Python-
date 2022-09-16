from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys  # 导入此模块,可以模拟键盘输入
import time

# 创建浏览器对象
web = Chrome()
web.get('http://lagou.com')

# 找到某个元素-find_element_by_***
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
# 点击找到的元素
el.click()
time.sleep(1)
# 找到输入框,输入要搜索的内容
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)
# time.sleep(1)
# 点击职位名称,打开职位详情信息页面
web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[2]/div[1]/div[1]/div[1]/a/h3').click()
# selenium视角在原来的窗口中,需要切换到新窗口
web.switch_to.window(web.window_handles[-1])  # 切换到最后一个窗口
# 获取招聘信息
job_data = web.find_element_by_xpath('//*[@id="job_detail"]').text
print(job_data)
# 关掉当前窗口
web.close()
# 切换到第一个窗口
time.sleep(1)
web.switch_to.window(web.window_handles[0])
web.close()

