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
# print_welcome("quqiao")`
#
# print("width=", 4, "height=", 5, "area=", area(4, 5))


# 函数调用
# def printme(str):
#     a = print(str)
#     # b = print("11111")
#     return a
# printme("123456789")
# printme("asdqwerttyy")

# 参数传递
# Python中，类型属于对象，变量是没有类型的
# 可更改对象：list,dict
# 不可更改对象：strings,tuples,numbers
# 传不可变对象实例
# def ChangeInt(a):
#     a = "string"
#     return a
# ChangeInt("string2")
# print(ChangeInt("string2"))

# 传可变对象实例
# def changeme(mylist):
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值：", mylist)
#     return
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值：", mylist)

# 参数
# 必须参数：须以正确的顺序传入函数，调用时的数量必须和声明时的一样
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
# printme("12345678902")

# 关键字参数：和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
# def printinfo(name, age):
#     print("名字：", name)
#     print("年龄：", age)
#     return
# printinfo(name="张三", age=10)

# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数
# def printinfo(name="张三", age=20):
#     print("名字：", name)
#     print("年龄：", age)
#     return
# printinfo(age=10, name="李四")
# print("-----------------")
# printinfo(name="王五")

# 不定长参数 *vartuple是输出元组
# def printinfo(arg1, *vartuple):
#     print("输出：")
#     print(arg1)
#     print(vartuple)
# printinfo(1,2,3,4,5,6,7,8,9)

# **vardict的参数会以字典的形式导入
# def printinfo(arg1, **ad):
#     print("输出：")
#     print(arg1)
#     print(ad)
# printinfo(1, b=2, c=3, d=4, e=5)

# 声明函数时，参数中星号*可以单独出现，出现后，*后的参数必须用关键字传入
# def info(a,b,*,c):
#     return a+b+c
# print(info(1,2,c=3))

# 匿名函数：lambda函数体比def简单，
#           主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
#           拥有自己的命名空间，且不能访问自己参数列表以外的或全局命名空间里的参数
# flu = lambda arg1, arg2: arg1+arg2
# print("相加后的值为：", flu(1, 1))
# print("相加后的值为：", flu(10, 20))

# return语句: 用于退出函数，选择性地向调用方返回一个表达式，不带参数值的return语句返回None
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("函数内：",total)
#     return total
# total = sum(10,20)
# print("函数外：", total)

# 变量作用域
# python作用域：1.local局部作用域 2.Enclosing闭包函数外的函数中 3.Global全局作用域 4.Built-in内建作用域
# x = int(2.9)  # 内建作用域
# g_count = 0  # 全局作用域
# def outer():
#     o_count = 1  # 闭包函数外的函数中
#     def inner():
#         i_count = 2  # 局部作用域

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，局部变量只能在其被声明的函数内部访问
# 定义在函数外的拥有全局作用域，全局变量可以在整个程序范围内访问
# 调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
# total = 0
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("函数内是局部变量：", total)
#     return total
# sum(10, 20)
# print("函数外是全局变量", total)

# global和nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，需要用到global和nonlocal关键字
# num = 1
# def fun1():
#     global num
#     print("第一个打印：", num)e
#     num = 123
#     print("第二个打印：", num)
# fun1()
# print("第三个打印：", num)

# nonlocal关键字使用
# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         print("第一个输出：", num)
#         num = 100
#         print("第二个输出：", num)
#     inner()
#     print("第三个输出：", num)
# outer()

# a = 10
# def test():
#     a = 3 + 1
#     print(a)
# test()



