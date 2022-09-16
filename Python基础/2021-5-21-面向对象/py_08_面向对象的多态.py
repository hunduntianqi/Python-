"""
多态：
 1.可以增加代码的灵活度
 2.以继承和重写方法为前提
 3.是调用方法的技巧,不会影响到类的内部设计

"""

"""
需求：
1.在Dog类中封装方法game
    普通狗只是简单的玩耍
2.定义XiaoTianQuan继承自Dog,并重写game方法
    哮天犬要在天上玩耍
3.定义person类,并且封装一个和狗玩的方法
   在方法内部,直接让狗对象调用game方法
"""

class Dog:

    def __init__(self, name):
        self.name = name

    def game(self):
        print('{}在蹦蹦跳跳的玩耍！！！'.format(self.name))


class XiaoTianQuan(Dog):

    def game(self):
        print('{}飞到天上玩耍'.format(self.name))


class Person:

    def __init__(self, name):
        self.name = name

    def game(self, dog):
        print('{}和{}一起快乐的玩耍...'.format(self.name, dog.name))


# dog = Dog('旺财')
xtq = XiaoTianQuan('哮天犬')
xioaming = Person('小明')
xioaming.game(xtq)

