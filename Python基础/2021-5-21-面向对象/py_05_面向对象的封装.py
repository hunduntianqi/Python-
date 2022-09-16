"""
封装：
1.封装是面向对象编程的一大特点
2.面向对象编程的第一步-将属性和方法封装到一个抽象的类中
3.使用类创建对象,让对象调用方法
4.对象方法的细节都被封装在类的内部
5.一个对象的属性可以是另外一个类创建的对象！！
提示：在定义属性时,如果不知道设置什么初始值,可以设置为None
1.None关键字表示什么都没有
2.None表示一个空对象,没有方法和属性,是一个特殊的常量
3.可以将None赋值给任何一个变量
"""
"""
封装案例1-小明爱跑步
需求：
1.小明体重75.8公斤
2.小明每次跑步会减肥0.5公斤
3.小明每次吃饭会增加1公斤
提示：
1.在对象的方法内部,是可以直接访问对象的属性的！！！
2.同一个类创建的多个对象之间,属性互补干扰！！
"""

# class Person():
#     def __init__(self, name, weight):
#         # self.属性 = 形参
#         self.name = name
#         self.weight = weight
#         print('{}的体重是{}公斤'.format(name, weight))
#
#     def __str__(self):
#         return '我的名字叫{},体重是{}公斤'.format(self.name, self.weight)
#
#     def run(self):
#         self.weight -= 0.5
#         print('{}跑步了,现在的体重是{}公斤'.format(self.name, self.weight))
#
#     def eat(self):
#         self.weight += 1
#         print('{}吃了一顿饭,现在的体重是{}公斤'.format(self.name, self.weight))
#
#
# xiaoming = Person('小明', 78.5)
# xiaoming.run()
# print(xiaoming)
# num = 100
# xiaoming.eat()
# print(xiaoming)
# print(xiaoming.weight)
#
# xiaomei = Person('小美', 45.0)
# print(xiaomei)
# xiaomei.eat()
# xiaomei.run()
# print(xiaomei)
# print(xiaomei.weight)


"""
封装案例2-摆放家具
1.房子（House）有户型,总面积,家具名称列表
 新房子没有任何家具
2.家具（HouseItem）有名字和占地面积
  1）席梦思床（bed）占地4平米
  2）衣柜（chest）占地2平米
  3）餐桌（table）占地1.5平米
3.将以上家具添加到房子中
4.打印房子时,要求输出:户型,总面积,剩余面积,家具名称列表
5.剩余面积：
 1）在创建房子对象时,定义一个剩余面积的属性,初始值和总面积相等
 2）当调用add_item（添加家具）方法时,让剩余面积 -= 家具面积！！
6.多个类开发时,被其他类使用到的类应优先开发!!!
"""

#
# class HouseItem:
#
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return '[{}]的占地面积是{}平米'.format(self.name, self.area)
#
#
# class House:
#
#     def __init__(self, house_type, area):
#         self.house_type = house_type
#         self.area = area
#
#         # 剩余面积
#         self.free_area = area
#
#         # 家具名称列表
#         self.item_list = []
#
#     def __str__(self):
#         # python 能够自动将一对括号内部的代码连接在一起
#         return ('房子的户型是:{},\n总面积为:{}平米,\n剩余面积有:{}平米,\n家具有:{}'
#                 .format(self.house_type, self.area, self.free_area, self.item_list))
#
#     def add_item(self, item):
#         if item.area < self.free_area:
#             print('要添加家具{}'.format(item))
#             self.item_list.append(item.name)
#             self.free_area = self.area - item.area
#         else:
#             print('家具{}的面积太大,家里放不下！！'.format(item.name))
#
#
# # 创建家具对象
# bed = HouseItem('席梦思', 4)
# chest = HouseItem('衣柜', 2)
# table = HouseItem('餐桌', 1.5)
# # 打印家具对象
# print(bed)
# print(chest)
# print(table)
# # 创建房子对象
# house = House('一室一厅', 60)
#
# # 调用add_item方法添加家具
# house.add_item(bed)
# house.add_item(chest)
# house.add_item(table)
# print(house)


"""
封装案例3-士兵突击
需求：
1.士兵许三多有一把AK47
2.士兵可以开火
3.枪能够发射子弹
4.枪可以装填子弹-增加子弹数量
"""


class Gun:

    def __init__(self, module, bullet_count):
        # 枪的型号
        self.module = module
        # 枪的初始数量
        self.bullet_count = bullet_count
        print('有一把枪的名字是{},现在子弹数量为{}'.format(self.module, self.bullet_count))

    def add_bullet(self, count):
        self.bullet_count += count
        print('填装了{}颗子弹,现在的子弹数量为{}'.format(count, self.bullet_count))

    def shoot(self, num):
        if self.bullet_count > 0:
            self.bullet_count -= num
            print('突突突...,现在子弹数量为{}'.format(self.bullet_count))
        else:
            print('{}已经没有子弹了,需要填充子弹！！！'.format(self.module))


class Soldier:

    def __init__(self, name):
        self.name = name
        # 通过None关键字定义枪的初始属性（没有枪）
        self.gun = None

    def fire(self, num):
        if self.gun is not None:
            print('{}:兄弟们,冲啊！！！'.format(self.name))
            if self.gun.bullet_count > 0:
                self.gun.shoot(num)
                print('士兵{}扣动扳机开火了,现在子弹减少了{}颗,还剩{}颗'.format(self.name, num, self.gun.bullet_count))
            else:
                print('{}现在没有子弹,需要先填充子弹'.format(self.gun.module))
        else:
            print('士兵{}没有枪,无法冲锋!!!'.format(self.name))

    def __str__(self):
        if self.gun is None:
            return '士兵{}没有枪,无法冲锋!!!'.format(self.name)
        else:
            return '士兵{}有一把{}'.format(self.name, self.gun.module)


ak47 = Gun('AK47', 0)
solidaer = Soldier('许三多')
# 修改gun的属性,将ak47赋值给gun属性（‘让士兵有枪’）
solidaer.gun = ak47
print(solidaer)
solidaer.fire(10)
ak47.add_bullet(5)
solidaer.fire(3)

"""
身份运算符：用于比较两个对象的内存地址是否一致--是否是对同一个对象的引用
 在Python中针对None比较时,建议使用is判断
 is：是判断两个标识符是不是引用同一个对象,x is y 类似于id(x) == id(y)
 is not:判断两个标识符是不是引用不同对象,x is not y类似于id(x) != id(y)
 
is 与 == 的区别：
is用于判断两个变量引用对象是否为同一个
==判断引用变量的值是否相等
"""
a = 5
b = 3
print(a is b)  # 执行结果为False
print(a is not b)  # 执行结果为True
