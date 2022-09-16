"""
一个进程的线程之间共享全局变量,因为同一进程的线程使用资源空间相同(同一CPU)
不同进程的线程之间无法共享全局变量
"""

import threading
import time

g_num = []


def my_write():
    global g_num

    for i in range(5):
        g_num.append(i)
    print('write:', g_num)


def my_read():
    global g_num
    print('read:', g_num)


if __name__ == '__main__':
    write = threading.Thread(target=my_write)
    read = threading.Thread(target=my_read)
    write.start()
    time.sleep(3)
    read.start()
