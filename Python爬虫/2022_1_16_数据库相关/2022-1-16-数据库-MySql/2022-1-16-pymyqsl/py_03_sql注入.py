"""
SQL注入:通过SQL语句的漏洞,盗取数据库的数据！！！
SQL注入无法彻底防止！！！
"""


import pymysql

# 创建连接对象连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password='13480194858gpt', database='python01')

# 获取游标对象
cursor = conn.cursor()
# # 插入新的数据
# sql = "update test set grade=2 where id=5;"
# cursor.execute(sql)

name = input('请输入要查询的人员姓名:')

# 定义变量存储查询SQL语句
sql = "select * from data where name=%s"
# 使用游标执行SQL语句
# 为防止SQL注入,给SQL语句添加参数时,要在execute中写！！！
cursor.execute(sql, [name])
# 获取数据库数据/返回数据为元组
data1 = cursor.fetchone()
print(data1)
data = cursor.fetchall()
for i in data:
    print(i)
    print()
# 对数据表进行修改一定要对数据进行提交,否则数据库中的数据不会发生改变！！！
conn.commit()
# 关闭游标
cursor.close()

# 关闭连接

conn.close()
