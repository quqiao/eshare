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

def CreateAsync():
    test_url1 = "http://product.api.guodong.com/Product/CreateAsync"
    c = pycurl.Curl()
    data1 ={"productInfo": {"gameId": "5b96086a00018201a8c05688",
                            "areaId": "5b9608b400018201a8c05688",
                            "serverId ": "5b9608d100018201a8c05688",
                            "categoryId": "5b9608f200018201a8c05688",
                            "sellerId": "5abb073d00016301a8c05d1b",
                            "safeguardId": 0,
                            "tradeType": 2,
                            "attributes": [
                                  {"attributeId": "5b960a0c00018201a8c078f0",
                                   "attributeValue": 111},    # 商品标题
                                  {"attributeId": "5b960a2d00018201a8c078f0",
                                   "attributeValue": 222},       # 商品单件
                                  {"attributeId": "5b960a3d00018201a8c078f0",
                                   "attributeValue": 20},       # 发布数量
                                  {"attributeId": "5b960a4800018201a8c078f0",
                                   "attributeValue": 333},       # 单价数量
                                  {"attributeId": "5b960abd00018201a8c078f0",
                                   "attributeValue": 444},       # 商品描述
                                  {"attributeId": "5b960d3900018201a8c078f0",
                                   "attributeValue": 555},       # 发货方式
                              ]},
              "accountInfo": {"attributes": [
                                            {"attributeId": "5b96097100018201a8c078f0",
                                             "attributeValue": "test11"},       # 游戏账号
                                            {"attributeId": "5b96099200018201a8c078f0",
                                             "attributeValue": "test12"},       # 游戏角色
                                            {"attributeId": "5b9609ac00018201a8c078f0",
                                             "attributeValue": 123456},       # 联系方式
                                            {"attributeId": "5b9609c000018201a8c078f0",
                                             "attributeValue": 123456}        # 密码
                              ]},
              "serviceInfo": {"isPledge": True,
                              "tradeStartTime": "17:00",
                              "tradeEndTime": "24:00",
                              "validity": 15,
                              "enabledPledge": True},
              "payCallBackUrl": "http://useraccount.api.guodong.com/callback"
            }
    test_json = json.dumps(data1)
    PostData(c, test_url1, test_json)
    print(time.time())



threads = []
t1 = threading.Thread(target=CreateAsync)
threads.append(t1)
t2 = threading.Thread(target=CreateAsync)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()