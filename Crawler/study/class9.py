# coding=utf-8
'''
Created on 2019年04月17日
@author: quqiao
第八课：scrapy学习
'''

# Scrapy初识：使用Twisted作为框架，是事件驱动，并且比较适合异步代码。对于会阻塞线程的操作包含文件，数据库或者Web，产生
#             新的进程并需要处理新进程的输出，执行系统层次操作代码（如等待系统队列），Twisted提供了允许执行上面的操作
#             但不会阻塞代码执行的方法

# scrapy项目结构：
#       1)items.py:负责数据模型的建立，类似于实体类
#       2)middlewares.py:自己定义的中间件
#       3)pipelines.py:负责对spider返回数据的处理
#       4)settings.py:负责对整个爬虫的配置
#       5)spider目录:负责存放继承自scrapy的爬虫类
#       6)scrapy.cfg:scrapy基础配置

