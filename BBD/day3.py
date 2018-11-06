# a = ['哈哈', 'xixi', 'hehe']
# print(a[0])
# print(a[0:2])
# a[1] = '嘻嘻'
# a[-1] = '呵呵'
# print(a)
# print(a[-3])
# a.append('汪汪')
# print(a)
# b = [1,2,3]
# # a.append(b)
# # print(a)
# a.extend(b)
# print(a)

# a += b
# a[2:2] = b
# print(a)

# a = ['h', 'e', 'l', 'l', 'o']
# print(a.count('e'))
# print(a.index('l'))
# print(a.append('haha'))
#
# a.append('haha')
# print(a)
# print(a.pop(1))
# print(a)
# print(a.remove('e'))
# print(a)

# a.reverse()
# print(a)

# a = ['Java', 'Python', 'C', 'Ruby', 'PHP', 'JavaScript']

# def my_sort(a):
#     return a[-1]
#
# 匿名函数

# a.sort(key=lambda a:a[-1])
# print(a)


# table = [(1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000)]
#
# # def my_sort(a):
# #     return a[-1]
#
# table.sort(reverse=True, key=lambda x:x[-1])
# print(table)
#
# # [(3, 'tiantian', 20000),(1, 'zhangsan', 3000), (2, 'lisi', 2500)]

# table = [(1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000)]
#
# print(sorted(table, key=lambda x:x[-1], reverse=True)[0][1])

# a = ['Java', 'Python', 'C', 'Ruby', 'PHP', 'JavaScript']
#
# for ele in a:
#     print(ele)

# a[0]
# a[1]
#
#
# a[len(a)-1]

# for i in range(len(a)):
#     print(a[i])
#
# for i,j in enumerate(a):
#     print(i,j)

# a = [1,2,3,4,5]
#
# new = []
# for ele in a:
#     new.append(ele ** 2)
# print(new)
#
# print([ele ** 2 for ele in a])

# a = [1,2,3]
# b = [2,3,4]
# # print(a+b)
# print(a*3)

# a = [1,2,3]
# b = ['zhangshan', 'lishi', 'tiantian']
# c = [2000, 3000, 20000]
#
# print(tuple(zip(a,b,c)))
#
# int()
# str()
# list()
# tuple()
#
# str0='xiaoming&xiaohong&xiaohua'
# a = str0.split('&')
# print('&&'.join(a))

# a = '(1,"a", 23]'
# print(type(eval(a)))

# s1 = [8, 1, 5, 3, 2, 5, 3]

# lst0 = list(set(s1))
#
# lst0.sort(key=lambda x:s1.index(x))
# print(lst0)

# new = []
# for ele in s1:
#     if ele not in new:
#         new.append(ele)
#     else:
#         pass
# print(new)

# dic = {'name':'zhangsan', 'age': 57}
# # print(dic['age'])
# dic['age'] = 58
# # print(dic)
#
# # print(dic['gender'])
# # print(dic.get('gender'))
# dic['gender'] = '男'
# print(dic)

# 1、把字符串”k1:1|k2:2|k3:3”处理成 python 字典的形式:{'k1': 1, 'k2': 2, 'k3': 3}

source = 'k1:1|k2:2|k3:3'

list0 = source.split('|')

result = {}

for ele in list0:
    key = ele.split(':')[0]
    value = ele.split(':')[-1]
    result[key] = int(value)
print(result)
#
print(result.keys())
print(result.values())
print(result.items())


#
# print(result.pop('k2'))
# print(result)

# dic = {}
# a = ['name', 'age', 'gender']
# print(dic.fromkeys(a))

# a = {'k1': 10, 'k4': 5}
# result.update(a)
# print(result)

# for key in result.keys():
#     print(key)
#
# for value in result.values():
#     print(value)
#
# for item in result.items():
#     print(item)
#
# for k, v in result.items():
#     print(k, v)

# print(sorted(result.keys(), reverse=True))
# print(sorted(result.values(),reverse=True))
# print(sorted(result.items(),reverse=True))
#
# scores = {'zhangsan': 98, 'lisi': 85, 'wangwu': 90}
#
# # [('zhangsan', 98), ('lisi', 85),('wangwu', 90)]
#
# print(sorted(scores.items(), key=lambda x:x[-1], reverse=True))


def add_two_number(x, y):   #形式参数 形参
    '''求加法的函数,
gongnndnfasdfafds'''
    return x + y

x = 3
y = 4

list = ['aa', 'bb', 'ccc']









