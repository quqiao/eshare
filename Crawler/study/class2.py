# coding=utf-8
'''
Created on 2019年03月18日
@author: quqiao
第一课：urllib库的基本使用
'''

# 什么是urllib
# 1)Python内置的HTTP请求库
# urllib.request 请求模块
# urllib.error 异常处理模块
# urllib.parse.url 解析模块
# urllib.robotparser robots.txt 解析模块

# urllib.request.urlopen()：用于实现对目标url的访问
# from urllib import request
# response = request.urlopen('https://www.baidu.com/')
# print(response.read().decode('utf-8'))

# urllib.parse.urlencode():把key-value这样的键值对转换成我们想要的格式，返回a=1&b=2这样的字符串
# from urllib import parse
# values = {}
# values["username"] = "汪汪队"
# values["password"] = "123456"
# data = parse.urlencode(values)
# print(data)

# urldecode：没有urldecode()函数，只提供了unquote()函数
# from urllib import parse
# s = "%E5%B9%BF%E5%B7%9E"
# s1 = parse.unquote(s)
# print(s1)

# 响应：响应类型，状态码，响应头
# from urllib import request
# response = request.urlopen('https://www.python.org')
# print(type(response))
# print(response.status)
# print(response.getheaders().response.getheader("server"))

# 设置headers:有很多网站为了防止程序爬虫爬网站造成网站瘫痪，会需要携带一些headers头部信息才能访问，
#             最常见的有user-agent参数
# from urllib import request,parse
# url = "http://httpbin.org/post"
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'zhaofan'
# }
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method="POST")
# response = request.urlopen(req)
# print(response.read().decode("utf-8"))

# 高级用法，各种handler,代理，ProxyHandler
# 通过urllib.request.ProxyHandler()可以设置代理，网站会检测某一段时间某个IP的访问次数，如果访问次数过多，他会禁止你的
# 访问，所以这个时候需要通过设置代理来爬取数据
# import urllib.request
# proxy_handler = urllib.request.ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read())

# cookie.HTTPCookiProcessor:cookie中保存中我们常见的登录信息，有时候爬取网站需要携带cookie信息访问，这里用到了http.cookie
#                           用于获取cookie以及存储cookie
# import http.cookiejar, urllib.request
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# 同样的如果想要通过获取文件中的cookie获取的话可以通过load方式
# import http.cookiejar,urllib.request
# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))

# 异常处理：在很多时候我们通过程序访问页面的时候，有的页面可能会出现错误，类似404,500等错误，这个时候就需要我们捕捉异常
# urllib异常两个异常错误：URLError,HTTPError,HTTPError是URLError的子类
# URLError只有一个属性：reason，即抓异常的时候只能打印错误信息，
# HTTPError有三个属性：code,reason,headers，即抓异常的时候可以获得code,reason,headers三个信息
# from urllib import request, error
# try:
#     response = request.urlopen("http://pythonsite.com/1111.html", timeout=5)
# except error.HTTPError as e:
#     print(e.reason)
#     print(e.code)
#     print(e.headers)

# URL解析
# urlparse
# from urllib.parse import urlparse
# result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
# print(result)
# urlunparse:功能与urlparse相反，用于拼接
# from urllib.parse import urlunparse
# data = ['http','www.baidu.com','index.html','user','a=123','commit']
# print(urlunparse(data))
# urljoin:做拼接
# from urllib.parse import urljoin
# print(urljoin('http://www.baidu.com', 'FAQ.html'))


