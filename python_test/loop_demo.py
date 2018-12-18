#coding=utf-8
'''
Created on 2018年12月10日
@author: quqiao
'''

# Python循环语句有for和while
# 同样需要注意冒号和缩进。另外，在Python中没有do..while循环

# while循环
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter +=1
# print("1 到 %d 之和为: %d" % (n, sum))

# 无限循环
# var = 1
# while var == 1:
#     num = int(input("输入一个数字："))
#     print("你输入的数字为：",num)
# print("GoodBye!!!")

# while循环使用else语句
# count = 0
# while count < 5:
#     print(count, "小于5")
#     count = count + 1
# else:
#     print(count, "大于或等于5")

# 简单语句组
# flag = 5
# while (flag): print("欢迎访问菜鸟教程！")
# print("GoodBye!!!!")

# for语句
# sites = ["test1", "test2", "test3", "test4", "test5", "test6"]
# for site in sites:
#     if site == "test2":
#         print("是我是我！")
#         break
#     print("循环数据" + site)
# else:
#     print("没有循环数据！")
# print("完成循环！")

# range()函数
# 遍历数字序列，可以使用内置range()函数 例如：range(5)
# 指定区间:range（5,9）
# 指定数字开始并指定不同的增量:range(0,10,3）
# a = ["Google", "Baidu", "Runoob", "TaoBao", "QQ"]
# for i in range(len(a)):
#     print(i, a[i])

# break和continue
# break语句可以跳出for和while的循环体。如果从for或while循环中止，任何对应的循环else块将不执行
# continu语句被用来告诉Python跳过当前循环快中的剩余语句，继续进行下一轮循环
# for letter in "Runoob":
#     if letter == 'o':
#         break
#     print("当前字母为：", letter)
# var = 10
# while var > 0:
#     print("当前变量为：", var)
#     var = var - 1
#     if var == 5:
#         break
# print("Good bye!")

# for letter in "Runoob":
#     if letter == 'o':
#         continue
#     print("当前字母为：", letter)
# var = 10
# while var > 0:
#     var = var - 1
#     if var == 5:
#         continue
#     print("当前变量为：", var)
# print("Good bye!")

# 循环语句中的else子句
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x ==0:
#             print(n, "等于", x, "*", n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, "是质数")

# pass语句
# pass是空语句，为了保持程序结构的完整性
# pass不做任何事情，一般用做占位语句
# for letter in "Runoob":
#     if letter == "o":
#         pass
#         print("执行 pass 块")
#     print("当前字母：", letter)




