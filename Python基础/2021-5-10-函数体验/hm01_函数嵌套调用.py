"""
函数嵌套调用：在一个函数里面又调用另外的函数！！！
如果函数1调用了函数2
1）执行到调用函数2的位置时,会先执行函数2
2）当函数2执行完毕时,会回到调用函数2的位置,继续执行后续的代码

"""
# def test1():
#     print('妮妮')
#
#
# def test2():
#     m = 1
#     while m <= 10:
#         test1()
#         print('我爱你！！')
#         m += 1
#
#
# test2()

# 打印分隔线
def print_line(char,num,lines):
    """
    打印分割线！！
    :param char: 分隔线符号类型参数
    :param num: 分隔符号数量参数
    :param lines:打印的分割线行数参数
    :return: None
    """
    for i in range(lines):
        print(char * num)

# print_line('*',50)
# print_line('-',100)
# print_line('+',200)
# print_line('/',150)