"""
    MongoDB:
        非关系型数据库, 数据以键值对方式基于磁盘存储
        数据类型单一:值为JSON文档
        数据库结构:
            库->集合->文档
    MongoDB常用命令:
        1. 进入MongoDB命令行:mongo
            退出: exit
        2. 查看所有库:show dbs
        3. 切换到指定库: use 库名
        4. 查看当前库中的所有集合: show collections
        5. 查看当前库中的文档:db.集合名.find().pretty()
        6. 统计集合中文档数量: db.集合名.count()
        7. 删除集合: db.集合名.drop()
        8. 删除当前库:db.dropDatabase()

    pymongo模块使用:
        1. 创建连接对象: conn = pymongo.MongoClient('localhost', 27017)
        2. 创建库对象: db = conn['库名']
        3. 创建集合对象: myset = db['集合名']
        4. 在集合中插入文档: myset.insert_one({})
        5. 在集合中插入文档2:myset.insert_many([{}, {}, {}, {}.....{}])
        注意:
            MongoDB无需提前建库建集合, 直接操作即可, 会自动建库建集合
"""

import pymongo

# 创建连接对象
conn = pymongo.MongoClient('localhost', 27017)
# 创建库对象
db = conn['maoyan']
# 创建集合对象
myset = db['mao']
# 在集合中插入一条文档
myset.insert_one({'name': '郭鹏涛', 'age': '23', 'sex': '男'})
# 在集合中插入多条文档
myset.insert_many([{'name': '郭鹏涛', 'age': '23', 'sex': '男'},
                   {'name': '陈欣妮', 'age': '23', 'sex': '女'}]
                  )
db_test = conn['中国植物油行业协会']
mycol_set = db_test['行业动态']
data_list = []
for data in mycol_set.find():
    print(data)
    data_list.append(data)
print(len(data_list))