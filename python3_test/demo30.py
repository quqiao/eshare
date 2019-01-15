#coding=utf-8
'''
Created on 2018年12月05日
@author: quqiao
'''

# demo1:数字求和
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
# total = num1 + num2
# print("他们的和是：",total)

# demo2:平方根
# num = float(input("请输入一个数字："))
# num_sqrt = num ** 0.5
# print("%0.1f的平方根为%0.1f" % (num, num_sqrt))

# demo3:二次方程
# import cmath
# a = float(input("输入a:"))
# b = float(input("输入b:"))
# c = float(input("输入c:"))
# d = (b**2) - (4*a*c)
# print("d的结果为：", d)
# print("d的平方根为：", cmath.sqrt(d))

# demo4:计算三角形面积
# a = float(input('输入三角形第一边长：'))
# b = float(input('输入三角形第二边长：'))
# c = float(input('输入三角形第三边长：'))
# s = (a + b + c)/2
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print("面积为：%0.1f" % area)

# demo5:随机数生成
# import random
# i = 1
# a = random.randint(1, 100)
# b = int(input("请输入一个整数数字："))
# while a != b:
#     if a > b:
#         print("你输入的数字太小了")
#         b = int(input("请再输入一次"))
#     else:
#         print("你输入的数字太大了")
#         b = int(input("请再输入一次"))
#         i += 1
# else:
#     print("恭喜你! 猜对了！！！，你猜测%d次后，终于与电脑的数字%d一致了"% (i, b))

# demo6:摄氏温度转华氏温度
# celsius = float(input("输入摄氏度温度："))
# fahrenheit = (celsius * 1.8) + 32
# print("%0.1f摄氏度转为华氏摄氏度为：%0.1f"%(celsius, fahrenheit))

# demo7:交换变量
# x = input('输入x值：')
# y = input('输入y值：')
# # temp = x
# # x = y
# # y = temp
# x,y = y, x
# print("交换后x的值为：{}".format(x))
# print("交换后y的值为：{}".format(y))

# demo8:if语句
# num = float(input("请输入一个数字："))
# # if num > 0:
# #     print("这是一个正数！！！！")
# # elif num == 0:
# #     print("该数为零！！！！")
# # else:
# #     print("该数为负数！！！！")
# if num >= 0:
#     if num >0:
#         print("正数")
#     else:
#         print("零")
# else:
#     print("负数")

# demo9:判断字符串是否为数字
# import unicodedata
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#     try:
#         unicodedata.numeric(s)
#         return TypeError
#     except(TypeError,ValueError):
#         pass
#     return False
# print(is_number("sssss"))

# demo10:判断奇数偶数
# num = int(input("请输入一个数字："))
# if (num%2)==0:
#     print("{}数字为偶数！！！！".format(num))
# else:
#     print("{}该数字为奇数！！！！".format(num))

# demo11:判断闰年
# year = int(input("请输入一个年份："))
# if (year%4) == 0:
#     if(year%100) ==0:
#         if(year%400) == 0:
#             print("{}年是闰年".format(year))
#         else:
#             print("{}年不是闰年".format(year))
#     else:
#         print("{}年是闰年".format(year))
# else:
#     print("{}年不是闰年".format(year))

# demo12:质数判断
# num = int(input("请输入一个数字："))
# if num > 1:
#     for i in range(2,num):
#         if(num%i) == 0:
#             print(num,"不是质数")
#             print(i,"乘以",num//i,"是",num)
#             break
#     else:
#         print("该数字是质数！！！")
# else:
#     print("该数字是质数！！！")

# demo13:输出指定范围内的素数
# s1 = int(input("请输入第一个数："))
# s2 = int(input("请输入第二个数："))
# for num in range(s1,s2+1):
#     if num > 1:
#         for i in range(2, num):
#             if (num%i) == 0:
#                 break
#         else:
#             print(num)

# demo14:阶乘实例
# num = int(input("请输入一个数字："))
# factorial = 1
# if num < 0:
#     print("抱歉，负数没有阶乘")
# elif num == 0:
#     print("0 的阶乘为1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial*i
#     print("%d 的阶乘为%d"%(num,factorial))

# demo15:九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}*{}={}\t'.format(j, i, i*j), end = "")
#     print()

# demo16:斐波那契数列
# nterms = int(input("你需要几项？"))
# n1 = 0
# n2 = 1
# count = 2
# if nterms <= 0:
#     print("请输入一个正整数。")
# elif nterms == 1:
#     print("斐波那契数列：",n1)
# else:
#     print("斐波那契数列：",n1,",",n2,end=" , ")
#     while count < nterms:
#         nth = n1 + n2
#         print(nth, end=" , ")
#         n1 = n2
#         n2 = nth
#         count += 1

# demo17:阿姆斯特朗数
# num = int(input("请输入一个数字："))
# sum = 0
# n = len(str(num))
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** n
#     temp //= 10
# if num == sum:
#     print("%d为阿姆斯特朗数" % num)
# else:
#     print("%d不是阿姆斯特朗数" % num)

