#coding=utf-8
'''
Created on 2018年11月06日
@author: quqiao
'''

# 多线程：同时执行多个不同程序
# Python3 线程模块（_thread,  threading)
# 线程分类：
# 内核线程：由操作系统内核创建和撤销
# 用户线程：不需要内核支持而在用户程序中实现的过程
# 使用线程方式：函数或者用类来包装线程对象


# 函数式
# 调用_thread模块开启新线程，_thread.start_new_thread(function,args[,kwargs])
# function---线程函数
# args---传递给线程函数的参数，必须是个tuple类型
# kwargs---可选参数
# import _thread
# import time
# 为线程定义一个函数
# def print_time(threadName,delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s" % (threadName, time.ctime(time.time())))
# 创建两个线程
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2))
#     _thread.start_new_thread(print_time, ("Thread-2", 1))
# except:
#     print("Error: 无法启动线程")
# while 1:
#     pass

# 线程模块
# threading.currentThread():返回当前的线程变量
# threading.enumerate():返回一个包含正在运行的线程list.正在运行指线程启动后，结束前，不包括启动前和终止后的线程
# threading.activeCount():返回正在运行的线程数量，与len(threading.enumerate())有相同的结果
# run():用以表示线程活动的方法
# start():启动线程活动
# join([time]):等待至线程中止
# isAlive():返回线程是否活动的
# getName():返回线程名
# setName():设置线程名

# 使用threading模块创建线程
# import threading
# import time
# exitFlag = 0
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print("退出线程：" + self.name)
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
# print(thread1.isAlive())
# thread1.start()
# thread2.start()
# print(thread1.isAlive())
# thread1.join()
# thread2.join()
# print(thread1.isAlive())
# print("退出主线程")

# 线程同步
# import threading
# import time
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print("开启线程：" + self.name)
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         threadLock.release()
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("%s:%s" % (threadName, time.ctime(time.time())))
#         counter -= 1
# threadLock = threading.Lock()
# threads = []
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
# # 开启新线程
# thread1.start()
# thread2.start()
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print("退出主线程")

# 线程优先级队列（Queue):提供了同步的，线程安全的队列类
# 包括FIFO（先入先出）Queue,LIFO(后入先出）队列LifoQueue,优先级队列PriorityQueue
import queue
import threading
import time
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("开启线程："+ self.name)
        process_data(self.name, self.q)
        print("关闭线程："+ self.name)
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID =1
# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()
# 等待队列清空
while not workQueue.empty():
    pass
# 通知线程是时候退出
exitFlag = 1
# 等待所有线程完成
for t in threads:
    t.join()
print("退出线程")





