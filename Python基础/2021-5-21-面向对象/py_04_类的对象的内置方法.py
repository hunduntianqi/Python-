"""
初始化方法：
当使用类名（）创建对象时,会自动执行以下操作：
  1）为对象在内存中分配空间-创建对象
  2）为对象的属性设置初始值-初始化方法（init）
初始化方法：__init__方法.,__init__是对象的内置方法
__init__方法是专门用来定义一个类具有哪些属性的方法

"""

# class Cat():
#     def __init__(self):
#         # self.属性名 = 属性的初始值
#         self.name = "Tom"
#         print('{}是一个猫对象！！'.format(self.name))
#
#     def eat(self):
#         print("{}爱吃鱼".format(self.name))
#
#
# # 使用类名创建对象会自动调用初始化方法！！
# tom = Cat()
# tom.eat()
# tom.name = '懒猫'
# tom.__init__()
# tom.eat()

"""
使用参数设置属性初始值：
"""

#
# class Cat():
#     def __init__(self, name):
#         # self.属性名 = 属性的初始值
#         self.name = name
#         print('{}是一个猫对象！！'.format(self.name))
#
#     def eat(self):
#         print("{}爱吃鱼".format(self.name))
#
#     # 在对象被销毁前执行的方法__del__,与__init__相对应
#     def __del__(self):
#         print('{}凉了'.format(self.name))
#
#
# tom = Cat(name='Tom')
# tom.eat()
#
# lazy_cat = Cat('懒猫')
# lazy_cat.eat()
#
# # del关键字可以删除对象
# del tom
#
# print('-' * 50)

"""
对象的生命周期：
1.一个对象从调用类名（）创建,生命周期开始
2.一个对象的__del__方法被调用后,生命周期结束
在对象的生命周期内,可以调用类的属性和方法！！！
"""

"""
__str__方法：
使用print()函数打印某一个对象变量,希望在控制台看到一些我们自己希望看到的内容
可以使用__str__方法,该方法要求必须返回一个字符串！！！

"""


class Cat():
    def __init__(self, name):
        # self.属性名 = 属性的初始值
        self.name = name
        print('{}是一个猫对象！！'.format(self.name))

    def eat(self):
        print("{}爱吃鱼".format(self.name))

    # 在对象被销毁前执行的方法__del__,与__init__相对应
    def __del__(self):
        print('{}凉了'.format(self.name))

    def __str__(self):
        # 此方法必须返回一个字符串！！！
        return 'my is cat'


tom = Cat('Tom')
print(tom)