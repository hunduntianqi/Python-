"""
条件查询:
比较运算符查询:select */要查找的字段 from 表名 where 数据类型为可比较大小的字段+比较运算符+限制条件(例:age>18);
 大于:>
 小于:<
 大于等于:>=
 小于等于:<=
 等于:=
 不等于:!=或<>

逻辑运算符:select */要查找的字段 from 表名 where 条件1 逻辑运算符 条件2(例:age>18 and age<20);
 and:与;or:或;not:非(not后面的条件如果不止一个需要有小括号包裹)


模糊查询(关键字:like，%:替换任意个字符,_:替换任意一个字符):
 以指定字符开始:select * from 表名 where 字段 like '查询字符%';
 查询含有指定字符的所有数据:select * from 表名 where 字段 like '%查询字符%';
 查询含有指定字符数的数据:select * from 表名 where 字段 like '下划线个数';
 查询至少两个(或指定个数)字符数据:select * from 表名 where 字段 like '下划线个数%';


范围查询:
 in(num1,num2,num3,...):表示在一个非连续的范围内-select 数据字段 from 表名 where 条件字段 in(约束条件1,约束条件2, ....);
 not in(num1, num2, num3, ...):表示不在一个非连续的范围内-select * from 表名 where 条件字段 not in(约束条件1,约束条件2,....);
 between...and...:表示在一个连续的范围内-select * from 表名 where 条件字段 between 约束条件1(下限) and 约束条件2(上限);
 not between...and...:表示不在一个连续的范围内select * from 表名 where 条件字段 not between 约束条件1(下限) and 约束条件2(上限);


空判断:
 判断为空:select * from 表名 where 字段 is null;
 判断为非空:select * from 表名 where 字段 is not null;


排序查询:关键字:order by;asc-从小到大排列-升序(默认);desc-从大到小排序-降序；
  select * from 表名 where 条件1 and 条件2 order by 排序字段 升序-asc/降序desc;


分页查询:关键字-limit-限制查询时显示的数据量.
 不加条件:select * from 表名 limit 数据个数;
 带条件查询:select * from 表名 where 条件1,条件2,..... limit 数据个数;（limit要放在Sql语句末尾）
 分页查询:select * from 表名 limit 数据开始位置下标,查询数据数量

分组查询:关键字-group by 字段:按某一字段进行分组
 只显示分组字段信息:select 分组字段 from 表名 group by 分组字段;
 显示分组字段和其他想要看到的字段信息:(select 分组字段,group_conact(想要看到的的字段1,字段2,...(多个字段会数据显示不清晰,数据之间无间隔))
                                 from 表名 group by 分组字段;)
 having-对分组后数据进行筛选-只显示分组字段信息:select 分组字段 from 表名 group by 分组字段 having 限制条件;
 显示分组字段和其他想要看到的字段信息:(select 分组字段,group_conact(想要看到的的字段1,字段2,...(多个字段会数据显示不清晰,数据之间无间隔))
                                 from 表名 group by 分组字段 having 限制条件;)
 with rollup:对数据进行汇总-select 分组字段 from 表名 group by 分组字段 with rollup;

子查询(了解)-一次查询的结果当做另一次查询的条件.
 标量子查询:子查询返回的结果为一个数据(一行一列)；
 列子查询:返回结果是一列(一列多行);
 行子查询:返回结果为一行(一行多列)；


 连接查询-当查询结果的数据来源于多张表,需要将多张表连接成一个大的数据集进行汇总显示！！！
 mysql三种连接查询：
  1.内连接查询-查询结果为两个表符合条件匹配到的数据(交集)
   语法:select 字段 from 表1 inner join 表2 on 表1.字段1=表2.字段2
   注意：
      1）内连接:根据连接条件取出两个表的交集
      2）on是连接条件,where是连接后筛选条件
  2.外连接查询
    左连接-查询结果为两个表中匹配到的数据和左表特有的数据（两个表的交集和左表独有的数据部分）
     注意:对于右表中不存在的部分使用null填充
     语法:主表 left join 从表 on 连接条件;
    右连接-查询结果为两个表中匹配到的数据和右表特有的数据（两个表的交集和右表独有的数据部分）
     注意:对于左表中不存在的部分使用null填充
     语法:从表 right 主表 on 连接条件;
  3.自连接查询-数据在同一张表中,通过起不同的别名来达到想要的查询数据结果：
    语法:select * from 表名 as 别名1 inner join 表名 as 别名2 on 别名1.条件字段=别名2.条件字段;
"""