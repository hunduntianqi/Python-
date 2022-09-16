"""
args:以元组形式传参-args =（参数1, 参数2, ...）,若只有一个参数,则参数后必须有逗号,
kwargs:以字典形式传参-kwargs = {'形参名1' ： 值,'形参名2': 值,... },
       以字典形式传参,字典的key必须与形参名完全一致！！！
"""

import threading
import time


def dance(num1):
    for i in range(num1):
        print('跳舞..', i)
        time.sleep(1)


def sing(num2):
    for i in range(num2):
        print('唱歌..', i)
        time.sleep(1)


if __name__ == '__main__':
    # 创建子线程
    my_dance = threading.Thread(target=dance, args=(5,))  # 以元组形式传参
    my_sing = threading.Thread(target=sing, kwargs={'num2': 5})  # 以字典形式传参

    my_dance.start()
    my_sing.start()
