# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，小程序端_订单
'''
from urllib import parse
from urllib import request
import threading
import time

head = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "token": "9963dd9fa6cdd8e131e3691dc8f499a4"
}

"**********************************************************************"
"订单列表"
url_list = "https://api.365fengchao.com/app/weapporder/list"
data_list = {
"order_status": 3,  # 订单状态 1待付款 2待发货 3待收货 4已完成
"per_page": 10,
"page": 1
}
"************************************************************"

"************************************************************"
"订单详情"
url_detail = "https://api.365fengchao.com/app/weapporder/detail?order_id=269"
"************************************************************"

"************************************************************"
"小程序添加订单以及微信公众号支付统一下单"
url_addorder = "https://api.365fengchao.com/app/weapporder/addorder"
data_addorder = {
"action": "orderpay",
"goodsinfo": "{\"count\":1,\"discount\":\"10\",\"freight\":0,\"goods_amount\":998,\"pay_amount\":998,\"mobile\":\"18256989988\",\"consignee\":\"111\",\"address\":\"北京北京市东城区111\",\"goods\":[{\"goods_id\":1000490,\"item_id\":\"\",\"goods_name\":\"750*2912裁剪上传\",\"goods_images\":\"http://wxmiimage.esharex.com/m_1/shop/15469169138062.png\",\"spec_name\":\"\",\"goods_price\":\"998.00\",\"goods_num\":1}],\"remark\":\"\",\"actual_money\":0,\"actual_integral\":0,\"get_integral\":0,\"coupon_list_id\":0}",
"type": "immebuy"}
"**************************************************************"

"**************************************************************"
"结算时积分抵扣或者使用优惠券"
url_deduction = "https://api.365fengchao.com/app/weapporder/deduction"
data_deduction = {
    "deductinfo": "{\"is_use\":1,\"coupon_list_id\":127}",
    "pay_amount": 1
}
"*************************************************************"

"*************************************************************"
"删除订单"
url_del_order = "https://api.365fengchao.com/app/weapporder/del_order?order_id=242"
"*************************************************************"

"*************************************************************"
"结算"
url_settle = "https://api.365fengchao.com/app/weapporder/settle"
data_settle = {"action": "cart", "city_id": 110100}
"*************************************************************"

def GetData():
    req = request.Request(url_detail, headers=head)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 = page1.replace("null", "222")
    page3 = eval(page2)
    print(page3)
    print(time.time())


def PostData():
    data2 = parse.urlencode(data_deduction).encode('utf-8')
    req = request.Request(url_deduction, headers=head, data=data2)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 = page1.replace("null", "222")
    page3 = eval(page2)
    print(page3)
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