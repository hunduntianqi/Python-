'''
    findall:匹配字符串中所有符合正则的内容,返回一个列表
    print(re.findall(r"\d+", '我的电话号是:17320101759,她的电话是:13480194858'))

    finditer:匹配字符串中所有的内容,返回一个迭代器,从迭代器中拿到内容需要.group()
    it = re.finditer(r"\d+", '我的电话号是:17320101759,她的电话是:13480194858')
    print(it)
    for i in it:
        print(i.group())

    search返回的结果是match对象,拿到内容需要.group(),找到一个符合正则的内容就结束
    s = re.search(r"\d+", '我的电话号是:17320101759,她的电话是:13480194858')
    print(s.group())

    match是从字符串头部开始匹配,第一个字符不符合正则会报错
    m = re.match(r"\d+", '我的电话号是:17320101759,她的电话是:13480194858')
    print(m.group())

    compile可以预加载正则表达式,可以提高一点效率
    obj = re.compile(r'\d+')  # 用obj来代表正则‘\d+’
    ret = obj.finditer('我的电话号是:17320101759,她的电话是:13480194858')
    for i in ret:
        print(i.group())

    print(obj.findall('我的电话号是:17320101759,她的电话是:13480194858'))
'''
import re


