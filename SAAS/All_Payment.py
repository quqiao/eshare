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

head = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11",
    "Content-Type": "application/x-www-form-urlencoded",
    "token": "d2dd77242b4ac355debd4ae5ffc11580"
    }

"************************************************************************"
"领取优惠券"
url_accept = "https://api.365fengchao.com/app/weappcoupon/accept?coupon_id=264"
"************************************************************************"

"************************************************************"
"小程序添加订单以及微信公众号支付统一下单"
url_addorder = "https://api.365fengchao.com/app/weapporder/addorder"
data_addorder = {
"action": "orderpay",
"goodsinfo": "{\"count\":1,\"discount\":\"10\",\"freight\":0,\"goods_amount\":998,\"pay_amount\":998,\"mobile\":\"18256989988\",\"consignee\":\"111\",\"address\":\"北京北京市东城区111\",\"goods\":[{\"goods_id\":1000490,\"item_id\":\"\",\"goods_name\":\"750*2912裁剪上传\",\"goods_images\":\"http://wxmiimage.esharex.com/m_1/shop/15469169138062.png\",\"spec_name\":\"\",\"goods_price\":\"998.00\",\"goods_num\":1}],\"remark\":\"\",\"actual_money\":0,\"actual_integral\":0,\"get_integral\":0,\"coupon_list_id\":0}",
"type": "immebuy"}
"**************************************************************"

"**************************************************************"
"订单-支付"
url_order2_pay = "https://api.365fengchao.com/app/weapporder/pay?order_sn=19040421041711943203&payType=2"  # 余额支付
url_order5_pay = "https://api.365fengchao.com/app/weapporder/pay?order_sn=19040421100611954326&payType=5"  # 微信支付
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
# url_seckill_order = "https://api.365fengchao.com/app/snap/app/order"
# data_seckill_order = {{"goodsinfo":"{\"count\":1,\"discount\":\"1.99\",\"freight\":0,\"goods_amount\":19.9,\"pay_amount\":1.91,\"mobile\":\"13589885566\",\"consignee\":\"老罗\",\"address\":1652,\"goods\":[{\"accumulate_deduct\":1,\"deduct_all\":1,\"exchange_integral\":\"0\",\"goods_id\":1001394,\"goods_images\":\"http://wxmiimage.esharex.com/formal/m_115/weapp_220/shop/goods/15518663376936.jpeg\",\"goods_name\":\"秒杀水果\",\"free_post_num\":null,\"free_post_amount\":null,\"item_id\":0,\"support_coupon\":1,\"template_id\":0,\"support_discount\":1,\"snap_id\":7352,\"snap_num_limit\":0,\"goods_price\":\"19.90\",\"spec_name\":\"默认\",\"other_price\":\"19.90\",\"goods_num\":\"1\",\"vip_price\":\"1.99\",\"discount_price\":17.91,\"integral_price\":17.91,\"snapId\":\"7352\"}],\"remark\":\"\",\"actual_money\":\"9.00\",\"actual_integral\":70,\"coupon_list_id\":326}","payType":5,"snapId":"7352"}}
"************************************************************"

"************************************************************"
"秒杀-支付"
url_seckill_pay = "https://api.365fengchao.com/app/snap/app/order/pay"
data_seckill_pay = {"order_sn": "19032019340287711699", "payType": 5}
"************************************************************"

"************************************************************"
"充值-下单"
url_recharge_order = "https://api.365fengchao.com/app/weapp/recharge/order"
data_recharge_order = {"amount": "0.01"}
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
    t1 = threading.Thread(target=GetData)
    threads.append(t1)
    # t2 = threading.Thread(target=GetData)
    # threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()