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

head= {
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11",
    "Accept":"application/json",
    "Content-Type":"application/json",
    "token":"737611bf031309f09ec661024026a8fe"
}

"**********************************************************************"
"订单列表"
url_list = "https://fctest.guodong.com/app/weapporder/list"
data_list = {
"order_status": 1,  # 订单状态 1待付款 2待发货 3待收货 4已完成
"per_page": 10,
"page": 1
}
"************************************************************"

"************************************************************"
"订单详情"
url_detail = "https://fctest.guodong.com/app/weapporder/detail?order_id=269"
"************************************************************"

"************************************************************"
"小程序添加订单以及微信公众号支付统一下单"
url_addorder = "https://fctest.guodong.com/app/weapporder/addorder"
data_addorder = {
"action": "orderpay",
"goodsinfo": "{\"count\":1,\"discount\":\"10\",\"freight\":0,\"goods_amount\":998,\"pay_amount\":998,\"mobile\":\"18256989988\",\"consignee\":\"111\",\"address\":\"北京北京市东城区111\",\"goods\":[{\"goods_id\":1000490,\"item_id\":\"\",\"goods_name\":\"750*2912裁剪上传\",\"goods_images\":\"http://wxmiimage.esharex.com/m_1/shop/15469169138062.png\",\"spec_name\":\"\",\"goods_price\":\"998.00\",\"goods_num\":1}],\"remark\":\"\",\"actual_money\":0,\"actual_integral\":0,\"get_integral\":0,\"coupon_list_id\":0}",
"type": "immebuy"}

"**************************************************************"

"**************************************************************"
"结算时积分抵扣或者使用优惠券"
url_deduction = "https://fctest.guodong.com/app/weapporder/deduction"
data_deduction = {
    "deductinfo": "{\"is_use\":1,\"actual_money\":5}",
    "pay_amount": 20
}
"*************************************************************"

"*************************************************************"
"删除订单"
url_del_order = "https://fctest.guodong.com/app/weapporder/del_order?order_id=269"
"*************************************************************"

"*************************************************************"
"结算"
url_settle = "https://fctest.guodong.com/app/weapporder/settle"
data_settle = {

}
"*************************************************************"

def GetData():
    req = request.Request(url_detail, headers=head)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 =eval(page1)
    print(page2)
    print(time.time())


def PostData():
    data2 = parse.urlencode(data_list).encode('utf-8')
    req = request.Request(url_list, headers=head, data=data2)
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