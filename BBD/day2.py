# coding: utf-8

# 作业讲解

'亲爱的小岳岳你好！你9月的话费是32.00元，余额是18.00元'

# 方法1 - 1
# print('亲爱的%s你好！你%d月的话费是%.2f元，余额是%.2f元' % ('小岳岳', 9, 32, 18))

# 方法1 - 2
# name = '小岳岳'
# month = 9
# charge = 32
# balance = 18

# print('亲爱的%s你好！你%d月的话费是%.2f元，余额是%.2f元' % (name, month, charge, balance))

# 方法2 - 1
# name = '小岳岳'
# month = 9
# charge = 32.00
# balance = 18.00
#
# print('亲爱的{}你好！你{}月的话费是{}元，余额是{}元'.format(name, month, charge, balance))

# 方法2 - 2
# name = '小岳岳'
# month = 9
# charge = 32.00
# balance = 18.00

# print('亲爱的{xm}你好！你{yf}月的话费是{hf}元，余额是{ye}元'.format(xm=name, yf=month, hf=charge, ye=balance))

# 方法2 - 3
# name = '小岳岳'
# month = 9
# charge = 32.00
# balance = 18.00

# print('亲爱的{xm}你好！你{yf}月的话费是{hf}元，余额是{ye}元'.format(xm=name,
#                                                   yf=month,
#                                                   hf=charge,
#                                                   ye=balance))
# 方法2 - 4
# name = '小岳岳'
# month = 9
# charge = 32.00
# balance = 18.00
#
# print('亲爱的{name}你好！你{month}月的话费是{charge}元，余额是{balance}元'.format(name=name,
#                                                                 month=month,
#                                                                 charge=charge,
#                                                                 balance=balance))
# 方法2 - 5
# formal_str = '亲爱的{name}你好！你{month}月的话费是{charge}元，余额是{balance}元'
# name = '小岳岳'
# month = 9
# charge = 32.00
# balance = 18.00
# real_str = formal_str.format(name=name,
#                              month=month,
#                              charge=charge,
#                              balance=balance)
#
# print(real_str)

'http://192.168.2.111/huice/event/api/add?title=python大会&time=2018-01-06'

# 方法1
# protocol = 'http'
# hostname = '192.168.2.111'
# address = 'huice/event/api/add'
# params = 'title=python大会&time=2018-01-06'
#
# print('%s://%s/%s?%s' % (protocol, hostname, address, params))

# 方法2
# protocol = 'http'
# hostname = '192.168.2.111'
# address = 'huice/event/api/add'
# params = 'title=python大会&time=2018-01-06'
#
# f_str = '{protocol}://{host}/{url}?{params}'
# r_str = f_str.format(protocol=protocol,
#                      host=hostname,
#                      url=address,
#                      params=params)
# print(r_str)

# 字符串连接

# +连接

'田老师的年龄是xxxx岁'
# age = 50
# a = '田老师的年龄是%d岁' % age
# print(a)

# print('田老师的年龄是' + str(age) + '岁')

# 以上两种方法，需要拼接的字符串太多时(超过3个)不方便且可读性差，
# 应改用format()方法

# 如：亲爱的{}你好！你{}月的话费是{}元，余额是{}元

# join()连接

# 错误1
# '&'.join('xiaoping', 'xiaofang', 'xiaoling')

# 错误2
# print('&'.join('xiaoping'))

# 正确1
# print('&'.join(['xiaoping', 'xiaofang', 'xiaoling']))

# 正确2
# print('###'.join(['xiaoping', 'xiaofang', 'xiaoling']))
# print(' '.join(['xiaoping', 'xiaofang', 'xiaoling']))
# print(''.join(['xiaoping', 'xiaofang', 'xiaoling']))

# 类和对象简介
# 不写代码

# print()
# st = open('1.txt', 'w')
# print(1, 2, 3, file=st)

# input
# 接收一个数字，把这个数字加1再输出出来
# 错误
# a = input('请输入数字')
# print(a + 1)

# 正确
# a = input('请输入数字')
# print(int(a) + 1)

# 模拟倒计时
# import time
#
# a = 9
# while (a >= 0):
#     print('\r', a, sep='', end='')
#     time.sleep(1)
#     a -= 1

# for ele in [1, 3, 7, 2, 4]:
#     print(ele)
#
# for c in 'Hello Huice':
#     print('*')
#
# for c in '大家好':
#     print(c)

