"""
字符串常用方法：
1.len（字符串）：统计字符串长度
2.大字符串.count（小字符串）：统计小字符串在大字符串中出现的次数
3.大字符串.index（小字符串）：获取第一个小字符串出现的索引位置（子字符串不存在,程序会报错）

"""
"""
一、判断类型方法：
1.string.isspace():如果String中只包含空格/'\n'/'\t'/'\r',则返回True
2.string.isalnum（）：如果string中至少有一个字符,并且所有字符都是字母或数字，则返回True
3.string.isalpha（）：如果string中至少有一个字符,并且所有字符都是字母则返回True
4.string.isdecima（）：如果string只包含数字则返回True,全角数字
5.string.isdigit()：如果string只包含数字则返回True,全角数字、（1）、\u00b2
6.string.isnumeric()：如果string只包含数字则返回True,全角数字、汉字数字
7.string.istitle()：如果string是标题化的（每个单词首字母大写）则返回True
8.string.islower()：如果string中包含至少一个区分大小写的字符,并且这些（区分大小写）字符都是小写,则返回True
9.string.isupper()：如果string中包含至少一个区分大小写的字符,并且这些（区分大小写）字符都是大写,则返回True

二、查找和替换类型方法：
1.string.startswith(str)：检查字符串是否以str开头,是则返回True
2.string.endswith(str)：检查字符串是否以str结束,是则返回True
3.string.find(str,stat=0,end=len(string))：检查str是否包含在string中,如果start和end指定范围,则检查是否包含在指定范围
                                           内,是则返回开始的索引值,否则返回-1
4.string.rfind(str,stat=0,end=len(string))：类似于find函数,不过是从右边开始查找
5.string.index(str,stat=0,end=len(string))：和find()方法类似,若str不在string会报错
6.string.rindex(str,stat=0,end=len(string))：类似于index（），从右边开始
7.string.replace(old_str,new_str,num=string.count(old)):把string中的old_str替换成new_str,若果指定num,则替换次数不
                                                        超过指定次数

三、大小写转换方法：
1.string.capitalize()：把字符串的第一个字符大写
2.string.title()：把字符串的每个单词首字母大写
3.string.lower()转换string中的所有大写字符为小写
4.string.upper()：转换string中的小写字母为大写
5.string.swapcase():翻转string中的大小写

四、文本对齐方法：
1.string.ljust(width)：返回一个原字符串左对齐,并使用空格填充至长度width的新字符串
2.string.rjust（width）：返回一个原字符串右对齐,并使用空格填充至长度width的新字符串
3.string.center(width)：返回一个原字符串居中,并使用空格填充至长度width的新字符串

五、去除空白字符方法：
1.string.lstrip():截掉string左边的空白字符
2.string.rstrip():截掉string右边的空白字符
3.string.strip()：截掉string左右两边的空白字符

六、拆分和连接方法：
1.string.partition(str):把字符串string分成一个3元素的元组（str前面,str,str后面）
2.string.rpartition（str）：右partition类似,从右边开始查找
3.string.split(str=""，num):以str为分隔符切片string,如果num有指定值,则仅分隔num+1个子字符串,str默认包含'\t','\r'
                            '\n'和空格
4.string.splitlines()：按照行（'\r','\n','\t'）分隔,返回一个包含各行为元素的列表
5.string.join(seq)：以string为分隔符,将seq中所有的元素（字符串）合并为一个新的字符串

"""
# # 1.判断空白字符
# space_str = '  \t\r\n'
#
# print(space_str.isspace())
#
# # 2.判断字符串中是否只包含数字
#
# # num_str = '123456'
# # num_str = '\u00b2'
# num_str = '一'
# print(num_str.isdecimal())
# print(num_str.isdigit())
# print(num_str.isnumeric())
#
# hello_str = 'hello world'
# # 1.判断是否以指定字符串开始
# print(hello_str.startswith('H'))
# # 2.判断是否以指定字符串结束
# print(hello_str.endswith('lD'))
# # 3.查找指定字符串
# # index方法同样可以查找指定字符串在大字符串中的索引
# # 区别在于,若查找字符串不存在,index方法会报错,而find方法则会返回-1，不会报错！！！
# print(hello_str.find('ll'))
#
# # 4.替换字符串
# # replace方法执行完成会返回一个新的字符串,不会改变原来的字符串！！！
# print(hello_str.replace('l','m',1))

poem = ['  登鹳雀楼  ',
        ' 王之涣  ',
        '  白日依山尽     ',
        ' 黄河入海流 ',
        '欲穷 千里目',
        '更 上一层 楼']

for poem_str in poem:
    print('↑{}↑'.format(poem_str.strip().center(5,'　')))