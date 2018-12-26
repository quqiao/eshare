#coding=utf-8
'''
Created on 2018年12月18日
@author: quqiao
'''

# Python两种输出值的方式：表达式语句和print()函数
# 第三种方式是使用问价对象的write()方法，标准输出文件可以用sys.stdout引用
# str()：函数返回一个用户易读的表达形式
# repr()：产生一个解释器易读的表达形式
# s = "hello,world!"
# print(str(s))
# print(repr(s))
# print(str(1/7))
# 输入平方和立方表,rjust()方法,将字符串靠右并在左边填充空格
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")
#     print(repr(x*x*x).rjust(5))
# for x in range(1, 11):
#     print('{0:2d}{1:5d}{2:8d}'.format(x, x*x, x*x*x))
# zfill()方法，会在数字的左边填充0
# print("test".zfill(10))

# str.format()的基本使用：括号及其里面的字符（称作格式化字段)将会被format()中的参数替换
#                         括号中的数字用于指向传入对象在format()中的位置
# print('{1}网址："{0}!"'.format("菜鸟教程", "www.runoob.com"))
# format()中使用了关键字参数，他们的值会指向使用该名字的参数
# print('{name}网址：{site}'.format(name="菜鸟教程", site='www.baidu.com'))
# 位置及关键字参数可以任意的结合
# print('站点列表{0},{1},和{other}.'.format("ttt", "eee", other="111"))
# '!a'使用ascii(),'!s'使用str(),'!r'使用repr()
# import math
# print('常量PI的值近似为：{}'.format(math.pi))
# print('常量PI的值近似为：{!s}'.format(math.pi))
# ':'和格式标识符可以跟着字段名。这就允许对值进行更好的格式化
# import math
# print('常量PI的值近似为：{0:.3f}'.format(math.pi))
# 在':'后传入一个整数,可以保证该域至少有这么多的宽度，用于美化表格时很有用
# table = {"google": 1, "baidu": 2, "sina": 3}
# for name, number in table.items():
#     print("{0:10}==>{1:10d}".format(name, number))

# 旧式字符串格式化:%操作符也可以实现字符串格式化
# import math
# print("常量PI的值近似为：%5.3f。" % math.pi)

# 读取键盘输入：input()内置函数从标准输入读入一行文本，默认的标准输入是键盘
#               input可以接收一个Python表达式作为输入，并将运算结果返回
# str = input("请输入：")
# print("你输入的是:", str)

# 读和写文件
# open()将会返回一个file对象
# open(filename, mode)
# filename,包含了你要访问的文件名称的字符串值
# mode,决定了打开文件的模式：只读,写入，追加等
# r    以只读方式打开文件。文件的指针将会放在文件的开头
# rb   以二进制格式打开一个文件用于只读。文件指针将放在文件的开头
# r+   打开一个文件用于读写。文件指针将会放在文件的开头ww
# rb+  以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头
# w    打开一个文件只用于写入。文件存在会重新写入，删除原有内容；不存在创建新文件
# wb   以二进制格式打开一个文件只用于写入。存在重新写入并删除原有内容；不存在创建新文件
# w+   打开一个文件用于读写。存在重写写入并删除原有内容；不存在创建新文件
# a    打开一个文件用于追加。该文件存在，文件指针将会放在文件结尾。如果该文件不存在，创建新文件进行写入
# ab   以二进制格式打开一个文件用于追加。如果文件存在，文件指针将会放在文件的结尾。文件不存在，创建文件进行写入
# a+   打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件不存在，创建新文件用于读写
# ab+  以二进制格式打开一个文件用于追加。文件存在，文件指针将会放在文件的结尾。文件不存在，创建新文件用于读写
# f = open("D:/report/test.txt", "a+")
# f.write("很好很好\n testtest \n")
# f.close()

# 文件对象的方法
# f.read(),为了读取一个文件的内容，调用f.read(size),这将读取一定数目的数据，然后作为字符串或者字节对象返回
# size是可选的数字类型参数.当size被忽略或者为负，那么该文件的所有内容都将被读取并返回
# f = open("D:/report/test.txt", "r")
# print(f.read(-1))
# f.close()

# f.readline():会从文件中读取单独的一行。换行符为"\n"。f.readline()如果返回一个空字符串，说明已经读取到最后一行
# f = open("D:/report/test.txt", "r")
# print(f.readline())
# print(f.readline())
# f.close()

# f.readlines():将返回该文件中包含的所有行
# f = open("D:/report/test.txt", "r")
# # print(f.readlines())
# # print(f.readlines())
# for line in f:
#     print(line, end="")
# f.close()

# f.write():f.write(string)将string写入到文件中，返回写入的字符数
# f = open("D:/report/test001.txt", "w")
# value = ("1234567890")
# test = str(value)
# print(f.write(test))
# f.close()

# f.tell():返回文件对象当前所处的位置，它是从文件开头开始算起的字节数
# f = open("D:/report/test001.txt", "a+")
# f.write("123456789")
# print(f.tell())
# f.close()

# f.seek():如果要改变文件当前的位置，可以使用f.seek(offset,from_what)函数
# from_what的值，如果是0表示开头，如果是1表示当前位置，2表示文件的结尾
# seek(x,0):从起始位置即文件首行首字符开始移动x个字符
# seek(x,1):表示从当前位置往后移动x个字符让
# seek(x,2):表示从文件的结尾往前移动x个字符
# from_what值默认为0，即文件开头
# f = open("D:/report/test001.txt", "wb+")
# f.write(b"1234567890test")
# print(f.seek(-3, 2))
# print(f.read(1))
# f.close()

# f.close():在文本文件中（哪些打开文件模式下没有b的）,只会相对于文件起始位置进行定位
# 处理完一个文件后，调用f.close()来关闭文件并释放系统的资源,如果尝试再调用该文件则会抛出异常
# 使用with关键字
# with open("D:/report/test001.txt", "r") as f:
#     read_data = f.read()
#     print(read_data)
# f.closed

# pickle模块:实现了基本的数据序列和反序列化
# 序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储
# 反序列化操作，我们能够从文件中创建上一次程序保存的对象
# import pickle, pprint
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
# # print(x)
# output = open("data.pkl", "wb+")
# pickle.dump(data1, output)
# pickle.dump(selfref_list, output, -1)
# output.close()
#
# pkl_file = open("C:/Users/Administrator/PycharmProjects/eshare/python_test/data.pkl", "rb")
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
# print(data1)
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
# print(data2)
# pkl_file.close()


