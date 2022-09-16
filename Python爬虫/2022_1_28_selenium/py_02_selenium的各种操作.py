"""
当页面上的元素超过一屏后，想操作屏幕下方的元素，是不能直接定位到，会报元素不可见的。这时候需要借助滚动条来拖动屏幕，使被操作的元素显示在当前的屏幕上。滚动条是无法直接用定位工具来定位的。selenium里面也没有直接的方法去控制滚动条，这时候只能借助J了，还好selenium提供了一个操作js的方法:execute_script()，可以直接执行js的脚本。
　　一、控制滚动条高度
    　　1.滚动条回到顶部：
    　　　　js="var q=document.getElementById('id').scrollTop=0"
    　　　　driver.execute_script(js）
    　　2.滚动条拉到底部
    　　　　js="var q=document.documentElement.scrollTop=10000"
    　　　　driver.execute_script(js)
    　　　　可以修改scrollTop 的值，来定位右侧滚动条的位置，0是最上面，10000是最底部。
    　　　　以上方法在Firefox和IE浏览器上上是可以的，但是用Chrome浏览器，发现不管用。Chrome浏览器解决办法：
    　　　　js = "var q=document.body.scrollTop=0"
    　　　　driver.execute_script(js)
　　二、横向滚动条
　　　　1.有时候浏览器页面需要左右滚动（一般屏幕最大化后，左右滚动的情况已经很少见了）。
　　　　2.通过左边控制横向和纵向滚动条scrollTo(x, y）js = "window.scrollTo(100,400);"
　　　　driver.execute_script(js)
　　三、元素聚焦
　　　　虽然用上面的方法可以解决拖动滚动条的位置问题，但是有时候无法确定我需要操作的元素在什么位置，有可能每次打开的页面不一样，元素所在的位置也不一样，怎么办呢？这个时候我们可以先让页面直接跳到元素出现的位置，然后就可以操作了。
　　　　同样需要借助JS去实现。 具体如下：
    　　　　target = driver.find_element_by_xxxx()
    　　　　driver.execute_script("arguments[0].scrollIntoView();", target)
    selenium常用方法:
        browser.get(url): 地址栏输入url地址并确认
        browser.quit(): 关闭浏览器
        browser.close(): 关闭当前页
        browser.maximize_window():浏览器窗口最大化
        browser.page_source: HTML结构源码
        browser.page_source.find('字符串'):从源码中查找指定字符串, 没有返回-1, 常用于判断最后一页
        browser.set__window_size(width, height): 设置浏览器窗口大小
        browser.back(): 浏览器后退
        browser.forward(): 浏览器前进
        browser.refresh(): 模拟浏览器刷新当前页面
        元素对象.clear(): 清除文本内容
        元素对象.send_keys(*value): 模拟按键输入
        元素对象.click(): 模拟浏览器单击元素
    WebElement接口常用方法:
        1. submit(): 提交表单, 例如回车操作
        2. size: 返回元素的尺寸
            例:size = driver.find_element_by_id('kw').size
        3. text: 返回元素的文本
            例:text = driver.find_element_by_id('cp').text
        4. get_attribute(name): 获得元素的属性值, 可以是id, name, type或其他任意属性值
            例:attribute = driver.find_element_by_id('kw').get_attribute('type')
        5. is_displayed(): 该元素是否用户可见, 返回结果为True或False
            例:result = driver.find_element_by_id('kw').is_displayed()
    鼠标事件-ActionChains类:
        导入类:
            from selenium.webdriver import ActionChains
            调用ActionChains类, 浏览器驱动作为参数传入:
                ActionChains(driver)
                ActionChains(driver).鼠标事件方法.perform()
                perform()为对整个操作的提交动作
        1. perform(): 执行所有ActionChains中存储的行为
        2. context_click(): 右击
            # 定位元素
            right_click = driver.find_element_by_id('xx')
            # 执行操作
            ActionChains(driver).context_click(right_click).perform()
        3. double_click(): 双击
            # 定位元素
            double_click = driver.find_element_by_id('xx')
            # 执行操作
            ActionChains(driver).double_click(double_click).perform()
        4. drag_and_drop(source, target): 拖动源元素到目标元素上释放
            source: 鼠标拖动的源元素
            target: 鼠标释放的目标元素
            # 定位元素的原位置
            source = driver.find_element_by_id('xx')
            # 定位元素要拖动到的目标位置
            target = driver.find_element_by_id('xx')
            # 执行操作
            ActionChains(driver).drag_and_drop(source, target).perform()
        5. move_to_element(): 鼠标悬停
            # 定位元素
            above = driver.find_element_by_id('xx')
            # 执行操作
            ActionChains(driver).move_to_element(above).perform()
        6. move_to_element_with_offset(to_element, xoffset):
            移动到距离某个节点多少距离的位置
        7. move_by_offset(xoffset, yoffset):
            鼠标从当前位置, 移动多少的距离
    键盘事件-Keys类:
        导入类:
            from selenium.webdriver.common.keys import Keys
        常用键盘操作:
            send_keys(Keys.BACK_SPACE):删除键(BackSpace)
            send_keys(Keys.SPACE): 空格键(Space)
            send_keys(Keys.TAB): 制表键(Tab)
            send_keys(Keys.ESCAPE): 回退键(Esc)
            send_keys(Keys.ENTER): 回车键(Enter)
            send_keys(Keys.CONTROL, 'a'): 全选(Ctrl + A)
            send_keys(Keys.CONTROL, 'c'): 复制(Ctrl + C)
            send_keys(Keys.CONTROL, 'x'): 剪切(Ctrl + X)
            send_keys(Keys.CONTROL, 'v'): 粘贴(Ctrl + V)
            send_keys(Keys.F1): 键盘F1
            .....
            send_keys(Keys.F1): 键盘F12
    获得验证信息:
        1. driver.title:获得当且页面标题
        2. driver.current_url: 获得当前页面的url
    设置元素等待-页面元素加载:
        1. 显式等待:
            使webdriver等待某个条件成立时继续执行, 否则在达到最大时长时抛出超时异常(TimeOutException)
            方法: WebDriverWait(driver, timeout, poll_frequency, ignored_exceptions)
            driver: 浏览器驱动
            timeout: 最长超时时间, 默认以秒为单位
            poll_frequency: 检测的间隔时间, 默认为0.5s
            ignored_exceptions: 超时后的异常信息, 默认情况下抛NoSuchElementException异常
            WebDriverWait()一般与until()和until_not()方法配合使用:
                until(method, message=''): 调用该方法提供的驱动程序作为一个参数, 直到返回值为True
                until_not(method, message=''): 调用该方法提供的驱动程序作为一个参数, 直到返回值为False
                例: element = WebDriverWait(driver, 5, 0.5).until(
                except_conditions.presence_of_element_located((By.ID, 'kw')))
        2. 隐式等待:
            通过一定时长等待页面上的元素加载完成, 如果超出了设置的时长元素还没有加载, 抛出NoSuchElementException异常
            方法: implicitly_wait(time)
            time: 设置等待时长, 默认单位为秒
            例: driver.implicitly_wait(10)
                driver.get(url)
    多表单切换:
        switch_to.frame()方法:
            将当前定位的主体切换到frame/iframe表单的内嵌页面中
            使用方法:
                1. 先定位到iframe:
                    xpath定位:xf = driver.find_element_by_xpath('xx')
                2. 将定位对象传给switch_to.frame()方法
                    driver.switch_to.frame(xf)
                3. 操作完毕跳出当前一级表单:
                    switch_to.parent_content(): 该方法默认对应于离它最近的switch_to.frame()方法
                    跳出多级表单:
                        switch_to.default_content():跳回最外层页面
    多窗口切换:
        driver.switch_to.window(窗口句柄)方法:切换到相应窗口
        driver.current_window_handle: 获得当前窗口句柄
        driver.window_handles:获得所有窗口的句柄
    操作cookies:
        1. get_cookies(): 获得所有cookie信息
        2. get_cookie(name): 返回字典的键为“name”的cookie信息
        3. add_cookie(cookie_dict): 添加cookie, 'cookie_dict'指字典对象, 必须有name和value值
        4. delete_cookie(name, optionsString): 删除cookie信息, "name"是要删除的cookie的名称,
                                               'optionsString'是该cookie的选项, 包括路径, 域
        5. delete_all_cookies(): 删除所有cookie信息
    调用JavaScript:
        WebDriver提供了execute_script()方法来执行JavaScript代码
        例: 通过JavaScript设置滚动条位置
            window.scrollTop(左边距, 上边距)
            js = 'window.scrollTop(0, 450);'
            driver.execute_script(js)
    处理HTML5的视频播放:
        1. 定位video标签位置
            video = driver.find_element_by_xpath('xxx')
        2. 返回播放文件地址
            url = driver.execute_script('return arguments[0].currentSrc;', video)
            播放视频
                driver.execute_script('return arguments[0].play();', video)
            暂停视频
                driver.execute_script('return arguments[0].pause();', video)
            加载视频
                driver.execute_script('return arguments[0].load();', video)
    窗口截图
        driver.get_screenshot_as_file(path): 截取当前窗口并指定截图图片的保存位置
    Chrome Options配置Chrome启动属性:
        from selenium import webdriver
        options = webdriver.ChromeOptions()
        web = Chrome(options=opt)  # 将设置的浏览器参数传入要创建的浏览器对象
        属性配置:
            options.add_argument('--disable-infobars')  # 禁止策略化
            options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
            options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            options.add_argument('--incognito')  # 隐身模式（无痕模式）
            options.add_argument('--disable-javascript')  # 禁用javascript
            options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
            options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
            options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置
"""
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

# 找到输入框,输入要搜索的内容
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)
# login = web.find_element_by_xpath('/2022-1-12-html/body/section/div[2]/div[1]/div[2]/form/div[1]/input')
# login.send_keys(input('请输入手机号或邮箱:'))
# password = web.find_element_by_xpath('/2022-1-12-html/body/section/div[2]/div[1]/div[2]/form/div[2]/input')
# password.send_keys(input('请输入登录密码:'))
# dl = web.find_element_by_xpath('/2022-1-12-html/body/section/div[2]/div[1]/div[2]/form/div[5]/input')
# dl.click()
# time.sleep(3)
# web.find_element_by_xpath('//*[@id="filterCollapse"]/li[2]/a[6]').click()
# time.sleep(1)
for i in range(30):
    data = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
    # print(data)
    for li in data:
        job_name = li.find_element_by_tag_name('h3').text
        job_price = li.find_element_by_xpath('./div/div/div[2]/div/span').text
        job_company = li.find_element_by_xpath('./div/div[2]/div/a').text
        print(job_company, job_name, job_price)
    # time.sleep(3)
    web.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[6]').click()
    time.sleep(3)
    web.close()
