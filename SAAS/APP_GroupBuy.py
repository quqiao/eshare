# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，小程序端_组团
'''
from urllib import parse
from urllib import request
import threading
import time

head= {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "token":"ab7446432aa4c890b58eedcc884462c6"}

"************************************************************************"
"用户-取消订单（未支付的订单）"
url_cancel = "https://fctest.guodong.com/app/weapp/groups/cancel"
data_cancel = {"orderSn": "1"}
"************************************************************************"

"************************************************************************"
"商城-商品列表"
url_hot = "https://fctest.guodong.com/app/weapp/groups/goods/hot"
data_hot = {"weapp_id": 75}
"************************************************************************"

"************************************************************************"
"用户-订单详情"
url_details = "https://fctest.guodong.com/app/weapp/groups/order/details"
data_details = {"groupsColonelId": 75}
"************************************************************************"

"************************************************************************"
"用户-我的订单"
url_my = "https://fctest.guodong.com/app/weapp/groups/order/my"
data_my = {"status": 0, "page": 1, "per_page": 10}
"************************************************************************"

"************************************************************************"
"用户-邀请/支付后显示的界面"
url_groupnum = "https://fctest.guodong.com/app/weapp/groups/groupnum"
data_groupnum = {"groupsNum": 0}
"************************************************************************"

"************************************************************************"
"用户-申请支付"
url_pay = "https://fctest.guodong.com/app/weapp/groups/pay"
data_pay = {"order_sn": 0}
"************************************************************************"

"************************************************************************"
"商品-参团"
url_groupjoin = "https://fctest.guodong.com/app/weapp/groups/groupjoin"
data_groupjoin = {"groupsNum": "", "groupsId":"", "itemId":"", "addressId":"", "pickType":"","payType":""}
"groupsNum:团号"
"groupsId:拼团ID"
"itemId:规格ID 默认为 0"
"addressId:地址ID"
"pickType:取货方式"
"payType:付款方式 "
"************************************************************************"

"************************************************************************"
"商品-开团"
url_groupopen = "https://fctest.guodong.com/app/weapp/groups/groupopen"
data_groupopen = {"groupsNum": "", "groupsId":"", "itemId":"", "addressId":"", "pickType":"","payType":""}
"groupsNum:团号"
"groupsId:拼团ID"
"itemId:规格ID 默认为 0"
"addressId:地址ID"
"pickType:取货方式"
"payType:付款方式 "
"************************************************************************"

"************************************************************************"
"商品-详情-正在拼团的团（当前拼团商品）"
url_grouplist = "https://fctest.guodong.com/app/weapp/groups/grouplist"
data_grouplist = {"groupsId":""}
"************************************************************************"

"************************************************************************"
"商品-商品详情"
url_grouplist = "https://fctest.guodong.com/app/weapp/goods/detail"
data_grouplist = {"groupsId":"","itemId":0}
"************************************************************************"

def PostData():
    data2 = parse.urlencode(data_cancel).encode('utf-8')
    req = request.Request(url_cancel, headers=head, data=data2)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 = eval(page1)
    print(page2)
    print(time.time())




threads = []
for i in range(1):
    t1 = threading.Thread(target=PostData)
    threads.append(t1)
    # t2 = threading.Thread(target=list)
    # threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()