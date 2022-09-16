a = 3
b = 5
# 解法1:使用其他变量
# c = a
# a = b
# b = c
# print(a)
# print(b)

# 解法二：不使用其他变量
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)

# 解法三： 直接交换变量-python专有,利用元祖

a , b = b , a
print(a)
print(b)

"""
列表使用 += 运算符,本质上是调用了extend方法,不会修改变量的引用！！！
"""