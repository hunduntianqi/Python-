"""
主进程默认会等待子进程结束后再结束！！！
设置守护主进程-让子进程随主进程结束一起结束,不让主进程再等待子进程去执行！！
两种方式：
 1. 设置守护主进程方式：子进程对象.daemon = True
  该方式需要再开启子进程（start方法执行）之前设置,否则无效！！！
 2. 销毁子进程方式:子进程对象.terminate()

"""

import multiprocessing
import time


def func():
    for i in range(5):
        time.sleep(0.2)
        print('func')


if __name__ == '__main__':
    # (注意点)主进程会等待子进程结束之后再结束
    # 程序运行就会默认创建主进程！！

    my_func = multiprocessing.Process(target=func)  # 主进程创建子进程

    # my_func.daemon = True  # 设置守护主进程,需要再开启子进程之前设置！！！

    my_func.start()  # 主进程开启子进程

    time.sleep(0.5)
    # 手动设置结束子进程！！
    my_func.terminate()
    print('主进程结束！！')
    exit()