# demo18:十进制转二进制，八进制，十六进制
# dec = int(input("请输入一个整数："))
# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))

# demo19:ASCII码与字符相互转换
# c = input("请输入一个字符：")
# a = int(input("请输入一个ASCII码："))
# print(c +"的ASCII码为", ord(c))
# print(a, "对应的字符为", chr(a))

# demo20:最大公约数算法
# def hcf(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if((x % i == 0)and(y % i == 0)):
#             hcf = i
#     return hcf
# num1 = int(input("输入第一个数字："))
# num2 = int(input("输入第二个数字："))
# print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))

# demo21:最小公倍数算法
# def lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while(True):
#         if((greater % x == 0) and (greater % y ==0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
# num1 = int(input("输入第一个数字："))
# num2 = int(input("输入第二个数字："))
# print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))

# demo22:简单计算器实现
# def add(x, y):
#     return x+y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x*y
# def divide(x, y):
#     return x/y
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
# print("选择运算：1.相加，2相减，3.相乘，4.相除")
# choice = input("请输入你的运算1/2/3/4/：")
# if choice == "1":
#     print(num1, "+", num2, "=", add(num1, num2))
# elif choice == "2":
#     print(num1, "+", num2, "=", subtract(num1, num2))
# elif choice == "3":
#     print(num1, "+", num2, "=", multiply(num1, num2))
# elif choice == "4":
#     print(num1, "+", num2, "=", divide(num1, num2))
# else:
#     print("暂时没有该运算")

# demo23:python生成日历
# import calendar
# yy = int(input("输入年份："))
# mm = int(input("输入月份："))
# print(calendar.month(yy, mm))

# demo24:使用递归斐波那契数列
# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return(recur_fibo(n - 1) + recur_fibo(n-1))
# nterms = int(input("你要输出几项？"))
# if nterms <= 0:
#     print("输入整数")
# else:
#     print("斐波那契数列：")
#     for i in range(nterms):
#         print(recur_fibo(i))

# demo25:字符串判断
# print("测试实例一")
# str = "sssstttt2222"
# print(str.isalnum())  # 所有都是数字或者字母
# print(str.isalpha())  # 所有字符为字母
# print(str.isdigit())  # 所有字符为数字
# print(str.islower())  # 所有字符都是小写
# print(str.isupper())  # 所有字符都是大写
# print(str.istitle())  # 所有单词首字母大写
# print(str.isspace())  # 所有字符都是空白字符
# print(str.upper())  # 所有字符中小写转换成大写字母
# print(str.lower())  # 所有字符中大写转换成小写字母
# print(str.capitalize())  # 把第一个字母转化为大写字母，其余小写
# print(str.title)  # 把每个单词的第一个字母转化为大写，其余小写

# demo26:计算每个月天数
# import calendar
# monthRange = calendar.monthrange(2019, 1)
# print(monthRange)

# demo27:获取昨天日期
# import datetime
# def getYesterday():
#     today = datetime.date.today()
#     oneday = datetime.timedelta(days = 1)
#     yesterday = today - oneday
#     return yesterday
# print(getYesterday())

# demo28:list常用操作
list1 = ["11", "22", "33", "44", "55", "66", "77"]
# 索引
# print(list1)
# print(list1[1])
# print(list1[1:3])
# print(list1[1:-3])
# print(list1[-3, -1])  # 错误
# print(list1[:3])
# print(list1[3:])
# 增加元素
# list1.append("88")
# list1.insert(2, "test")
# list1.extend(["zhutou", "zhuzhu"])
# print(list1)
# list搜索
# print(list1.index("22"))
# list删除元素,如果有重复的值，删除首次出现的一个值
# list1.remove("22")
# list1.pop()
# print(list1)
# list运算符
# list1 = list1 + ["88", "99"]
# list1 += ["888", "999"]
# list1 = list1 * 2
# print(list1)
# 使用join链接list成为字符串
# str = ";".join(list1)
# list2 = str.split(";")
# print(list2)
# list的映射解析
# li1 = [1, 2, 3, 4]
# li2 = [li3*2 for li3 in li1]
# print(li2)
# dictionary中的解析
# dict1 = {"xiaoming": 1, "xiaowang": 2, "xiaoyang": 3}
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# test1 = [(k,v) for k, v in dict1.items()]
# test2 = ["%s = %s"% (k,v) for k, v in dict1.items()]
# print(test2)
# list过滤
# list2 = ["a", "b", "ab", "abc", "abcd", "d", "c", "bc", "abcdef", "acdedfsd", "bcd"]
# test2 = [bat for bat in list2 if len(bat) > 3]
# test3 = [bat for bat in list2 if bat != "b"]
# test4 = [bat for bat in list2 if list2.count(bat) == 2]
# print(test4)



