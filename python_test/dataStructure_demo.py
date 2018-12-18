#coding=utf-8
'''
Created on 2018年12月12日
@author: quqiao
'''

# 数据结构
# Python中列表是可变的，字符串和元祖是不能修改的

# 列表的方法：
# list.append(x):把一个元素添加到列表的结尾，相当于a[len(a):] = [x]
# list = [1, 2, 3, 4, 5]
# list.append("test")
# list[len(list):] = [x]
# print(list)
# list.extend(L):通过添加指定列表的所有元素来扩充列表，相当于a[len(a):] = L
# list = [1, 2, 3, 4, 5]
# list2 = ["test", "test2"]
# list.extend(list2)
# # list[len(list):] = list2
# print(list)
# list.insert(i,x):在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引
# list = [1, 2, 3, 4, 5]
# list.insert(1,"test")
# print(len(list))
# list.remove(x):删除列表中值为x的第一个元素，如果没有这样的元素，就会返回一个错误
# list = [1, 2, 3, 4, 5]
# list.remove(1)
# print(list)
# list.pop([i]):从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除
# list = [1, 2, 3, 4, 5]
# list.pop(3)
# print(list)
# list.clear():移除列表中的素有想，等于del a[:]
# list = [1, 2, 3, 4, 5]
# list.clear()
# print(list)
# list.index(x):返回列表中第一个值为x的元素的索引。如果没有匹配的元素就会返回一个错误
# list = [1, 2, 3, 4, 5]
# print(list.index(2))
# list.count(x):返回x在列表中出现的次数
# list = [1, 2, 3, 4, 3, 3, 5]
# print(list.count("test"))
# list.sort():对列表中的元素进行排序
# list = [2, 4, 5, 3, 5, 9, 10, 11, 23, 9, 12]
# list.sort()
# print(list)
# list.reverse():倒排列表中的元素
# list = [9, 5, 8, 22, 18]
# list.reverse()
# print(list)
# list.copy():返回列表的浅复制，等于a[:]
# list = [1, 2, 3, 4, 5]
# list.copy()
# print(list)

# 将列表当做堆栈使用
# append()和pop()方法
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)

# 将列表当作队列使用
# from collections import deque
# queue = deque([1, 2, 3, 4, 5, 6, 7])
# queue.append(8)
# queue.append(9)
# print(queue)
# print(queue.popleft())

# 列表推导式
# vec1 = [2, 4, 6]
# vec2 = [10, 20, 30]
# print([3*x for x in vec1])
# print([[x, x**2] for x in vec1])
# print([3*x for x in vec1 if x > 3])
# print([x*y for x in vec1 for y in vec2])
# print([vec1[i]*vec2[i] for i in range(len(vec1))])
# print([str(round(355/113, i)) for i in range(1, 6)])

# 嵌套列表解析
# Python的列表还可以嵌套
# matrix = [
#             [1, 2, 3, 4],
#             [5, 6, 7, 8],
#             [9, 10, 11, 12],
#          ]
# print([[row[i] for row in matrix] for i in range(4)])
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

# del语句
# 可以用del语句从列表中删除一个切割，或者
# 清空整个列表
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[3]
# print(a)

# 元组和序列
# 元组由若干逗号分割的值组成
# 输出时总是有括号的，在输入时可能有或没有括号，不过括号通常是必须的
# t = 12345, 34566, 2222, "test", 1
# print(t[1])
# u = t, 1222, 3333, 9999
# print(u)

# 集合
# 集合是一个无序无重复元素的集。基本功能包括关系测试和消除重复元素
# 可以用大括号{}创建集合
# 创建一个空集合，必须用set()
# basket = {'sss', '2222', '2222', '3333', 'sddffd', '1wedf'}
# print(basket)
# print("ssss" in basket)
# a = set("abcdefghigklmn")
# b = set("1234567890")
# print(a)
# print(a - b)
# print(a | b)
# print(a & b)
# print(a ^ b)
# 集合推导式
# a = {x for x in "abc1bca2cab3" if x not in "abc"}
# print(a)

# 字典
# 字典以关键词为索引，关键字可以是任意不可变类型，通常用字符串或数值
# 字典是无序的键值对集合，同一个字典内，关键字必须是互不相同
# 一对大括号创建一个空的字典
# alibaba = {"test001": "zhangsan", "test002": "lisi", "test003": "wangwu"}
# print(alibaba["test001"])
# print(alibaba)
# del alibaba["test002"]
# print(alibaba)
# alibaba["test004"] = "jialiu"
# print(alibaba)
# print(list(alibaba.keys()))
# print("test001" in alibaba)
# print("test010" in alibaba)
# 构造函数dict()直接从键值对元组列表中构建字典
# a = dict([("tt1", 1), ("tt2", 2), ("tt3", 3)])
# b = dict(first=1, second=2)
# print(b)
# print(a)
# 字典推导用来创建任意键和值的表达式词典
# a = {x: x**2 for x in (2, 4, 6)}
# print(a)

# 遍历技巧
# 在字典中遍历时，关键字和对应的值可以使用items()方法同时解读出来
# knights = {"test001": 1, "test002": 2}
# for i, j in knights.items():
#     print(i, j)
# 在序列中遍历时，索引位置和对应值可以使用emumerate()函数同时得到
# for i, v in enumerate(["tic", "tac", "toe"]):
#     print(i, v)
# 同时遍历两个或更多的序列，可以使用zip()组合
# question = ["name", "quest", "favorite", "color"]
# answers = ["lancelot", "the holy grail", "blue"]
# for q, a in zip(question, answers):
#     print("whai is your {0}? it is {1}!".format(q, a))
# 要反向遍历一个序列，首先指定这个序列，然后调用reverse()函数
# for i in reversed(range(1, 10, 2)):
#     print(i)
# 要按顺序遍历一个序列，使用sorted()函数返回一个已排序的序列，并不修改原值
# basket = ["apple", "orange", "apple", "pear", "orange", "bannana"]
# for f in sorted(set(basket)):
#     print(f)
