#coding=utf-8
'''
Created on 2016年7月27日
@author: quqiao
'''

import io
import pycurl
import threading
import json
import time

def PostData(curl, url, data):
    # head = ["Accept:*/*"
    #         , "User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
    #         , 'Accept:*/*'
    #         , "application/json"
    #         , 'Content-Type:*/*'
    #         , "application/json"
    #         ]
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

def login():
    test_url1 = "http://userpassport.api.guodong.com/Password/UserLoginAsync"
    c = pycurl.Curl()
    data1 = {"phone": "13512345678", "password": "123456"}
    test_json = json.dumps(data1)
    PostData(c, test_url1, test_json)
    print(time.time())



threads = []
t1 = threading.Thread(target=login)
threads.append(t1)
t2 = threading.Thread(target=login)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
