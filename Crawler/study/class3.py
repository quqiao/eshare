# coding=utf-8
'''
Created on 2019年03月21日
@author: quqiao
第三课：Requests库的基本使用
'''

# 什么是Requests：是用Python语言基于urllib编写的，采用Apache2 Licensed开原协议的HTTP库

# import requests
# response = requests.get("https://www.baidu.com")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)
# print(response.content)
# print(response.content.decode("utf-8"))

# 各种请求方式
# import requests
# print(requests.post("http://httpbin.org/post"))
# print(requests.get("http://httpbin.org/post"))
# print(requests.put("http://httpbin.org/post"))
# print(requests.delete("http://httpbin.org/post"))
# print(requests.option("http://httpbin.org/post"))

# 基本GET请求
# import requests
# 第一种情况
# response = requests.get("http://httpbin.org/get?name=zhangsan&age=23")
# print(response.text)
# 第二种情况
# data = {"name": "zhangsan", "age": 25}
# response = requests.get("http://httpbin.org/get", params=data)
# print(response.url)
# print(response.text)

# 解析json
import requests
import json
# response = requests.get("http://httpbin.org/get")
# print(type(response.text))
# print(json.loads(response.text))
# print(type(response.json()))
# print(response.content)
# print(type(response.content))
# 获取二进制数据：response.content,这样获取的数据是二进制数据，这个方法也可以用于下载图片以及视频资源

# 基本POST请求：通过发送post请求时添加一个data参数，这个data参数通过字典构成
# import requests
# data = {"name": "james", "age":23}
# response = requests.post("http://httpbin.org/post", data=data)
# print(response.text)

# 响应
# import requests
# response = requests.get("http://www.baidu.com")
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)

# requests高级用法
# 文件上传：构造一个字典然后通过files参数传递
# import requests
# files = {"files": open("git.jpeg", "rb")}
# response = requests.post("http://httpbin.org/post",files=files)
# print(response.text)
# 获取cookie
# import requests
# response = requests.get("http://www.baidu.com")
# print(response.cookies)
# for key, value in response.cookies.items():
#     print(key+"="+value)
# 会话维持：cookie的一个作用就是可以用于模拟登录，做会话维持
# import requests
# s = requests.session()
# s.get("http://httpbin.org/cookies/set/number/123456")
# response = s.get("http://httpbin.org/cookies")
# print(response.text)
# 证书验证：现在很多网站都是https的方式访问，所以这个时候就涉及到证书的问题
# import requests
# import urllib3
# urllib3.disable_warnings()
# response = requests.get("https://www.12306.cn", verify=False)
# print(response.status_code)
# 代理设置
# import requests
# proxies = {"http": "http://127.0.0.1:222"}
# response = requests.get("https://www.baidu.com", proxies=proxies)
# print(response.text)
# 如果代理需要设置账户名和密码，只需要将字典更改如下
# proxies = {"http": "http://user:password@127.0.0.1:9999"}
# 超时设置：通过timeout参数可以设置超时的时间
# 认证设置：如果遇到需要认证的网站可以通过request.auth模块实现
# import requests
# from requests.auth import HTTPBasicAuth
# response = requests.get("http://120.27.34.24:9001/", auth=HTTPBasicAuth("user","123"))
# 异常处理
import requests
from requests.exceptions import ReadTimeout,ConnectionError,RequestException
try:
    response = requests.get("http://httpbin.org/get",timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connection Error")
except RequestException:
    print("error")