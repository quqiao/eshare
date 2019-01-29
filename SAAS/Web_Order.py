# coding = utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，Web端_订单
'''

from urllib import parse
from urllib import request
import threading
import time
import json

head = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "token": "IYFcmQvZcdPsaryOAnFlr7yCGnl00k04staPxgopEbbZpezI45nRjzHqwbsl5YeM"
}
"************************************************************************"
"订单详情"
url_detail = "http://fctest.guodong.com/api/order/detail?order_id=280&weapp_id=75"
"************************************************************************"

"************************************************************************"
"售后订单"
url_list = "http://fctest.guodong.com/api/aftersale/list"
data_list = {"weapp_id": 75}
"************************************************************************"

"************************************************************************"
"评价管理"
url_comment = "http://fctest.guodong.com/api/comment/list"
data_comment = {"weapp_id": 75}
"************************************************************************"

"************************************************************************"
"虚拟评价编辑"
url_multioperate = "http://fctest.guodong.com/api/comment/multioperate"
data_multioperate = {"weapp_id": 75, "virtual_user": "111", "grade": 0, "is_hidden": 0,"action": "add",
                     "goods_id": 1000513
                     }
"************************************************************************"

"************************************************************************"
"虚拟评价回复"
url_reply = "http://fctest.guodong.com/api/comment/reply"
data_reply = {"comment_id": 32, "reply": "222", "weapp_id": 75}
"************************************************************************"

"************************************************************************"
"订单列表"
url_orderlist = "http://fctest.guodong.com/api/order/list?page=1&per_page=10&type=1&order_sn=&order_status=&start_time=&end_time=&weapp_id=75"
"************************************************************************"

def GetData():
    req = request.Request(url_detail, headers=head)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    print(page1)
    page2 = page1.replace("null", "222")
    page3 = eval(page2)
    print(page3)
    print(time.time())

def PostData():
    data2 = parse.urlencode(data_list).encode('utf-8')
    req = request.Request(url_list, headers=head, data=data2)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 = eval(page1)
    print(page2)
    print(time.time())
    return page2

threads = []
for i in range(1):
    t1 = threading.Thread(target=PostData)
    threads.append(t1)
    # t2 = threading.Thread(target=list)
    # threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()