'''
    urllib.parse编码模块:
        作用:对url地址中的中文进行编码, 解决中文乱码问题, 通常时给查询参数编码
        导入模块
            1. import urllib.parse
            2. from urllib import parse
        示例:
            编码前:https://www.baidu.com/s?wd=美女
            编码后:https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
        urlencode()方法:
            作用:给url地址中查询参数进行编码, 参数类型为字典
            示例:
                编码前:params = {'wd':'美女'}
                编码中:params = urllib.parse.urlencode(params)
                编码后:params结果:'wd=%E7%BE%8E%E5%A5%B3'
            多个查询参数:params = {'参数1':'值1', '参数2':'值2', ...}
            urlencode()方法会自动对多个查询参数之间添加&符号链接
        quote()方法:
            作用: 给url地址中的查询参数进行编码, 参数类型为字符串
            示例:
                word = '美女'
                result = urllib.parse.quote(word)
                result结果:'wd=%E7%BE%8E%E5%A5%B3'
        unquote()方法:
            作用:将编码后的字符串转为普通的Unicode字符串
            示例:
                params = 'wd=%E7%BE%8E%E5%A5%B3'
                result = parse.unquote(params)
                result结果:美女

'''
from urllib import parse, request

params = parse.urlencode({'wd': '赵丽颖'})
print(params)

result = parse.quote('美女')
print(result)