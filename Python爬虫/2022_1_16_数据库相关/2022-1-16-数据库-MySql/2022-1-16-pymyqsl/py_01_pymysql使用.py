"""
1.导入pymysql包
2.创建连接对象
 调用pymysql模块中的connect()函数来创建连接对象,代码如下:
  conn = connect(参数表):
   参数host:连接的MySQL主机,如果是本机是'localhost'
   参数port:连接的MySQL主机端口,默认是3306
   参数user:连接的用户名
   参数password:连接的密码
   参数database:数据库的名称
   参数charset:通信采用的编码方式,推荐使用utf-8
 连接对象操作说明:
   关闭连接:conn.close()
   提交数据:conn.commit()
   撤销数据:conn.rollback()
3.获取游标对象
 获取游标对象的目标是要执行sql语句,完成对数据库的增、删、改、查操作
 游标可以记录获取数据的个数,第一次取出第一条数据,第二次会从第二条从数据开始读取
  调用连接对象的cursor()方法获取游标对象:cur = conn.cursor()
  操作说明:
   3.1 使用游标执行SQL语句:execute(operation[parameters])执行SQL语句,返回受影响的行数,主要用于执行insert,update,delete,select
       等语句
   3.2 获取查询结果集中的一条数据:cur.fetchone()返回一个元组,如（1, '张三'）
   3.3 获取查询结果集中的所有数据:cur.fetchall()返回一个元组,如(1,'张三'),(2,'李四')
   3.4 关闭游标:cur.close(),表示和数据库的操作完成

"""
import pymysql

# 创建连接对象连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password='13480194858gpt', database='python_test')
# 获取游标对象
cursor = conn.cursor()
# 定义变量存储查询SQL语句
sql1 = 'select * from data;'
# 使用游标执行SQL语句
cursor.execute(sql1)
# 获取数据库数据/返回数据为元组
data1 = cursor.fetchone()
print(data1)
# 获取Sql语句执行后查询到的剩余数据(如果之前有执行fetchone(), 则已查询到的数据不会再获取)
data = cursor.fetchall()
for i in data:
    print(i)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
