# coding=utf-8
'''
Created on 2019年04月12日
@author: quqiao
第八课：进程，线程的初步了解
'''

# 进程：程序并不能单独运行，只有将程序装载到内存中，系统为他分配资源才能运行，而这种执行的程序称为进程
# 程序和进程区别：程序是指令的集合，它是进程的静态描述文本。进程是程序的一次执行活动，属于动态概念

# 进程的概念：进程是操作系统对一个正在运行的程序的一种抽象。即进程是处理器，主存，IO设备的抽象，操作系统可以同时运行多个
#             进程，而每个进程都好像在毒战的使用硬件

# 并发运行：一个进程的指令和另外一个进程的指令是交错执行的

# 上下文切换：CPU看上去像是在并发的执行多个进程，这是通过处理器在进程之间切换来实现的，操作系统实现这种交错执行的机制称
#             为上下文切换


# 线程：操作系统能够进行运算跳读的最小单位，被包含在进程中，是进程中的实际运作单位
#       一个进程实际上可以由多个线程的执行单元组成，每个线程都运行在进程的上下文中，并共享同样的代码和全局数据


# 并发和并行的概念
# 并发：指的是同时具有多个活动的系统
# 并行：指的是用并发来使一个系统运行的更快，并行可以在操作系统的多个抽象层次进行运用



