"""
逻辑运算符：程序开发需要多个判断条件时需要用到的运算符
逻辑运算符可以把多个条件按照逻辑进行连接,变成更复杂的条件
Python中的逻辑运算符包括：与：and/或：or/非：not
语法：
and
条件1 and 条件2
两个条件同时满足,返回True
有一个条件不满足,返回False

or
条件1 or 条件2
只要有一个条件满足,就返回True
所有条件都不满足,才返回False

not
not 条件
对条件进行取反,若条件成立,返回False
            条件不成立,返回True
"""
#逻辑运算符演练：
# and / or
# age = 120
# my_age = int(input('请输入你的年龄'))
# print(0 < my_age or my_age <age)
# print(0 < my_age and my_age <age)
# not
# 在开发中,通常希望某个条件不满足时,执行一些代码,可以使用 not
# 另外,如果需要拼接复杂的逻辑计算条件,同样也有可能使用到 not
is_employee = False
if not is_employee:
    print('非本公司人员,请勿入内！！！')