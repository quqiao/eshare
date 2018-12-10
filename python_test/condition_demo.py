#coding=utf-8
'''
Created on 2018年12月10日
@author: quqiao
'''

# Python条件语句是通过一条或者多条语句的执行结果（True或者False）来决定执行的代码块
# Python中用elif代替else if,所以if语句的关键字为：if-elif-else
# 注意点：1.每个条件后面要使用冒号:,表示接下来是满足条件后要执行的语句块
#         2.使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块
#         3.在Python中没有switch-case语句

# 简单的if实例
# var1 = 100
# if var1:
#     print("1 - if 表达式条件为 true")
#     print(var1)
# var2 = 0
# if var2:
#     print("2 - if 表达式条件为 true")
#     print(var2)
# print("Good bye!")


# 计算判断
# age = int(input("请输入你家狗狗的年龄："))
# print("")
# if age < 0:
#     print("逗比！")
# elif age ==1:
#     print("相当于14岁的人。")
# elif age ==2:
#     print("相当于22岁的人。")
# elif age >2:
#     human = 22 + (age - 2)*5
#     print("对应人类年龄：", human)
# ### 退出提示
# input("点击enter键退出")

# 猜字游戏
# number = 7
# guess = -1
# print("数字猜谜游戏！")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#     if guess ==number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了。。。")
#     elif guess > number:
#         print("猜的数字大了。。。")

# if嵌套
# num = int(input("输入一个数字:"))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print("1你输入的数字可以整除2和3")
#     else:
#         print("2你输入的数字可以整除2,但不能整除3")
# else:
#     if num % 3 == 0:
#         print("3你输入的数字可以整除3，但不能整除2")
#     else:
#         print("4你输入的数字不能整除2和3")

# i = 0
# a = 1
# while a != 20:
#     a = int(input("请输入数字："))
#     i += 1
#     if i < 3:
#         if a == 20:
#             if i < 3:
#                 print("哇，那么快就猜中了呀！")
#             else:
#                 print("你终于猜中了")
#         if a < 20:
#             print("小了！！！！！")
#         if a > 20:
#             print("大了！！！！")
#     else:
#         print("你已经没有机会了")
#         break





