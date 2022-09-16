"""
主线程默认会等待子线程结束后再结束！！！
设置守护主线程-让子线程随主线程结束一起结束,不让主线程再等待子线程去执行！！
设置守护主线程两种方式：
1.threading.Thread(target=任务名, daemon=True)
2.线程对象.setDaemon(True)
"""

import threading
import time


def func():
    for _ in range(5):
        time.sleep(0.2)
        print('func')


if __name__ == '__main__':
    # 让子线程随着主线程结束而结束
    # 1.Thread(daemon=True)
    my_func = threading.Thread(target=func, daemon=True)
    # my_func = threading.Thread(target=func)
    # 2.线程对象.setDaemon(True)
    my_func.setDaemon(True)
    my_func.start()
    time.sleep(0.5)
    print('over')
    exit()
