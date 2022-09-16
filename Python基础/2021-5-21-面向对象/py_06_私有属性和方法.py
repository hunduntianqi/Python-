"""
应用场景：对象的某些属性或方法只希望在对象的内部被使用,不希望在外部被访问到
1.私有属性：对象不希望公开的属性
2.私有方法：对象不希望公开的方法

定义方式：在属性名或方法名前增加两个下划线'__',定义的就是私有属性和方法：

class Test:

    def __init__(self, name, age):
        self.name = name # 非私有属性
        self.__age = age # 私有属性

    # 非私有方法
    def test1(self):
        pass


    # 私有方法
    def __test2(self):
        pass
提示：python中并没有真正的私有,在外界如果要访问私有属性和方法,要在私有属性和方法前加上‘_类名’,即：--> _类名__属性名或方法名
    （在日常开发中不推荐使用此方法访问私有属性和方法）
"""


class Women:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部可以访问对象的私有属性！！！
        print('{}的年龄是{}岁'.format(self.name, self.__age))


xiaofang = Women('小芳')

# 私有属性,在外界不能被直接访问,以下代码会报错！！！
# print(xiaofang.__age)
# 私有方法也不允许在外界直接访问,以下代码会报错！！！
# xiaofang.__secret()
# 以下代码可以访问私有属性和私有方法！！！
print(xiaofang._Women__age)
print(xiaofang._Women__secret())