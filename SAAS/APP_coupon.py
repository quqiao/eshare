# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，小程序端_优惠券
'''
from urllib import parse
from urllib import request
import threading
import time

head= {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11",
    "Content-Type": "application/x-www-form-urlencoded",
    "token": "92a7b40ccad44110c329f07cd59d8b46"
}

"************************************************************************"
"优惠券列表"
url_list = "http://fctest.guodong.com/app/weappcoupon/list?status=0"
#data_list = {"status": 0,}  # 0未使用 1已使用 2已过期

"************************************************************************"

"************************************************************************"
"领券中心满减券"
url_minus = "http://fctest.guodong.com/app/weappcoupon/minus"
"************************************************************************"

"************************************************************************"
"领取优惠券"
url_accept = "https://fctest.guodong.com/app/weappcoupon/accept?coupon_id=127"
"************************************************************************"

"************************************************************************"
"引流系统扫码优惠券回调"
url_getflow = "https://fctest.guodong.com/app/weappcoupon/getflow?code=117"
"************************************************************************"


def GetData():
    req = request.Request(url_accept, headers=head)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 =eval(page1)
    print(page2)
    print(time.time())


# def PostData():
#     data2 = parse.urlencode(data_list).encode('utf-8')
#     req = request.Request(url_list, headers=head, data=data2)
#     page = request.urlopen(req).read()
#     page1 = page.decode('utf-8')
#     page2 = eval(page1)
#     print(page2)
#     print(time.time())

threads = []
for i in range(1):
    t1 = threading.Thread(target=GetData)
    threads.append(t1)
    # t2 = threading.Thread(target=list)
    # threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()