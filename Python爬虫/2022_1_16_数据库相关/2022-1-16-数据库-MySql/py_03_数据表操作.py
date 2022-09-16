"""
注意：操作数据表要先选择一个数据库！！！
查看当前数据库中的所有表：show tables;
创建表：
    字段以,分隔，最后一个字段后不需要加逗号！！！
    (字段后面必须先写数据类型,再写约束,数据类型必须有,约束可有可无)：create table 数据表名字（字段，类型，约束[,字段，类型，约束]）；
    例如：
    create table xxx(
        id int unsigned not null,
        name varchar(30) not null,
        .....

    );

查看表的结构：desc 数据表名字；

查看表的创建语句:show create table 数据表名;
修改表（alter）：
 添加字段:alter table 表名 add 列名（字段名） 数据类型及约束;
 修改字段-不重命名:alter table 表名 modify 列名 数据类型及约束;
 修改字段-重命名:alter table 表名 change 原字段名 新字段名 数据类型及约束;
 删除字段:alter table 表名 drop 列名;
删除表:drop table 表名;

插入数据:
 全列插入：insert into 表名 values(....);
 部分插入:insert into 表名 (字段1,...) values(字段1的值,...);
 多行插入:insert into 表名 values(第一行数据),(第二行数据);
修改数据:
 全部修改:update 表名 set 字段1=值1,字段2=值2,....;
 按条件修改:update 表名 set 字段1=值1,字段2=值2,.... where 条件;
查询数据:
 查询所有列:select * from 表名;
 定条件查询:select * from 表名 where 条件;
 查询指定列:select 字段1,字段2,....from 表名;
 使用as为字段或数据表指定别名:select 字段1 as 别名,字段2 as 别名 from 表名;
 指定字段显示顺序:select 字段1,字段2,.... from 表名;
删除数据:
 delete from 表名 where 条件;
消除重复行:select distinct 字段 from 表名;




"""