"""
单例设计模式：
 1. 设计模式
  1.1 设计模式是前任总结和提炼,通常,被人们广泛流传的设计模式都是针对某一特定问题的成熟的解决方案
  1.2 使用设计模式是为了可重用代码、让代码更容易被他人理解,保证代码的可靠性
2. 单例设计模式
 2.1 目的--让类创建的对象, 在系统中只有惟一的一个实例
 2.2 每一次执行类名（）返回的对象,内存地址是相同的

__new__方法：
1.使用类名创建对象时,python解释器首先会调用__new__方法为对象分配空间
2.__new__是一个由object基类提供的内置的静态方法,主要作用为：
 2.1 在内存中为对象分配空间
 2.2 返回对象的引用
3.python解释器获得对象的引用后,将引用作为第一个参数,传递给__init__方法

重写new方法
1.重写__new__方法一定要return super().__new__(cls)，否则Python解释器得不到分配空间的对象引用
 ,就无法调用对象的初始化方法
2.__new__是一个静态方法,调用时需要主动传递cls参数

初始化方法执行一次的方法：
1. 定义一个类属性init_flag标记是否执行过初始化动作,初始值为False
2. 在__init__中,判断init_flag,如果为False就执行初始化动作
3. 执行初始化动作后将init_flag设置为True

"""


class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1.创建对象时, new方法会被自动调用
        print('创建对象,分配空间！！')
        # 2.为对象分配空间
        # 2.1 判断类属性是否为None,类属性为None,调用父类方法,为第一个对象分配空间,并将引用返回python解释器
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        # 2.2 类属性不是None,直接返回对象的引用
        else:
            return cls.instance

    def __init__(self):
        # 判断是否执行过初始化动作
        if self.init_flag == False:
            print('播放器初始化...')
            self.init_flag = True


# 创建播放器对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

player3 = MusicPlayer()
print(player3)
