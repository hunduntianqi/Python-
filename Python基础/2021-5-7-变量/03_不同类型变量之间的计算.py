"""
数字型变量可以直接计算
如果变量是bool型：
True对应数字1
False对应数字0
"""
# i = 10
# fl = 0.5
# booler = True
# print(i*fl,i+fl,i-fl,i+booler,i-booler)
# print(i * booler)
# booler = False
# print(i * booler)

"""
字符串变量：
1.字符串之间可以使用‘+’拼接生成新的字符串
2.字符串变量可以和整数变量通过‘*’,来将字符串复制特定次数生成新的字符串
"""
i = 3
str1 = 'gpt'
str2 = 'cxn'
str3 = str1 + str2
str4 = str2 * i
print(str3)
print(str4)

# 数字型变量和字符串之间不能进行其他计算
