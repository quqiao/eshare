#   coding:utf-8
'''
Created on 2016年6月22日
@author: quqiao
这是下单接口测试
'''

import io
from urllib import parse
import pycurl
import json




def GetDate(curl, url):
    head = ['Accept:*/*'
            ,'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
            ,"X-LC-Session:"
            ]
    buf = io.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.perform()
    the_page =buf.getvalue()
    buf.close()
    return the_page

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


if __name__ == '__main__':
    c = pycurl.Curl()  # 创建一个curl对象
    test_url1 = "http://order.api.guodong.com/Orders/CreateOrder"
    test_data1 = {"productId": "5b95ceca00017201a8c0229f",
                  "number": 1,
                  "buyerId": "5abb073d00016301a8c05d1b",
                  "returnUrl": "http://useraccount.api.guodong.com/callback",
                  "attributelist": [
                                    {"attributeId": "5b62791000028201a8c06ede",
                                     "attributeValue": "111"},  # 收货角色
                                    {"attributeId": "5b62791000038201a8c06ede",
                                     "attributeValue": "111****1111"}  # 联系电话
                                    ],
                  "version": "123456789"
                  }
    print(type(test_data1))
    test_json = json.dumps(test_data1)
    print(type(test_json))
    PostData(c, test_url1, test_json)
    pass