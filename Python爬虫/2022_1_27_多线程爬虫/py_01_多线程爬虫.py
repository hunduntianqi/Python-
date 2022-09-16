"""
    多进程使用场景:
        CPU密集的程序, 可充分利用计算机的多核
    多线程应用场景:
        IO操作多的程序适合使用多线程, 包括网络IO, 本地磁盘IO
        爬虫发请求等响应:网络IO
        爬虫处理所抓数据:本地磁盘IO
            使用多线程编写爬虫能够极大提升数据抓取的效率
    队列模块-queue:
        导入模块:
            from queue import Queue
        常用方法:
            创建队列: q = Queue()
            入队列: q.put()
            出队列: q.get() 注意, 默认情况下, 该方法block参数默认值为True 当队列为空时, 再次从队列中取出数据会造成系统阻塞
                    解除阻塞:
                        方法一: block参数设置为False
                        方法二: 设置超时时间-q.get(block=True, timeout=超时时间)
                        方法三: 调用get()方法前先判断队列是否为空, 不为空再调用方法
            判断队列是否为空: q.empty(), 空返回True, 非空返回False
    多线程模块-threading模块:
        导入线程类:
            from threading import Thread
        使用流程:
            t = Thread(target=事件函数名)-创建子线程
            t.start()-开启子线程
            t.join()-线程等待
    线程锁:
        导入线程锁:
            from threading import Lock
        加锁场景:
            当多个线程操作同一个共享资源时
        常用方法:
            创建锁: lock = Lock()
            上锁: lock.acquire()
            释放锁: lock.release()
            注意:上锁成功后, 未释放锁之前, 再次上锁会阻塞
"""