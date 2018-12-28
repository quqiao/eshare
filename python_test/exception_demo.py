#coding=utf-8
'''
Created on 2018年12月27日
@author: quqiao
'''

# 错误和异常

# 语法错误
# while True print("hello,world!")
# 前面缺少了一个冒号，语法分析器支出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头

# 异常：语法是正确的，在运行它的时候也有可能发生错误。运行期检测到的错误被称为异常
# 10*(1/0)
# 异常以不同的类型出现，这些类型都作为信息的一部分打印出来

# 异常处理
# while True:
#     try:
#         x = int(input("Please enter a number:"))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again")
# 首先执行try子句。如果没有异常发生，忽略except子句，try子句执行后结束；如果执行try子句过程中发生异常，try子句余下的
# 部分将被忽略。如果异常的类型和except之后的名称相符，对应的except子句将被执行。最后执行try语句之后的代码
# 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中

# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
# except(RuntimeError, TypeError, NameError):
#         pass

# 一个try语句可能包含多个except子句，分别来处理不同的特定的异常，最多只有一个分支会被执行
# import sys
# try:
#     f = open("D:/report/test001.txt")
#     s = f.readline()
#     i = int(s)
#     print(i)
# except OSError as err:
#     print("OS error:{0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# try except语句还有一个可选的else子句，必须放在所有的except子句之后，这个子句将在try子句没有发生任何异常时执行
# import sys
# # print(sys.argv[0])
# for arg in sys.argv[0]:
#     try:
#         f = open(arg, "r")
#     except IOError:
#         print("cannot open", arg)
#     else:
#         print(arg, "has", len(f.readlines()), "lines")
#         f.close()

# 异常处理并不仅仅处理哪些直接发生在try子句中的异常，而且还能处理子句中调用的函数里发生的异常
# def this_fail():
#     x = 1/1
# try:
#     this_fail()
# except ZeroDivisionError as err:
#     print("Handling run-time error:",err)

# 抛出异常：使用raise语句抛出一个指定的异常
# raise NameError("HiThere")
# 如果指向知道是否抛出一个异常，并不想去处理它，一个简单的raise语句就可以再次把它抛出
# try:
#     x = 1/1
# except ZeroDivisionError:
#     print("出错了")
#     raise

# 用户自定义异常：通过创建一个新的异常类来拥有自己的异常，异常类集成自Exception类，可以直接继承或者间接继承
# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)
#
# print(MyError(3*2))
# try:
#     raise MyError(3*2)
# except MyError as e:
#     print('My exception occurred, value:', e.value)
# raise MyError("oops!")

# 当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包创建一个基础异常类。然后基于这个基础类为不同错误情
# 况创建不同的子类
# class Error(Exception):
#     pass
#
# class InputError(Error):
#     def __init__(self, expression,message):
#         self.expression = expression
#         self.message = message
#
# class TransitionError(Error):
#     def __init__(self, previous, next, message):
#         self.previous = previous
#         self.next = next
#         self.message = message

# 定义清理行为
# try语句还有另外一个可选子句，他定义了无论在任何情况下都会执行的清理行为
# try:
#     raise KeyboardInterrupt
# finally:
#     print("goodbye,world!")

# 如果异常在try子句里被抛出，而又没有任何的except把他截住，那么这个异常会在finally子句执行后再次被抛出
# def divide(x, y):
#     try:
#         result = int("test")
#         print("结果为：",result)
#     except ZeroDivisionError:
#         print("division by zero!")
#     except ValueError:
#         print("not int")
#     finally:
#         print("executing finally clause")
# divide(5, 3)

# 预定义的清理行为
# 关键词with语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
# with open("") as f:
#     for line in f:
#         print(line, end="")
# 以上这段代码执行完毕后，就算在处理过程中出现问题了，文件f总是会关闭

