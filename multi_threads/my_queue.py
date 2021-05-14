# import queue
# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print ("开启线程：" + self.name)
#         process_data(self.name, self.q)
#         print ("退出线程：" + self.name)
#
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         time.sleep(1)
#         if not workQueue.empty():
#             data = q.get()  #get 在队头读取并删除队列中的元素
#             print("q队列的大小是", q.qsize())
#             queueLock.release()
#             print("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)
#
#
# threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# print("workQueue队列的大小是", workQueue.qsize())
# print("workQueue队列是否为空", workQueue.empty())
# threads = []
# threadID = 1
#
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)  #在队尾插入元素
# queueLock.release()
# print("workQueue队列的大小是", workQueue.qsize())
# print("workQueue是否已经满了", workQueue.full())
#
# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
#
# # 填充队列
#
# print("workQueue队列是否为空", workQueue.empty())
# # 等待队列清空
# while not workQueue.empty():
#     pass
# print("workQueue队列是否为空》》》》》》》》", workQueue.empty())
# # 通知线程是时候退出
# exitFlag = 1
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")

import threading
import time
import queue

class worker(threading.Thread):
    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.name = name

    def run(self):
        print(">>>>>>>>>>>>>>>>>>>启动线程")
        time.sleep(1)
        while not q.empty():
            mylock.acquire()
            data = q.get()
            mylock.release()
            print(self.name, "is deal with ", data)


def myfuc(i):
    print("this is myfuc")
    return i

if __name__ == "__main__":
    q = queue.Queue(10)
    mylock = threading.Lock()
    worker1 = worker(q, "woker1")
    worker2 = worker(q, "woker2")
    worker1.start()
    worker2.start()


    q.put(myfuc(1))  # 向队列中添加元素，产生任务消息
    q.put(myfuc(2))
    q.put(myfuc(3))
    q.put(myfuc(4))
    q.put(myfuc(5))

    print("退出主程序")


import requests