'1、对于列表[1,5,2,4,9],打印其中每个数的平方'
# lst01 = [1, 5, 2, 4, 9]
# for ele in lst01:
#     print(ele ** 2, end=' ')

"2、对于字符串'Huice',打印出每个字符的ASCII码值（十进制）"
# for c in 'Huice':
#     print(ord(c))

'输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数'
# def isalpha(word):
#     try:
#         return word.encode('ascii').isalpha()
#     except:
#         return False
#
#
# line = input('请输入：')
# counter_alpha = counter_space = counter_digit = counter_other = 0
#
# for c in line:
#     if isalpha(c):
#         counter_alpha += 1
#     elif c.isdigit():
#         counter_digit += 1
#     elif c.isspace():
#         counter_space += 1
#     else:
#         counter_other += 1
# print('字母有' + str(counter_alpha) + '个')
# print('数字有' + str(counter_digit) + '个')
# print('空格有' + str(counter_space) + '个')
# print('其他字符有' + str(counter_other) + '个')

# 1. 分别使用while与for循环输出1-100之间的所有偶数
# i = 1
# while(i <= 100):
#     if i%2 == 0:
#         print(i, end=' ')
#     i += 1
# print()

# 2.
# for i in range(1, 101):
#     if i %2 == 0:
#         print(i, end=' ')

# 用python输出一个简单的旋转风车，模拟等待图标
# import time
# signs = ['/', '-', '\\', '|']
#
# while True:
#     for c in signs:
#         print(c, '\r', end='')
#         time.sleep(0.1)

# 反向
# while True:
#     for i in range(len(signs)-1, -1, -1):
#         print(signs[i], '\r', end='')
#         time.sleep(0.1)

# enumerate举例1
# phone_list = ['OPPO', 'vivo', 'Apple', 'Huawei', 'HONOR', 'MI', 'MEIZU']
# for i, j in enumerate(phone_list):
#     print('第%d名:' % (i + 1), j)

# enumerate练习
# seq = '2Apples&3Pears&5bananas'
# for i, j in enumerate(seq):
#     if j.isdigit():
#         print("第%d个字符是数字，为'%s'" % (i + 1, j))

# break continue else举例
# for i in range(1, 11):
#     if i % 3 != 0:
#         continue
# #       break
#     print(i)
# else:
#     print('循环正常结束')

'打印一个9*9 的方阵，由星号组成'

# for i in range(9):
#     for j in range(9):
#         print('*', end=' ')
#     print()
#
# 练习：
# 1.
# 接收用户输入的一个字符串：h, w
# 代表矩形的长和宽，打印一个空心的矩形
# h = input('请输入高：')
# w = input('请输入宽：')
# h = int(h)
# w = int(w)
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h-1 or j == w-1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# 2.
# 输出九九乘法口诀

# for i in  range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%2d' % (j, i, i*j), end=' ')
#     print()

#
# 例：
# 接收用户输入的数字，计算该数字的阶乘
# a = input('请输入一个数字')
#
# if not a.isdigit():
#     print('输入有误')
# else:
#     a = int(a)
#     res = 1
#     for i in range(1,a+1):
#         res = res * i
#     print('%d的阶乘是%d' % (a, res))


# 练习：
# 输入n, 计算1到n的阶乘之和

# n = input('请输入一个数字')
#
# if not n.isdigit():
#     print('输入有误')
# else:
#     n = int(n)
#     sum = 0
#     for i in range(1,n+1):
#         fact=1
#         for j in range(1,i+1):
#             fact *= j
#         sum += fact
#     print('1到%d的阶乘之和是%d' % (n, sum))

# 例：找1000以内最大平方数
# 方法1
# result = 1
# for i in range(1, 1001):
#     squ = i ** 2
#     if squ <= 1000:
#         result = squ
#     else:
#         break
# print(result)

# 方法2
# import math
#
# for i in range(1000, 0, -1):
#     if int(math.sqrt(i)) == math.sqrt(i):
#         print(i)
#         break

#
# 例：给定一个字符串
# target = 'hello huice'，从中找出第一个不重复的字符, 输出它是第几位
# 练习：去除上一题中的重复字符，得到一个新的字符串

