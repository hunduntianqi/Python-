# 打印小星星
# m = 0
# while m <= 15:
#     print((15-m)*' '+'*'*m+'*'*m)
#     m += 1
#     if m == 15:
#         while m > 0:
#             print((15-m)*' '+'*'*m+'*'*m)
#             m -= 1
#     if m == 0:
#         break
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('{} * {} = {}'.format(j, i, i * j), end='\t\t')
        j += 1
    print()
    i += 1
"""
字符串中的转义字符：
\\:反斜杠符号
\'：单引号
\":双引号
\n:换行
\t:横向制表符
\r:回车
"""
