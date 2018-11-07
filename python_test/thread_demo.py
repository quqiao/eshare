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

import _thread
import time

# 为线程定义一个函数
def print_time(threadName):
    count = 0
    while count < 5:
        # time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", ))
    _thread.start_new_thread(print_time, ("Thread-2", ))
except:
    print("Error: 无法启动线程")

while 1:
    pass
