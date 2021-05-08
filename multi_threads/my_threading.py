#!/usr/bin/python3

import threading
import time

exitFlag = 0


class MyThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        "用以表示线程活动的方法"
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()  # start(),启动线程活动
thread1.join()  #阻塞其他线程，直至thread1.start() 执行结束，也就是说thread2以及最后的print要等thread1执行结束
thread2.start()
thread2.join()
print (">>>>>>>>>>>>>>>>>>>>>>>>>退出主线程")