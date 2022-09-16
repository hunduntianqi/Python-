"""
包的概念：
1.包是一个含有多个模块的特殊目录
2.目录下有一个特殊的文件__init__.py
3.包名的命名方式和变量名一致,小写字母+_
4.使用import导入包名可以一次性导入包中的的所有模块
5.__init__.py:
 5.1 要在外界使用包中的模块,需要在__init__.py中指定对外界提供的模块列表
 5.2 在__init__.py文件中导入要被外界使用的模块名,语法如下：
    from . import 模块名1
    from . import 模块名2
    .....

"""
import test_message
test_message.send_message.send('你的手机号欠费了...')
print(test_message.receive_message.receive())