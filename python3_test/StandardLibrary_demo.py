#coding=utf-8
'''
Created on 2018年12月29日
@author: quqiao
'''

# Python3标准库概览

# 操作系统接口：os模块提供了不少与操作系统相关联的函数
# import os
# print(os.getcwd())  # 返回当前的工作目录
# os.chdir("C:/Users")  # 修改当前的工作目录
# os.system("mkdir test2")  # 执行系统命令 mkdir
# print(dir(os))
# print(help(os))
# 针对日常的文件和目录管理任务，shutil模块提供了一个易于使用的高级接口
import shutil
# shutil.copyfile("D:/report/test2.txt", "D:/report/test3.txt")  # 复制文件
# shutil.move("D:/report/test2.txt", "D:/Users")  # 移动文件

# 文件通配符：glob模块提供了一个函数用于目录通配符搜索中生成文件列表
# import glob
# print(glob.glob('*.py'))

# 命令行参数：
# 通用工具脚本经常调用命令行参数，这些命令行参数以链表形式存储于sys模块的argv变量
# import sys
# print(sys.argv)

# 错误输出重定向和程序终止
# sys还有stdin, stdout和stderr属性，即使在stdout被重定向时，后者也可以用于显示警告和错误信息
# import sys
# sys.stderr.write("Warning, log file not found starting a new one\n")
# 大多数脚本的定向终止都使用"sys.exit()"

# 字符串正则匹配：re模块为高级字符处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁，优化的方案
# import re
# scr = re.findall(r'\bw[a-z]*', 'which foot or hand fell fastest')
# print("findall的结果为：", scr)
# scr1 = re.sub(r'(\b[a-z]+)\1', r'\1', 'cat in the hat')
# print("sun的结果为：", scr1)
# scr2 = 'TT in the hose'.replace('in', 'into')
# print(scr2)

# 数学: math模块为浮点运算提供了对底层C函数库的访问
# import math
# m1 =math.cos(math.pi/4)
# print(m1)
# m2 = math.log(1024, 2)
# print(m2)
# random提供了生成随机数的工具
# import random
# print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(random.sample(range(100), 10))
# print(random.random())   # 随机浮点数
# print(random.randrange(20))  # 随机整数

# 访问互联网
# from urllib.request import urlopen
# for line in urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl"):
#     line = line.decode('utf-8')
#     if 'EST' in line or 'EDT' in line:
#         print(line)

# 日期和时间：datetime模块为日期和时间处理同时提供了简单和复杂的方法
# from datetime import date
# now = date.today()
# print(now)
# print(now.strftime('%m-%d-%y.%d %b %Y is a %A on the %d day of %B.'))
# birthday = date(1964, 2, 18)
# dieday = date(2017, 12, 29)
# age = dieday - birthday
# print(age.days)

# 数据压缩：
# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# unzip = zlib.decompress(t)
# print(len(unzip))

# 性能度量：
# from timeit import Timer
# import math
# t1 = Timer('stee2', 'ssss').timeit()
# t2 = Timer('ssddddddddd','123').timeit()
# print(t1)
# print(t2)

# 测试模块：doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试
# import doctest
# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#
#     return sum(values)/len(values)
# print(doctest.testmod())
# unittest模块不像doctest模块那么容易使用，不过他可以在一个独立的文件里提供一个更全面的测试集
# import unittest
# import numpy
# class TestStatisticalFunctions(unittest.TestCase):
#
#     def test_average(self):
#         self.assertEqual(numpy.average([20, 30, 70]), 40.0)
#         self.assertEqual(round(numpy.average([1, 5, 7]), 1), 4.3)
#         # self.assertRaises(ZeroDivisionError, numpy.average, [])
#         # self.assertRaises(TypeError, numpy.average, 20, 30, 70)
#
# unittest.main()
# print(numpy.average([20, 30, 70]))
