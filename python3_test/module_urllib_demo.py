#coding=utf-8
'''
Created on 2018年12月10日
@author: quqiao
'''

# urllib.request 请求模块
# urllib.error   异常处理模块
# urllib.parse   url解析模块
# urllib.robotparser  robots.txt解析模块

# urlopen
import urllib.request
response = urllib.request.urlopen('https://www.baidu.com')
print(response.read())