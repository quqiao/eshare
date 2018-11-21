#coding=utf-8
'''
Created on 2018年11月06日
@author: quqiao
'''

# 函数概念：组织好的，可重复使用的，用来实现单一或相关联功能的代码段
# 内置函数和自定义函数
# 函数规则：1.函数代码块以def关键字开头，后接函数标识符名称和圆括号()
#           2.任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数
#           3.函数的第一行语句可以选择性地使用文档字符串-----用于存放函数说明
#           4.函数内容以冒号起始，并且缩进
#           5.return[表达式]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回None

# 函数语法：
# def 函数名（参数列表）：
#       函数体


# 实例1：
# def hello():
#     print("hello,world!")
#     print("this is word")
#     a = 10+5
#     return a
# hello()

# 实例2：
# def area(width, height):
#     return width * height
# def print_welcome(name):
#     print("welcome,", name)
# print_welcome("quqiao")
#
# print("width=", 4, "height=", 5, "area=", area(4, 5))
