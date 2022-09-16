"""
linux系统终端可使用命令：
1.ctrl+a:快速回到行首
2.ctrl+e:回到行末
3.ctrl+l:清屏
4.ctrl+c+回车:结束
5.ctrl+shift+“+”:放大
6.ctrl+"-":缩小

连接(登录)2022-1-16-数据库-MySql:mysql -uroot -p+密码
不显示密码：mysql -uroot -p+回车
          输入密码
退出数据库:quit/ctrl+d/exit
注意：sql语句最后需要有;结尾
显示数据库版本:select version();
显示时间:select now();
查看当前使用的数据库:select database();
查看所有数据库:show databases;
创建数据库:create database 数据库名 charset=utf8;(此项为字符集设置,如果不设置,插入中文会报错！！！)
查看创建数据库的语句(查看字符集):show create database 数据库名;
删除数据库:drop database 数据库名;
使用数据库:use 数据库名;
查询数据库用户名:select * from mysql.user;





"""