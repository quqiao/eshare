#
# a = 1
# b = a
# print(b)
#
# c = a + 1
# print(c)
#
# def add(x,y):
#     return x+y
#
# d = add(3,5)
# print(d)

# 弱类型语言

# a = 1
# print(a)
# print(type(a))
# a = 'haha'
# print(a)
# print(type(a))
#
# a = '1'
# b = 'haha'
#
# print(id(a))
# print(id(b))
#
# print(type(1.2))
#
# a = 34124323142143243234234234234234341243231421432432342342342342343412432314214324323423423423423434124323142143243234234234234234341243231421432432342342342342343412432314214324323423423423423434124323142143243234234234234234
# print(type(a))
#
# a = 2 * 3.5
# print(type(a))
#
# a = 3.9
# print(int(a))
#
# a = 5
# print(float(a))
#
# print(chr(98 - 32))
# print(ord('a'))
#
# print(a < 0)
#
# a = 'Mary said, \"I\'m OK\"'
# print(a)
#
# a = '窗含西岭千秋雪\n门泊东吴万里船'
# print(a)
#
# print(r"C:\Program Files\fnord\foo\bar\baz\frozz")
#
# print()
#
# a = [1, 2, 3, 4, 5]
# b = str(a)
# print(b)
# print(type(b))
#
# a = [1.2, 'haha', True, ['a', 'b'], {}, ()]
# b = (1.2, 'haha', True, ['a', 'b'], {}, ())
# c = {'name': 'zhangsan', 'age': 18}
#
# print(None)
# print(type(None))

# def add(x,y):
#     x+y
#
# print(add(1,2))
#
#
#
# a = [1,2,3,4]
# print(id(a))
# a += [5,6]
# a.append(7)
# print(a)
# print(id(a))
# a = [1,2,3,4,5,6,7,8]
# print(id(a))
#
# print(9%2)
# # 地板除
# print(-29.0//10)
#
# a = 1
# b = 1
# print(a is b)
# print(id(a) == id(b))
#
# a = 'haha'
# b = 'haha'
# print (a is b)
#
# a = False
# b = False
# print (a is b)
#
# a = (1,2,3)
# b = (1,2,3)
# print (a is b)
#
# b = a
# print (a is b)

# a = [1,2,3]
# a = a + [4,5]
# a += [4,5]
#
# a,b,c = 1,2,3
#
# a=2
# b=5
# a,b = b,a
# print(a,b)
#
# print(a>2 and b+2 and b==3)
#
# print('ll' in 'hello')

# a = "您账户%s于%d月%d日入账工资，人民币%.2f，%s" % ('4567', 11, 10, 800.00, '欢迎来慧测')
# print(a)
#
# a = "您账户{}于{}月{}日入账工资，人民币{}，{}"
# print(a.format('4567', 11, 10, 800.65, '欢迎来慧测'))
#
# a = "您账户{account}于{month}月{day}日入账工资，人民币{money}，{adv}"
# a = a.format(account='4567',
#          money=200000.00,
#          adv='xx理财欢迎你',
#          month=12,
#          day=10)
# print(a)
#
# b = 'asdfasfsadfasdfasfdasdfasdfsadf'
# a = 'Hello World'
# b = 'How are you'
#
# ll = [a, b]
# c = '&'.join(ll)
# print(c)