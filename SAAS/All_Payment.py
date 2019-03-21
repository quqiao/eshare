# coding=utf-8
'''
Created on 2019年03月18日
@author: quqiao
SAAS_小程序，小程序端_订单
'''

from urllib import parse
from urllib import request
import threading
import time

head= {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11",
    "Content-Type": "application/x-www-form-urlencoded",
    "token": "b682f6e12f6fc7945e4a9acc2f1ecdae"
    }

"************************************************************************"
"领取优惠券"
url_accept = "https://api.365fengchao.com/app/weappcoupon/accept?coupon_id=168"
"************************************************************************"

"************************************************************"
"小程序添加订单以及微信公众号支付统一下单"
url_addorder = "https://api.365fengchao.com/app/weapporder/addorder"
data_addorder = {
"action": "orderpay",
"goodsinfo": "{\"count\":1,\"discount\":\"10\",\"freight\":0,\"goods_amount\":998,\"pay_amount\":998,\"mobile\":\"18256989988\",\"consignee\":\"111\",\"address\":\"北京北京市东城区111\",\"goods\":[{\"goods_id\":1000490,\"item_id\":\"\",\"goods_name\":\"750*2912裁剪上传\",\"goods_images\":\"http://wxmiimage.esharex.com/m_1/shop/15469169138062.png\",\"spec_name\":\"\",\"goods_price\":\"998.00\",\"goods_num\":1}],\"remark\":\"\",\"actual_money\":0,\"actual_integral\":0,\"get_integral\":0,\"coupon_list_id\":0}",
"type": "immebuy"}
"**************************************************************"

"************************************************************"
"分销中心-提现"
url_cashApply = "https://fctest.guodong.com/app/seller/cashApply"
data_cashApply = {"money": "2", "cash_way": "0", "name": "111", "account": "111", "seller_id": 65}
"************************************************************"

"************************************************************"
"我的订单-待收货-退款"
url_apply_refund = "https://api.365fengchao.com/app/weapporder/apply_refund?order_id=661"
"************************************************************"

"************************************************************"
"秒杀-下单"
url_seckill_order = "http://fctest.guodong.com/app/snap/app/order"
data_seckill_order = {"goodsinfo":"{\"count\":1,\"discount\":\"0.00\",\"freight\":0,\"goods_amount\":80,\"pay_amount\":80,\"mobile\":\"18025695588\",\"consignee\":\"uu\",\"address\":1629,\"goods\":[{\"accumulate_deduct\":0,\"deduct_all\":0,\"exchange_integral\":null,\"goods_id\":1000866,\"goods_images\":\"http://wxmiimage.esharex.com/m_1/shop/15490892581591.jpeg\",\"goods_name\":\"这是一个运动鞋\",\"free_post_num\":null,\"free_post_amount\":null,\"item_id\":0,\"support_coupon\":1,\"support_discount\":0,\"snap_id\":24151,\"snap_num_limit\":0,\"goods_price\":\"80.00\",\"spec_name\":\"默认\",\"other_price\":\"80.00\",\"goods_num\":\"1\",\"vip_price\":\"0.00\",\"discount_price\":80,\"integral_price\":0,\"snapId\":\"24151\"}],\"remark\":\"\",\"actual_money\":0,\"actual_integral\":0,\"coupon_list_id\":0}","payType":5,"snapId":"24151"}
"************************************************************"

"************************************************************"
"秒杀-支付"
url_seckill_pay = "http://fctest.guodong.com/app/snap/app/order/pay"
data_seckill_pay = {"order_sn":"19032116110319741586"}
"************************************************************"

def GetData():
    req = request.Request(url_accept, headers=head)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 = page1.replace("null", "222")
    page3 = eval(page2)
    print(page3)
    print(time.time())

def PostData():
    data2 = parse.urlencode(data_seckill_pay).encode('utf-8')
    req = request.Request(url_seckill_pay, headers=head, data=data2)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 = eval(page1)
    print(page2)
    print(time.time())

threads = []
for i in range(1):
    t1 = threading.Thread(target=PostData)
    threads.append(t1)
    # t2 = threading.Thread(target=PostData)
    # threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()