"""
列表（list）
1）python中使用最频繁的数据类型,在其他语言通常叫做数组
2）专门用于存储一串信息
3）列表用[]定义, 数据之间用英文逗号 , 分隔
4）列表的索引从 0 开始
   索引：数据在列表中的位置编号, 又可以被称为 下标
注意：从列表中取值时, 如果超出索引范围 ,程序会报错！！！
"""

name_list = ['']

for i in range(3):
    name = input('请输入你的名字:\n')
    name_list.append(name)
print(name_list)
"""
列表常用方法：
1.列表.insert（索引,数据）：在指定位置插入数据
2.列表.append（数据）：在列表末尾追加数据
3.列表.extend（列表2）：将列表2的数据追加到列表
4.del 列表[索引]：删除指定索引的数据
5.列表[索引] = 数据：修改指定索引的数据
6.列表.remove[数据]:删除第一个出现的指定数据
7.列表.pop：删除列表末尾的数据
8.列表.pop[索引]：删除指定索引的数据
9.列表.clear：清空列表
10.len(列表)：统计列表长度
11.列表.count（数据）：统计数据在列表中出现的次数
12.列表.sort（）：升序排序；列表.sort（rever = True）：降序排序
13.列表.reverse：列表翻转,逆序
14.列表.index（数据）：取列表中对应数据的索引值

使用tuple函数可以将列表转换为元组
tuple（列表）
"""
import keyword

list_test = keyword.kwlist

print(list_test)