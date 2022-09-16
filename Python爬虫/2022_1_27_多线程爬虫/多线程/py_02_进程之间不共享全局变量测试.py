"""
多进程特点：
1.进程之间不共享全局变量-因为进程是分配资源的最小单位
 创建子进程会对主进程资源进行拷贝,子进程相当于主进程的一个副本,进程之间不共享全局变量(无论是主进程还是子进程),
 是因为操作的不是同一进程的全局变量,不同进程的全局变量名字相同而已

"""



import multiprocessing
import time

g_num = []


def my_write():
    global g_num

    for i in range(5):
        g_num.append(i)
    print(g_num)


def my_read():
    global g_num
    print(g_num)


if __name__ == '__main__':
    write = multiprocessing.Process(target=my_write)
    read = multiprocessing.Process(target=my_read)
    write.start()
    time.sleep(3)
    read.start()
