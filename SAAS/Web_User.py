# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，web端_用户
'''
import io
import pycurl
import threading
import json
import time

def PostData(curl, url, data):
    head = [
            "Accept:*/*",
            "User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11",
            "Accept:application/json",
            "Content-Type:application/json"
           ]
    buf = io.BytesIO()  # 字符串的缓存
    # buf = io.StringIO()
    curl.setopt(pycurl.SSL_VERIFYPEER, False)
    curl.setopt(pycurl.HTTPHEADER, head)  # 设置http的包头信息
    curl.setopt(pycurl.POSTFIELDS, data)  # 设置post过去的数据，注意是一个字典样式的字符串
    curl.setopt(pycurl.URL, url)  # 设置url
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)  # 将返回的内容定向buf缓冲中
    curl.setopt(pycurl.CUSTOMREQUEST, "POST")  # 设置封装方法，有put，post，get，delete等多种方法
    curl.perform()  # 执行curl命令

    the_page = buf.getvalue().decode("utf-8")  # 返回对象buf中的所有数据
    print(the_page)
    buf.close()  # 关闭缓存
    return the_page

"保存用户的微信账号信息"
def bind_user_info():
    test_url = "http://fctest.guodong.com/api/user/login"
    c = pycurl.Curl
    data = {"username": "leizhihong",
            "pwd":"123456"}
    json_data = json.dumps(data)
    PostData(test_url, c, json_data)