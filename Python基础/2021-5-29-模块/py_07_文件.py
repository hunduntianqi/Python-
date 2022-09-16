"""
文件的概念
1.计算机的文件,就是储存在某种长期储存设备上的一段数据
2.长期储存设备包括：硬盘,U盘,移动硬盘,光盘等...
3.文件的作用：将数据长期保存下来,在需要的时候使用

文件的储存方式--在计算机中,文件以二进制的方式保存在磁盘上

文本文件和二进制文件
1.文本文件
 1.1 可以使用文本编辑软件查看
 1.2 本质上还是二进制文件
 1.3 例如:python的源程序
2.二进制文件
 2.1 保存的内容不是给人直接阅读的,而是提供给其他软件使用的
 2.2 例如：图片,音频,视频等
 2.3 二进制文件不能使用文本编辑软件查看

"""

"""
文件基本操作：
1.操作文件的套路：
 1.1 打开文件
 1.2 读、写文件
  1.2.1 读：将文件内容读入内存
  1.2.2 写：将内存内容写入文件
 1.3 关闭文件
2.操作文件的函数/方法--一个函数,三个方法：
 2.1 open函数：打开文件,并且返回文件操作对象
 2.2 read方法：将文件内容读取到内存
 2.3 write：将指定内容写入文件
 2.4 close：关闭文件
 2.5 read/write/close三个方法都要通过文件对象来调用
"""
"""
read方法--读取文件
1.open函数的第一个参数为要打开的文件名（文件路径,文件名称区分大小写）
 1.1 如果文件存在,返回文件操作对象
 1.2 如果文件不存在,会抛出异常
2.read方法可以一次性读入并返回文件的所有内容
3.close方法负责关闭文件,不关闭文件会造成系统资源消耗,并影响后续对文件的访问
在开发中,通常会先编写打开和关闭的代码,在编写中间针对文件的读/写操作！！！
注意：read方法执行后会把文件指针移动到文件末尾,再次调用read方法读取不到任何内容
"""

"""
打开文件方式：
open函数默认以只读方式打开文件,并且返回文件对象
语法如下：
open('文件名称（文件路径）', '文件打开方式r/w/a', encoding = '编码方式')
访问方式：
1.r:以只读方式打开文件,文件指针会放在文件的开头,默认模式,文件不存在会抛出异常
2.w:以只写方式打开文件,文件存在会被覆盖,不存在会新建文件
3.a:以追加方式打开文件,如果文件已存在,会把指针放在文件末尾,如果文件不存在,会创建新文件写入数据
4.r+:以读写方式打开文件,其余同r
5.w+:以读写方式打开文件,其余同w
6.a+:以读写方式打开文件,其余同a
7.rb/wb/ab:二进制只读/只写/追加,其余同r/w/a
8.rb+/wb+/ab+:二进制读写,其余同r/w/a
"""
"""
readline方法读取大文件：
read方法会一次性将文件所有内容读取到内存中,文件太大时,会占用内存
readline方法可以一次读取一行内容,读取后,会把指针移动到下一行,可以再次读取下一行内容
"""

"""
os模块常用方法：
1.listdir：返回文件夹内所有文件名称的列表,os.listdir(文件夹路径)
2.mkdir：创建文件夹,os.mkdir(创建文件夹的位置路径)
3.rmdir：删除文件夹,os.rmdir(要删除文件夹的路径)
4.getcwd：获取当前目录,os.getcwd()
5.chdir:修改当前目录,os.chdir()
6.path.isdir:判断是否是文件,os.path.isdir(文件路径)
"""
# file = open(r'D:\Users\Administrator\Desktop\test\新建文本文档.txt', 'r', encoding='utf-8')
# m = file.read()
# n = file.read()
# # print(m)
# print(n)
# file.close()
#
# import os
# print(os.getcwd())
# os.chdir(r'D:\Users\Administrator\Desktop\test')
# print(os.getcwd())
# #
# # print(dir(os))
# picture = os.listdir(r'D:\Users\Administrator\Desktop\test\图片备份')
# print(len(picture))
# os.mkdir(r'D:\Users\Administrator\Desktop\picture')
# for pic in picture:
#     pic_file1 = open(r'D:\Users\Administrator\Desktop\test\图片备份\{}'.format(pic), 'rb')
#     pic_file2 = open(r'D:\Users\Administrator\Desktop\picture\{}'.format(pic),'wb')
#     pic_file2.write(pic_file1.read())
#     pic_file2.close()
#     pic_file1.close()
#     print(pic)

source_file = open(r'D:\Users\Administrator\Desktop\test\蒋大为 - 最美的歌儿唱给妈妈.MP3', 'rb')
result_file = open(r'D:\Users\Administrator\Desktop\蒋大为 - 最美的歌儿唱给妈妈.MP3', 'ab')
while True:
    source_music = source_file.readline()
    result_file.write(source_music)
    print(source_music)
    if not source_music:
        break

source_file.close()
result_file.close()
