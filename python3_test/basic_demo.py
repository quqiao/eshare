#coding=utf-8
'''
Created on 2018年12月18日
@author: quqiao
'''

# 编码：源码文件以UTF-8编码，所有字符串都是Unicode字符串

# 标识符：第一个字符必须是字母表中字母或下划线_
#         标识符的其他的部分由字母，数字和下划线组成
#         标识符对大小写敏感

# Python保留字：不能用作任何标识符名称
# import keyword
# print(keyword.kwlist)

# 注释：单行注释以#开头，多行注释可用用#，还有"""和'''

# 行与缩进：使用缩进来表示代码块，不需要使用大括号。缩进空格数是可变的，同一个代码块的语句必须包含相同的缩进空格数

# 多行语句：语句很长时，可以使用反斜杠(\)来实现多行语句。在{},[],()中的多行语句不需要使用反斜杠

# 数字（Number）类型：整数（int),如1,只有一种整数类型，取消Python2中的long
#                     布尔（bool),如True或者False
#                     浮点数(float),如1.23,3E-2
#                     复数(complex),如1+2j,1.1+2.2j

# 字符串（String)：单引号和双引号使用完全相同
#                  三引号可以指定一个多行字符串
#                  反斜杠可以用来转义,使用r可以让反斜杠不发生转义
#                  按字面意义级练字符串，如"this" "is" "string"会被自动转换为this is string
#                  字符串可以用+运算符连接在一起,用*运算符重复
#                  字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
#                  字符串不能改变
#                  没有单独的字符类型,一个字符就是长度为1的字符串
# str = "1234567890abcdefg"
# print(str)
# print(str[0:-1])
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str*2)
# print("你们好"+str)
# print("-------------")
# print("hello\nrunoob")
# print(r"hello\nrunnb")

# 空行：函数之间或类的方法之间用空行分隔,表示一段新的代码的开始。类和函数入口之间叶勇一行空行分隔，以突出函数入口的开始
#       空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。空行也是程序代码的一部分

# 等待用户输入：
# input("n\n\按下enter键后退出:")

# 同一行显示多条语句：可以在同一行使用多条语句，语句之间使用分号(:)分割
# import sys;x = "runoob"; sys.stdout.write(x + '\n')

# 多个语句构成代码组：缩进相同的一组语句构成一个代码块，称之为代码组

# print输出：默认输出是换行的，如果不换行需要在变量末尾加上end=""
# x="a"
# y="b"
# # 换行输出
# print( x )
# print( y )
# print('---------')
# # 不换行输出
# print( x, end="\n" )
# print( y, end="\n" )
# print()

# import与from...import
# 将整个模块导入：import xxx
# 从某个模块中导入某个函数：from xxx import xxxx
# 从某个模块中导入多个函数：from xxx import xxx1,xxx2
# 将某个模块中的全部函数导入：from xxx import *

# 命令行参数：执行一些操作来查看一些基本信息，例如：Python -h

# python3解释器：交互式编程，在命令提示符中输入"Python"命令来启动Python解释器
#                脚本式编程，将脚本拷贝到.py文件中，通过命令执行该脚本

# Python算术运算符
# + 加：两个对象相加
# - 减：得到负数或是一个数减去另一个数
# * 乘：两个数相乘或是返回一个被重复若干次的字符串
# / 除：x除以y
# % 取模：返回除法的余数
# ** 幂：返回x的y次幂
# // 取整除：向下接近除数的整数, 9//2 = 4

# Python比较运算符
# == 等于：比较对象是否相等
# != 不等于：比较两个对象死否不相等
# > 大于：返回x是否大于y
# < 小于：返回x是否小于y
# >= 大于等于：返回x是否大于等于y
# <= 小于等于：返回x是否小于等于y

# Python赋值运算符
# = 简单的赋值运算符, c=a+b将a+b的运算结果赋值为c
# += 加法赋值运算符, c +=a等于c = c+a
# -= 减法赋值运算符, c -=a等于c = c-a
# *= 乘法赋值运算符, c *=a等于c = c*a
# /= 除法赋值运算符, c /=a等于c = c/a
# %= 取模赋值运算符, c %=a等于c = c%a
# **= 幂赋值运算符, c **=a等于c = c**a
# //= 取整除赋值运算符, c //=a等于c = c//a

# Python位运算符
# & 按位与运算符,两者都为1结果才能为1，否则为0
# | 按位或运算符,两者其中1个为1，结果就能为1,
# ^ 按位异或运算符,对应二进位相异时为1
# ~ 按位取反运算符,对数据的每个二进制位取反
# << 左移动运算符,运算数的各二进位全部左移若干位
# >> 右移动运算符,运算数的各二进位全部右移若干位

# Python逻辑运算符
# and, x and y, 布尔"与",如果x,y任意一个为false,返回false
# or, x or y, 布尔"或",如果x,y任意一个为true,返回true
# not, not x, 布尔"非",如果x为true,not x返回false

# Python成员运算符
# in 如果在指定的序列中找到值返回True,否则返回False
# not in 如果在指定的序列中没有找到值返回True,否则返回False

# Python身份运算符
# is 判断两个标识符是不是引用自一个对象
# is not 判断两个标识符是不是引用自不同对象

# Python运算符优先级
# **
# ~ + -
# * / % //
# + -
# >> <<
# &
# ^ |  位运算符
# <= < > >=  比较运算符
# < > == !=  等于运算符
# = %= /= //= -= += *= **=  赋值运算符
# is   is not  身份运算符
# in   not in  成员运算符
# and or not   逻辑运算符






