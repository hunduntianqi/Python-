"""
    re模块使用流程:
        方法一:
            r_list = re.findall('正则表达式', html, re.S)
            该方法返回结果为列表
        方法二:
            pattern = re.compile('正则表达式', re.S)
            r_list = pattern.findall(html)
        注意:
            1. findall()方法的到的结果一定为列表
            2. re.S作用为使正则表达式元字符.可匹配\n在内的所有字符
        匹配任意一个字符正则表达式:
            方法一:
                pattern = re.compile('[/s/S]')
                result = pattern.findall(html)
            方法二:
                pattern = re.compile('.*', re.S)
                result = pattern.findall(html)
    正则表达式分组匹配:
        匹配时先按照整体正则匹配, 然后再提取分组()中的内容
        如果有2个及以上分组(), 在结果中以元组形式显示[(), (), ()...]

"""

import re

# r_list = re.findall('AB', 'ABCABCDEFGANC', re.S)
# print(r_list)

# 分组示例
html = 'A B C D'
pattern = re.compile('\w+\s+\w+')
r_list = pattern.findall(html)
print(r_list) # r_list = ['A B','C D']

pattern = re.compile('(\w+)\s+\w+')
r_list = pattern.findall(html)
print(r_list) # r)list = ['A', 'C']

pattern = re.compile('(\w+)\s+(\w+)')
r_list = pattern.findall(html)
print(r_list) # r_list = [('A', 'B'), ('C', 'D')]
