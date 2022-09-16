"""
异常的概念：
1.程序运行时,python解释器遇到一个错误,停止程序的运行,并提示错误信息
2程序停止执行并且提示错误信息这个动作,称之为抛出异常
3.通过异常捕获可以对突发事件做集中处理,保证程序的稳定性和健壮性
异常捕获语法：
try:
    正常执行的代码
except (异常类型,不填默认为所有异常类型均捕获):
    对异常的处理代码
4.异常的传递--当函数/方法出现异常,会将异常传递到函数/方法的调用一方,当传递到主程序时,如果还没有异常处理,程序将被终止！！！

"""
"""
异常捕获演练：
1.让用户输入整数,并打印出用户输入的数字
2.当用户输入非整数时,再次提示用户输入整数
"""

# while True:
#     try:
#         num = int(input('请输入一个整数:'))
#         print(num)
#         break
#     except:
#         print('请输入正确的整数数字！！！')
#
# print('-' * 50)

"""
针对不同异常类型做出不同响应语法：
try:
    # 尝试执行的代码
    pass
except 异常类型1：
    # 针对异常类型1做出的处理
    pass
except (异常类型2, 异常类型3):
    # 针对异常类型2&3做出的处理
    pass
# 捕获未知错误
except Exception as result:
    print('未知错误{}'.format(result))

"""

# while True:
#     try:
#         num = int(input('请输入一个整数:'))
#         print(8 / num)
#         break
#     except ZeroDivisionError:
#         print('除0错误！！！')
#     except ValueError:
#         print('数据类型错误')
# print('-' * 50)

"""
异常捕获完整语法：
try:
    尝试执行的代码
    pass
except 错误类型1:
    针对错误类型1做出的处理
    pass
except (错误类型2, 错误类型3):
    针对错误类型2&3做出的处理
    pass
# 捕获未知错误
except Exception as result:
    # 打印错误信息
    print('未知错误{}'.format(result))
else:
    # 没有异常才会执行的代码
    pass
finally：
    # 无论是否有异常,都会执行的代码
    print('无论是否有异常,都会执行的代码！！')
    
    
"""
"""
异常传递演练
1.定义demo1（）函数,返回用户输入数字
2.定义demo2（）函数,返回调用demo1函数的执行结果
3.打印demo2（）函数的执行结果

"""


def demo1():
    return int(input('请输入一个整数:'))


def demo2():
    return demo1()


# 利用异常的传递性,在主程序中对异常进行处理
flag = 1
while flag:
    try:
        print(demo2())
        flag = 0
    except ValueError:
        print('请输入正确的数字！！')
