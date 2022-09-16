"""
聚合函数:
 又叫组函数,通常是对数据表中的数据进行统计和计算,一般结合分组(group by)来使用,用于统计和计算分组数据.
 常用聚合函数:
  count(col):求指定字段的总行数-select count(字段或*) from test where 约束条件(可以没有);
  max(col):求指定字段的最大值-select max(字段或*) from test where 约束条件(可以没有);
  min(col):求指定字段的最小值-select min(字段或*) from test where 约束条件(可以没有);
  sum(col):求指定字段的和-select sum(字段或*) from test where 约束条件(可以没有);
  avg(col):求指定字段的平均值-select avg(字段或*) from test where 约束条件(可以没有);
  round(col):保留指定位数的小数-select round(数字表达式,保留小数位数) from test where 约束条件(可以没有);



"""