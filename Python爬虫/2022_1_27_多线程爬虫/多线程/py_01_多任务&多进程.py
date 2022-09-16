"""
多任务：在同一时间执行多个任务,例如现在的电脑安装的都是多任务操作系统
优点/目的：充分利用CPU资源,提高程序的执行效率！！！
执行方式：
1.并发执行：在一段时间内交替去执行任务(单核CPU)
 例如：
2.并行执行：多个CPU内核同一时刻一起执行任务,始终有多个软件一起执行
"""

"""
多进程-Python中实现多任务的一种方式
进程概念：一个正在"运行"的程序或者软件就是一个进程,进程是操作系统进行资源分配的基本单位
       一个程序运行后至少有一个进程,一个进程默认有一个线程,进城里面可以创建多个线程,线程是依附
       在进程里面的,没有进程就没有线程
"""

"""
多进程的使用
1.导入进程包
import multiprocessing

2.Process进程类的说明：
Process([group[,target[,name[,args[,kwargs]]]]])
 group:指定进程组,目前只能使用None
 target:执行的目标任务名-函数名
 name:进程名字
 args:以元祖方式给执行任务传参
 kwargs:以字典方式给执行任务传参
Process创建实例对象的常用方法：
 start():启动子进程实例(创建子进程)
 join():等待子进程执行结束
 termlnate():不管任务是否完成,立即终止子进程
Process创建的实力对象的常用属性：
 name:当前进程的别名,默认为Process-N,N为从1开始递增的整数
 
3.多进程使用流程：
 3.1 导入多进程模块-multiprocessing包
 3.2 创建子进程-Process类
 3.3 开启子进程-start()方法
 
4.获取进程编号
 4.1 目的:验证子进程与主进程的关系,可得知子进程是由那个主进程创建的,子进程需要主进程回收资源
 4.2 获取进程编号的两种操作
    4.2.1 获取当前进程编号
     os.getpid()可以获取当前进程编号
    4.2.2 获取当前父进程编号
     os.getppid()可以获取当前父进程的编号
"""

import multiprocessing
import time
import os


def dance(count):
    # 获取子进程ID
    print(os.getpid())
    # 获取父进程ID
    print(os.getppid())
    for i in range(count):
        time.sleep(1)
        print('跳舞...', i)


def sing(num):
    print(os.getpid())
    print(os.getppid())
    for i in range(num):
        time.sleep(1)
        print('唱歌...', i)


# if __name__ == '__main__':
#     # 单进程需要10s
#     time1 = time.time()
#     dance()
#     sing()
#     time2 = time.time()
#     print(time2 - time1)

if __name__ == '__main__':
    # 获取主进程进程编号
    main_num = os.getpid()
    print(main_num)
    # 使用多进程
    # 创建子进程
    my_dance = multiprocessing.Process(target=dance, args=(5,))  # args传参方式
    my_sing = multiprocessing.Process(target=sing, kwargs={'num': 5})  # kwargs传参方式
    time1 = time.time()
    # 开启子进程
    my_dance.start()
    my_sing.start()
    time2 = time.time()
    print(time2 - time1)
