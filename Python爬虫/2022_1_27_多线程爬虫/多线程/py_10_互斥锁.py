"""
解决线程共享全局变量两种方式
1.线程等待(非主要使用)：
 线程对象.join()-让主线程执行完该线程任务,再继续向下执行！！！
2.互斥锁：
 对共享数据进行锁定,保证同一时刻只能由一个线程去操作
 互斥锁是多个线程一起去抢一个共享数据,抢到锁的线程先执行,其他线程需要等待,等到互斥锁使用完释放数据后,其他线程再去抢这个锁！！！
 2.1 互斥锁的使用：threading模块定义了Lock变量,此变量本质为一个函数,调用此函数可以获取一把互斥锁
  使用步骤：
   2.1.1 创建锁：mutex = threading.Lock()
   2.1.2 上锁：mutex.acquire()
   2.1.3 释放锁：mutex = release()
 2.2 注意点：
  2.2.1 acquire()和release()之间的代码同一时刻只能有一个线程操作
  2.2.2 如果在调用acquire方法时,其他线程已经使用互斥锁,acquire方法会被堵塞,直到互斥锁释放后才能再次上锁！！！
"""

import threading

g_num = 0
# 创建互斥锁
mutex = threading.Lock()


def sum_num1():
    global g_num

    # 上锁
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    # 释放锁(不解锁会出现死锁问题...)
    mutex.release()
    print('sum_num1', g_num)


def sum_num2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print('sum_num2:', g_num)


if __name__ == '__main__':
    sum1 = threading.Thread(target=sum_num1)
    sum2 = threading.Thread(target=sum_num2)

    sum2.start()
    sum1.start()
    # sum1.join()  # 等待sum1线程执行完再执行sum2线程

