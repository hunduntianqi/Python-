"""
类方法：
1.类属性：
 1.1 使用赋值语句在class关键字下方可以定义类属性
 1.2 类属性用于记录与这个类相关的记录
2.类方法--针对类对象定义的方法
 2.1 在类方法内部可以直接访问类属性或者调用其他的类方法
 2.2 定义类方法语法如下：
   @classmethod
   def 类方法名(cls):
       pass(或类方法实现代码)
  2.2.1 类方法需要用修饰器@classmethod来标识,告诉解释器这是一个类方法
  2.2.2 类方法的第一个参数应为cls（与实例方法的self类似,也可以使用其他名称,习惯使用cls）
  2.2.3 通过类名.调用类方法,调用方法时 ,不需要传递cls参数
  2.2.4 在方法内部：
   2.2.4.1 可以通过cls.访问类的属性
   2.2.4.2 可以通过cls.调用类的其他方法
"""

"""
示例需求：
1.定义一个工具类
2.每件工具都有自己的name
3.需求--在类封装一个show_tool_count的类方法,输出使用当前类,创建的对象个数！！
"""
#
#
# class Tool:
#     count = 0
#     def __init__(self, name):
#         Tool.name = name
#         Tool.count += 1
#         print('这件工具的名字是{}'.format(Tool.name))
#
#     @classmethod
#     def show_took_count(cls):
#         print('现在创建的工具对象个数为:{}'.format(Tool.count))
#
#
# #
# # tool1 = Tool('斧头')
# # tool2 = Tool('榔头')
# Tool.show_took_count()


"""
静态方法
1.应用场景：
 1.1 不需要访问实例属性或调用实例方法
 1.2 不需要访问类属性或调用类方法
2.定义语法：
 @staticmethod
 def 静态方法名():
    pass(或方法实代码)
2.1 静态方法用修饰器@staticmethod标识
2.2 通过类名.调用静态方法
"""


class Dog(object):

    @staticmethod
    def run():
        print('小狗要跑...')


#
# wangcai = Dog()
# wangcai.run()

Dog.run()
