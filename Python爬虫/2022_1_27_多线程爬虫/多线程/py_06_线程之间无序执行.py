import threading
import time


def func():
    time.sleep(1)
    print(threading.current_thread(), end='\n')


if __name__ == '__main__':
    # 循环创建5个线程,无序执行('线程1未执行,之后的线程也会执行！！！')
    for _ in range(5):
        my_func = threading.Thread(target=func)
        my_func.start()
