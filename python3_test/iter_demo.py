#coding=utf-8
'''
Created on 2018年12月07日
@author: quqiao
'''

import sys

# 迭代是Python最强大的功能之一，是访问集合的一种方式
# 迭代器是一个可以记住遍历的位置的对象
# 迭代器对想从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
# 迭代器有两个基本的方法：iter()和next().
# 字符串,列表或元祖对象都可用于创建迭代器

# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
# # for x in it:
# #     print(x, end="")
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# 创建一个迭代器
# 把一个类作为一个迭代器使用，需要在类中实现两个方法__iter__()与__next__()
# __iter__()方法返回一个特殊的迭代器对象,这个迭代器对象实现了__next__()方法并通过Stopiterration异常标识迭代的完成
# __next__()方法会返回下一个迭代器对象
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# StopIteration
# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a < 5:
#             x = self.a
#             self.a +=1
#             return x
#         else:
#             raise StopIteration
# myclass = MyNumber()
# myiter = iter(myclass)
# for x in myiter:
#     print(x)

# 生成器
# 使用了yield的函数被称为生成器（generator）
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单的理解生成器就是一个迭代器
# 调用一个生成器函数，返回的是一个迭代器对象
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield counter
#         a, b = b, a+b
#         counter +=1
# f = fibonacci(10)  # f是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

import sys

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        # yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except :
        sys.exit()