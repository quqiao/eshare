#coding=utf-8
'''
Created on 2018年12月26日
@author: quqiao
'''

# open()方法
# open()函数常用形式是接收两个参数：文件名(file)和模式（mode)
# open(file, mode = "r")
# 完整语法：open(file, mode = 'r', buffering = -1, encodeing = None, newline = None, closefd = True, opener = None)
# 参数说明：file:必需，文件路径（相对或者绝对路径）
#           mode:可选，文件打开模式
#           buffering:设置缓冲
#           encoding:一般使用utf8
#           errors:报错级别
#           newline:区分换行符
#           closefd:传入的file参数类型
#           opener
# mode参数：t,文本模式（默认)
#           x,写模式，新建一个文件，如果该文件已存在则会报错
#           b,二进制模式
#           +,打开一个文件进行更新（可读可写)
#           U,通用换行模式（不推荐)

# file.close():关闭文件，关闭后文件不能再进行读写操作。close()方法允许调用多次
#              当file对象被引用到操作另外一个文件时，Python会自动关闭之前的file对象

# file.flush():刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件，而不是被动的等待输出缓冲区写入
#              一般情况下，文件关闭后会自动刷新缓冲区，但有时需要在关闭前刷新，这时就需要使用flush()方法
# f = open("D:/report/test001.txt", "r")
# print("文件名为：", f.name)
# f.flush()
# f.close()

# file.fileno():返回一个整型的文件描述符（file descriptor FD整型）,可以用在如os模块的read方法等一些底层操作上
# f = open("D:/report/test001.txt", "r")
# print("文件名为：", f.name)
# fid = f.fileno()
# print("文件描述符为：", fid)

# file.isatty():如果文件连接到一个终端设备返回True,否则返回False
# f = open("D:/report/test001.txt", "r")
# print("文件名为：", f.name)
# ret = f.isatty()
# print("返回值：", ret)

# file.next():返回文件下一行
# f = open("D:/report/test002.txt", "r")
# print("文件名为：", f.name)
# for i in range(5):
#     line = next(f)
#     print("第%d 行 - %s" % (i, line))
# f.close()

# file.truncate(size):从文件的首行首字符开始阶段，截断文件为size个字符，无size表示从当前位置截断
#                     截断之后后面的素有字符被删除，其中windows系统下的换行代表2个字符大小
# f = open("D:/report/test002.txt", "r+")
# print("文件名为：", f.name)
# line1 = f.readline()
# print("读取行：%s" %(line1))
# f.truncate(5)
# line2 = f.readlines()
# print("读取行：%s"%(line2))


# file.write():用于向文件写入指定字符串
# test = ["111", "222", "333", "444", "555"]
# f = open("D:/report/test002.txt", "w+")
# for i in test:
#     f.write(i + "\n")
# f.close()
# f = open("D:/report/test002.txt", "r+")
# print("文件名: ", f.name)
# str = "666"
# f.seek(0,2)
# line = f.write(str)
# f.seek(0,0)
# for index in range(6):
#     line = next(f)
#     print("文件号%d---%s"%(index,line))
# f.close()

# file.writelines(sequence):想文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符
# f = open("D:/report/test004.txt", "w+")
# print("文件名为：", f.name)
# seq = ["11111\n", "hhhh\n", "2222\n", "xxxxxx"]
# f.writelines(seq)
# f.close()