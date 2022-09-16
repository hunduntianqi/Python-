"""
在Python中通过input函数从键盘获取用户输入
用户输入的内容Python认为是一个字符串
语法：
变量名 = input（‘提示信息：’）

"""
# name = input('请输入你的名字：')
#
# print(name)

"""
类型转换函数:可以用来转换input函数接受到的数据类型
int（X）：可以将变量x转换为整数类型
floa（x）：可以将变量x转换为浮点数类型
str(x)：可以将变量x转换为字符串类型
"""

m = input('请输入一个数字\n')
print(type(m))
print(int(m))
print(float(m))
