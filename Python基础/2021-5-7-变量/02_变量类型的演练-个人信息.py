"""
定义变量保存小明的个人信息：
姓名：小明
年龄：18岁
性别：男
身高：1.75米
体重：75.0公斤
"""
# 在Python中,定义变量是不需要指定变量的类型
# 在运行的时候,Python 解释器,会根据赋值语句等号右侧的数据
# 自动推导出变量中保存数据的准确类型
#str是一个字符串类型
name = '小明'
#int是一个整数类型
age = 18
#bool 表示一个布尔类型,真：True；假：False
grade = True
# float是一个浮点数类型
highter = 1.75
weight = 75.0

print('{}{}男孩,今年{}岁了,身高{}米,体重{}公斤'.format(name,grade,age,highter,weight))
print(type(name))