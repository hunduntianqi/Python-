for i in range(10):
    print('这是第{}次循环'.format(i+1))
m = 0
while True:
    print('这是{}次循环'.format(m+1))
    if m == 9:
        break
    else:
        m += 1
"""
程序的三大流程：
1.顺序结构：从上到下,顺序执行代码
2.分支结构:根据条件判断,决定执行代码的分支
3.循环结构：让特定代码重复执行
"""
"""
循环：
break：退出循环,不再执行后续循环代码
continue：此代码可以终止本次循环,进入下一次循环
break和continue只对当前所在循环有效
while循环：
语法：
while bool值为真的数值或表达式:
    循环体

如果while中循环条件恒为True,则必须要通过break跳出循环,否则就是一个死循环
使用while循环一定要注意不要产生死循环！！！

for循环
语法
for 遍历变量 in 可迭代数据：
    循环体
for循环通过可迭代数据来限制循环次数,也可以通过break跳出循环,或
通过continue终止本次循环进入下一次循环！！！
"""