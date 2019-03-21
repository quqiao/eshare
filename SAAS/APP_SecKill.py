# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，Web端_组团
'''
from urllib import parse
from urllib import request
import threading
import time

head = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate, br",
    "token": "7192403eda53a41988de5d88baf73ca2",
    "Connection": "keep-alive"
}


"************************************************************************"
"秒杀-用户-取消未支付订单"
url_cancel = "https://fctest.guodong.com/app/snap/app/order/cancel"
data_cancel = {"snapId": "3224", "goodsNum": "1", "addressId": 110100}
"orderSn:订单order_sn编号"
"************************************************************************"

"************************************************************************"
"秒杀-商城-结算"
url_settlement = "https://fctest.guodong.com/app/snap/app/order/settlement"
data_settlement = {"snapId": "9626", "goodsNum": "1", "addressId": 110100}
"snapId:秒杀ID"
"goodsNum:商品数量"
"addressId:不传为默认地址"
"************************************************************************"

"************************************************************************"
"秒杀-用户-申请退款"
url_refund = "https://fctest.guodong.com/app/snap/app/user/refund"
data_refund = {"order_id": ""}
"************************************************************************"

"************************************************************************"
"秒杀-用户-订单详情"
url_orderdetail = "https://fctest.guodong.com/app/snap/app/user/orderdetail"
data_orderdetail = {"order_id": ""}
"************************************************************************"

"************************************************************************"
"秒杀-用户-订单列表（包括售后）"
url_orderlist = "https://fctest.guodong.com/api/snap/app/user/orderlist"
data_orderlist = {"weapp_id": "", "order_status": 1, }
"order_status:订单状态 1未付款 2待发货 3待收货 4已完成 6已取消 1010 售后订单"
"************************************************************************"

"************************************************************************"
"秒杀-商城-申请支付"
url_pay = "https://fctest.guodong.com/app/snap/app/order/pay"
data_pay = {"order_sn": "019021405360562134"}
"************************************************************************"

"************************************************************************"
"秒杀-商城-下订单"
url_order = "https://fctest.guodong.com/app/snap/app/order"
data_order = {"snapId": "9626", "goodsNum": "1", "addressId": 1629, "integralNum": 0, "cityId": 110100, "pickType": "1",
              "payType": "5","couponListId":"","invoice_title":"","order_mark":""}
"snapId:秒杀商品秒杀ID"
"goodsNum:商品数量"
"addressId:地址ID"
"integralNum:抵扣积分数量"
"cityId:城市ID"
"************************************************************************"

"************************************************************************"
"秒杀-商城-商品评价信息"
url_eval = "https://fctest.guodong.com/api/snap/app/eval"
data_eval = {"goodsId": "", "commitType": ""}
"commitType 1 有图 2好评 3中品 4差评 其他 0 全部"
"************************************************************************"

"************************************************************************"
"秒杀-商城-商品详情（没有传商品规格为默认第一个规格）"
url_detail = "https://fctest.guodong.com/app/snap/app/detail"
data_detail = {"weapp_id": "", "goodsId": "","snapTime":"","snapDate":"","itemId":""}
"************************************************************************"

"************************************************************************"
"秒杀-商城-商品列表"
url_list = "https://fctest.guodong.com/app/snap/app/list"
data_list = {"snapTime": 19, "snapDate": "2019-02-02"}
"************************************************************************"

"************************************************************************"
"秒杀-商城-可秒杀时段"
url_time = "https://fctest.guodong.com/api/snap/app/time"
data_time = {"snapDate": "2019-02-02", "snapTime": "1"}
"************************************************************************"

def PostData():
    data2 = parse.urlencode(data_order).encode('utf-8')
    req = request.Request(url_order, headers=head, data=data2)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    print(page1)
    page2 = page1.replace("false", "222")
    page3 = eval(page2)
    print(page3)
    # print(time.time())


threads = []
for i in range(1):
    t1 = threading.Thread(target=PostData)
    threads.append(t1)
    # t2 = threading.Thread(target=list)
    # threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()