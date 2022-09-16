"""
    线程是执行代码（资源）的最小单位,线程必须依附与进程存在！！！
    每个进程至少有一个线程,通常为主线程
    多线程与多进程一样可以完成多任务,线程的执行需要CPU调度来完成！！！

多线程的使用：
    1.导入模块
     import threading
    2.创建子线程
     threading.Thread(target=任务名（函数名）)
    3.开启子线程：
     Thread实例对象.start()

多线程特点：
    1.线程之间执行是无序的
    2.线程之间共享全局变量
    3.主线程会等待所有子线程执行结束再结束
    4.线程之间共享全局变量数据可能会出现错误
"""

import threading
import time


def dance():
    for i in range(5):
        print('跳舞..', i)
        time.sleep(1)


def sing():
    for i in range(5):
        print('唱歌..', i)
        time.sleep(1)


if __name__ == '__main__':
    # 创建子线程
    my_dance = threading.Thread(target=dance)
    my_sing = threading.Thread(target=sing)

    my_dance.start()
    my_sing.start()
