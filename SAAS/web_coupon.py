# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，web端_优惠券
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
    "token": "y6DnwBSzu3GrzaTIVT4AA2kCQ49pPAphupkwMGE5LKIZfDHp2p3i1P38ihXj1jwB"
}

"************************************************************************"
"优惠券列表"
url_list = "http://fctest.guodong.com/api/coupon/list?page=1&per_page=10&weapp_id=192"
"************************************************************************"

"************************************************************************"
"优惠券管理操作"
url_multioperate = "https://api.365fengchao.com/api/coupon/multioperate"
data_multioperate = {"weapp_id": 192, "action": "delete", "coupon_name": "通用券", "lowest_consume": 20,
                     "preferential_money": 10, "effective_days": 5,  "coupon_count": 10, "effective_type": 1,
                     "coupon_type": 2, "add_center": 1, "sort":20,"coupon_id":500,"userid_str":192}
"action:操作名称,add、delete、update、provide"
"coupon_name:优惠券名称"
"lowest_consume:最低消费"
"preferential_money:优惠金额"
"effective_days:有效天数"
"coupon_count:优惠券发放总数"
"effective_type:"
"coupon_type:优惠券类型 1 满减券 2通用券"
"add_center:加入领券中心1是 0否"
"************************************************************************"
"自动发放设置"
url_releasecoupon_mutioperate = "http://fctest.guodong.com/api/releasecoupon/multioperate"
data_releasecoupon_mutioperate = {"action": "add", "trigger_event": 1, "limit": 10, "coupon_id": 72,
                                  "weapp_id": 192}
"action:操作名称：add、delete、update、provide"
"trigger_event：触发事件，1页面转发 2购买并付款"
"limit:限制次数,优惠券发放限制次数"
"coupon_id:优惠券表主键ID"
"************************************************************************"

"************************************************************************"
"自动发放列表"
url_releasecoupon_list = "http://fctest.guodong.com/api/releasecoupon/list?page=1&per_page=10&weapp_id=75"
"************************************************************************"

def GetData():
    req = request.Request(url_list, headers=head)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    print(page1)
    page2 = page1.replace("null", "222")
    page3 = eval(page2)
    print(page3)
    # print(time.time())

def PostData():
    data2 = parse.urlencode(data_multioperate).encode('utf-8')
    req = request.Request(url_multioperate, headers=head, data=data2)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 = eval(page1)
    print(page2)
    # print(time.time())
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