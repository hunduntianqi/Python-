"""
抛出raise异常
1.应用场景：
 1.1 在开发中.代码执行出错Python解释器会抛出异常
 1.2 还可以根据应用程序特有的业务需求,主动抛出异常
 1.3 例如：提示用户输入密码,如果长度少于8,抛出异常
2.抛出异常
 2.1 Python中提供了一个Exception异常类
 2.2 在开发时,如果满足特定业务需求,希望抛出异常,可以：
  2.2.1 创建一个Exception对象
  2.2.2 使用raise关键字抛出异常对象

"""

"""
需求演练：
1.定义input_password函数,提示用户输入密码
2.如果用户输入密码长度<8,抛出异常
3.如果用户输入密码长度>=8,返回输入的密码
"""


def input_password():
    # 1.提示用户输入密码
    pwd = input('请输入密码:')

    # 2.判断密码长度>=8,返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3.如果密码长度<8,抛出异常
    print('主动抛出异常！！')
    # 创建异常对象
    ex = Exception('密码长度不够！！')
    # 主动抛出异常对象
    raise ex


try:
    print(input_password())
except Exception as result:
    print('未知错误:{}'.format(result))
