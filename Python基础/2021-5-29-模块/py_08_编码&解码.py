"""
编码：'你想编码的内容'.encode('你使用的编码表')
解码：'你想解码的内容'.decode('你使用的编码表')
四种编码表：
1.ASCII码：适用英文大小写,字符,不支持中文,是美国人的发明,占用空间小,python2.x默认编码方式
2.GB2312,GBK码：支持中文,GBK码是GB2312的升级版
3.Unicode码：支持国际语言,占用空间大,适用性强
4.UTF-8码：支持国际语言,是Unicode码的升级,两者可以非常容易的互相转化,占用空间小,ASCII码被UTF-8码包含,python3.x默认编码方式
在python2.x中使用中文的两种方法：
1.在python2.x文件的第一行增加代码：# *-* coding:utf-8 *-*
2.在python2.x文件的第一行增加代码：# coding=utf-8
"""
print('郭鹏涛'.encode('Utf-8'))
print(b'\xe9\x83\xad\xe9\xb9\x8f\xe6\xb6\x9b'.decode('Utf-8'))