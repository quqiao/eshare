#coding=utf-8
'''
Created on 2018年12月05日
@author: quqiao
'''

# 类（Class)：用来描述具有相同的属性和方法的对象的集合。他定义了该集合中每个对象所共有的属性和方法。对象是类的实例
# 方法：类中定义的函数
# 类变量：在整个实例化的对象中是公用的。类变量定义在类中且函数体之外。类变量通常不作为实例变量使用
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法覆盖（override），也称方法重写
# 局部变量：定义在方法中的变量，只作用于当前实例的类
# 实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的
# 继承：即一个派生类继承基类的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待
# 实例化：创建一个类的实例，类的具体对象
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法

# 类对象：支持两种操作，属性引用和实例化
# class MyClass:
#     i = 123456
#     def f(self):
#         return 'hello world'
#
# x = MyClass()  # 实例化类
# print("MyClass类的属性i为：", x.i)
# print("MyClass类的方法f输出为：", x.f())

# 构造方法：__init__()方法
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(4, 5)
# print(x.r, x.i)

# self代表实例，而非类
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
# t = Test()
# t.prt()

# 类的方法
# class people:
#     # 定义基本属性
#     name = "xxxx"
#     age = 35
#     # 定义私有属性，私有属性在类外部无法直接进行访问
#     __weight = 90
#     # 定义构造方法
#     def __init__(self,n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说：,体重 %d KG" % (self.name, self.__weight))
# p = people("test", 10, 30)
# p.speak()

# 继承
# 类的定义
# class people:
#     # 定义基本属性
#     # name = ''
#     # age = 0
#     # # 定义私有属性,私有属性在类外部无法直接进行访问
#     # __weight = 0
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
# class student(people):
#     grade = ''
#     def __init__(self, n, a, w, g):
#         # 调用父类的构造函数
#         people.__init__(self, n, a, w)
#         self.grade = g
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说：我 %d 岁了，我在读 %d 年纪" % (self.name, self.age, self.grade))
# s = student("ssss", 10, 500, 3)
# s.speak()

# 多继承
# class people:
#     # 定义基本属性
#     name = ""
#     age = 0
#     # 定义私有属性，私有属性在类外部无法直接进行访问
#     __weight = 0
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说： 我 %d 岁了。" %(self.name, self.age))
#
# class student(people):
#     grade = ""
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#     def speak1(self):
#         print("%s 说： 我 %d 岁了，在读 %d 年级"%(self.name, self.age, self.grade))
#
# class speaker():
#     topic = ""
#     name = ""
#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t
#     def speak2(self):
#         print("我叫%s,我是一个演说家，我演讲的主题是 %s"%(self.name, self.topic))
#
# class sample(student, speaker):
#     a = ""
#     def __init__(self,n, a, w, g, t):
#         student.__init__(self, n, a, w, g)
#         speaker.__init__(self, n, t)
#
# test = sample("teet", 25, 80, 4, "xxxx")
# test.speak2()

# 方法重写
# class Parent:
#     def myMethod(self):
#         print("调用父类方法")
#
# class Child(Parent):
#     def myMethod(self):
#         print("调用子类方法")
# c = Child()
# c.myMethod()
# super(Child, c).myMethod()

# 类属性与方法
# 类的私有属性：两个下划线开头，声明该属性为私有属性，不能在类的外部被使用或直接访问，在类内部的方法中使用时
#               self.__private_attrs
# 类的方法：def关键字定义一个方法，类方法必须包含参数self且为第一个参数，self代表的是类的实例
#           self的名字并不是规定死的，也可以使用this,但是最好还是按照约定使用self
# 类的私有方法：两个下划线开头，声明该方法为私有方法，只能在类的内部调用，不能在类地外部调用
# class JustCounter:
#     __secretCount = 10  # 私有变量
#     publicCount = 1  # 公开变量
#
#     def count(self):
#         self.__secretCount +=1
#         self.publicCount +=1
#         print(self.__secretCount)
#         # print(self.publicCount)
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)

# 类的私有方法
# class Site:
#     def __init__(self, name, url):
#         self.name = name
#         self.__url = url
#     def who(self):
#         print("name :", self.name)
#         print("url:", self.__url)
#     def __foo(self):
#         print("这是私有方法")
#     def foo(self):
#         print("这是公共方法")
#         self.__foo()
# x = Site("test", "www.runoob.com")
# x.who()
# x.foo()
# # x.__foo()

# 运算符重载
# class vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     # def __str__(self):
#     #     return "Vector (%d,%d)" % (self.a, self.b)
#     def __add__(self, other):
#         print(vector(self.a + other.a, self.b + other.b))
#
#
# v1 = vector(2, 10)
# v2 = vector(5, -2)
# print(v1 + v2)



