"""
    准备环境:
        1. js调试工具
            发条js调试工具:
                先通过对被加密的数据关键字进行搜索, 寻找到对应js文件, 再通过加密关键字搜索到相关加密代码,
            使用js调试工具对代码进行测试改写, 使改写代码达到与js源代码相同的加密效果
        2. PyExecJs模块
            作用:使用python模拟执行js代码
            使用流程:
                1. 环境安装:
                    1.1 安装node js开发环境
                    1.2 pip insatll PyExecJs安装模块
                2. 将调试后改写完成的js代码存入js文件保存
                3. 模块使用:
                    3.1 导入模块:
                        import execjs
                    3.2 实例化node对象
                        node = execjs.get()
                    3.3 编译js源文件
                        ctx = node.compile(open('js源文件路径', encoding = 'utf-8'))
                    3.4 执行js函数
                        result = ctx.ecal(要执行的函数名(字符串形式))
    js算法改写初探:
        1. 对可能与加密相关的关键代码打断点
        2. 在代码调试时, 如果发现了相关自定义变量的缺失, 一般将其定义为空字典
        3. 在调试过程中, 发现js内置对象未定义, 一般将其定义为this关键字
        4. 需要单独捕获的变量可以将其定义为参数, 在python代码中对其赋值
"""
# 导包
import execjs
import requests

# # 实例化node对象
# node = execjs.get()
# # 编译js源文件
# ctx = node.compile(open('./weixin.js', encoding='utf-8').read())
# # 执行js函数
# funcName = 'getPwd("{}")'.format('2251789949gpt')
# pwd = ctx.eval(funcName)
# print(pwd)



# 模拟登录实现
# 实例化node对象
node = execjs.get()
# 编译js源文件
ctx = node.compile(open('./weixin.js', encoding='utf-8').read())
# 定义登录名
username = input('请输入邮箱或微信号:')
password = input('请输入登录密码:')
# 对密码进行加密
pwd = ctx.eval('getPwd("{}")'.format(password))
# 定义post请求form表单字典
fromdata = {
    'username': username,
    'pwd': pwd,
    'imgcode': '',
    'f': 'json',
    'userlang': 'zh_CN',
    'redirect_url': '',
    'token': '',
    'lang': 'zh_CN',
    'ajax': '1'
}

url = 'https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
session = requests.session()
response = session.post(url=url, data=fromdata, headers=headers)

print(response)