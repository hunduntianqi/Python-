"""
索引的介绍:
 索引在MySQL中也叫作"键",是一个特殊的文件,保存着数据表里所有记录的位置信息,相当于一本书的目录,能加快数据库的查询速度！！
 应用场景:当数据库中的数据量很大时,查找数据会变得很慢,我们就可以通过索引来提高数据库查询效率！！
 查询表中已有的索引:show index from 表名;
开启时间监测：set profiling=1;
给字段创建索引:alter table 表名 add index(字段);
开启时间监测后,查看每条SQL语句的执行时间:show profiles;

"""
import pymysql


def main():
    # 创建coonection连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='13480194858gpt', database='python01')

    # 获得cursor对象
    cur = conn.cursor()
    sql = input("请输入您要进行的数据库操作:\n")
    cur.execute(sql)
    # 插入10万次数据
    for i in range(100000):
        cur.execute("insert into test_index values('ha-{}')".format(i))
    data = cur.execute('select * from test_index;')
    for x in range(data):
        print(x)
    # 提交数据
    conn.commit()


if __name__ == '__main__':
    main()
