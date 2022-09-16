import pymysql

# 创建连接对象链接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password='13480194858gpt', database='python01')
# 获取游标对象
cursor = conn.cursor()
while True:
    # 定义变量存储sql语句
    sql = input("请输入您要执行的修改数据库操作:")
    if sql == "exit":
        break
    # 使用游标执行sql语句
    cursor.execute(sql)
    # 提交数据, 修改数据库数据
    conn.commit()
    if "select" in sql:
        for i in cursor.fetchall():
            print(i)
# 关闭游标
cursor.close()
# 关闭链接
conn.close()