# target = 'hello huice'
#
# for idx, char in enumerate(target):
#     if target.count(char) == 1:
#         print('第一个不重复字符是%s，它是第%d位' %(char, idx + 1))
#         break
#
# for char in target:
#     if target.count(char) > 1:
#         target = target.replace(char, '')
# print(target)

# a = (1,)
# print(type(a))
# print(1, 2, 3, sep='哈哈哈')
# print(a[0])
# # a[0] = 1 #'tuple' object does not support item assignment
# a = (2,)
# print(a[0])
# del(a)
# print(a)
#
# a = 1, 2, 3
# b = 4, 5, 6
# c = a + b
# print(c)
# print(c * 3)
# print(min(c))
#
# a = range(1, 100)
# b = tuple(a)
# print(b)

# 元组虽然是不可变数据类型，但是当元组中嵌套可变元素时，该可变元素是可以修改的，元组本身不变
# a = ([1, 2, 3], (4, 5, 6))
# print(a, id(a))
# a[0][2] = 4
# print(a, id(a))
'''
练习：员工工资表，查询结果集如下：((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
1.计算员工的平均工资
2.输出工资最高的员工姓名
'''
# t = ((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
# sum = 0
# for item in t:
#     sum += item[-1]
# avg = sum/len(t)
# print(avg)
#
# max_salary = t[0][-1]
# max_name = t[0][1]
# for item in t:
#     if item[-1] > max_salary:
#         max_salary = item[-1]
#         max_name = item[1]
# print('工资最高的人是%s' % max_name)

a = [1, 2, 3, 4]

# a.append(5)
# print(a)
# a+=[6]
# print(a)

# a[2:2] = ['a','b','c']
# print(a)

# a[2:3] = ['a','b','c']
# print(a)

# a[2:] = ['a','b','c']
# print(a)

# a[1:3] = []
# print(a)

# del(a[1])
# print(a)

# a.insert(2,8)
# print(a)

# print(a.pop(2))
# print(a)

# print(a.remove(2))
# print(a)

# def my_sort(string):
#     return string[0]
#
# a = ['Java', 'Ruby', 'Python', 'JavaScript', 'C', 'C#']
# a.sort(reverse=True, key=my_sort)
# print(a)

# def my_sort(list):
#     return list[-1]
#
# lst = [[1, 'zhangsan', 3000], [2, 'lisi', 2500], [3, 'tiantian', 20000]]
#
# lst.sort(key=my_sort)
# print(lst)
#
# print(sorted(lst, key=lambda x:x[-1], reverse=True)[0][1])

# 1.检查get请求的参数中是否包含sign,如果包含将参数值替换为空格，重新拼接为参数字符串
# title=华为春季新品发布会&sign=2&limit=100&status=0&address=国家会议中心&time=2018-03-28

# source = 'title=华为春季新品发布会&sign=2&limit=100&status=0&address=国家会议中心&time=2018-03-28'
# para_list = source.split('&')
# for para in para_list:
#     if(para.startswith('sign=')):
#         idx = para_list.index(para)
#         para_list[idx] = para.replace(para.split('=')[-1], ' ')
# print('&'.join(para_list))

# x = [1, 2, 3, 4, 5]
# print([i ** 2 for i in x])

# 一行代码实现对a中的偶数位置的元素进行加3后，组成的新列表
# a=[1, 2, 3, 4, 5, 6]
# print([i + 3 for i in range(1, len(a), 2)])

# a = [1,2,3,4]
# b = ('tian', 'liu', 'zhang')
# c = [50, 18]
#
# print(list(zip(a,b,c)))

print(list('haha'))
str1 = '[1,2,3,4]'
print(type(eval(str1)))

s1 = {'zhangsan', 'lisi', 'wangwu'}
s2 = set((1, 2, 3))
print(type(s1))
print(type(s2))
# print(s1[0]) #不支持
for i in s1:
    print(i)

# s1.add('zhaoliu')
# s1.remove('liuliu')
# s1.discard('liuliu')
# print(s1)
# s1.add('zhangsan')
# print(s1)
#
# print(s1.pop())
# print(s1)

# dic1 = {'name':'zhangsan', 'age': 18, 'address': 'beijing', 'xxx': 'hahaha'}
# print(dic1['age'])
# print(dic1.get('xxx'))

lst1 = ['name', 'age']
lst2 = ['tianlaoshi', 18]
print(dict(zip(lst1, lst2)))