# coding = utf-8
'''
Created on 2019年01月31日
@author: quqiao
SAAS_小程序，Web端_秒杀
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
"开放时间-修改"
url_snaptime_update = "http://fctest.guodong.com/api/websnap/snaptime/update"
data_snaptime_update = {"weapp_id": 192, "timeid[0]":19, "timeid[1]":13, "timeid[2]":7}
"************************************************************************"

"************************************************************************"
"开放时间-获取信息"
url_snaptime_get = "http://fctest.guodong.com/api/websnap/snaptime/get"
data_snaptime_get = {"weapp_id": 192}
"************************************************************************"

"************************************************************************"
"秒杀设置-过期时间获取"
url_snapaging_get = "http://fctest.guodong.com/api/websnap/snapaging/get"
data_snapaging_get = {"weapp_id": 192}
"************************************************************************"

"************************************************************************"
"秒杀设置-过期时间设置"
url_snapaging_update = "http://fctest.guodong.com/api/websnap/snapaging/update"
data_snapaging_update = {"weapp_id": 192, "time": 5}
"************************************************************************"

"************************************************************************"
"订单列表-导出订单"
url_export = "http://fctest.guodong.com/api/websnap/snaporder/export"
data_export = {"weapp_id": 75, "order_status": 1, "activityType": 1}
"order_status:订单状态 1未付款 2待发货 3待收货 4已完成 5待处理 6已取消 7异常订单"
"activityType:活动类型 活动类型 0普通 1秒杀 2团购 3预约 4拼团"
"************************************************************************"

"************************************************************************"
"订单列表-取消订单（已经支付的订单，售后订单等）"
url_cancel = "http://fctest.guodong.com/api/websnap/snaporder/cancel"
data_cancel = {"weapp_id": 75, "orderSn": 1, "agree": 1}
"orderSn:订单编号，不是order_id"
"agree:0 拒绝退款 1同意退款"
"************************************************************************"

"************************************************************************"
"评价管理-添加虚拟评价-回复"
url_reply = "http://fctest.guodong.com/api/comment/reply"
data_reply = {"weapp_id": 75, "reply": "", "comment_id": ""}
"************************************************************************"

"************************************************************************"
"评价管理-添加虚拟评价-添加/修改（同）注： 具体订单管理里面的吧"
url_multioperate = "http://fctest.guodong.com/api/comment/multioperate"
data_multioperate = {"weapp_id": 75, "reply": "", "action": "", "virtual_user": "","grade": "", "desc":"",
              "goods_id":"", "user_img":"","comment_img":"", "is_hidden":""}
"action:add 添加|update 更新|hidden 隐藏|delete 删除"
"************************************************************************"

"************************************************************************"
"评价管理-评价列表(使用:商品管理-商品列表)"
url_list = "http://fctest.guodong.com/api/websnap/snapcommit/list"
data_list = {"weapp_id": 75, "goods_id": ""}
"************************************************************************"

"************************************************************************"
"售后订单-退款 同意/拒绝"
url_operate = "http://fctest.guodong.com/api/websnap/snaporderafter/operate"
data_operate = {"weapp_id": 75, "sale_id": "", "action": ""}
"************************************************************************"

"************************************************************************"
"售后订单-订单列表"
url_order_list = "http://fctest.guodong.com/api/websnap/snaporderafter/list"
data_order_list = {"weapp_id": 75}
"************************************************************************"

"************************************************************************"
"订单列表-修改待收货跨地单号"
url_upostsingle = "http://fctest.guodong.com/api/websnap/snaporderafter/upostsingle"
data_upostsingle = {"weapp_id": 75, "orderId": "", "postSingle": ""}
"orderId:实际是是order_sn "
"postSingle: 订单号"
"************************************************************************"

"************************************************************************"
"订单列表-修改未支付订单价格"
url_uprice = "http://fctest.guodong.com/api/websnap/snaporder/uprice"
data_uprice = {"weapp_id": 75, "orderId": "", "orderPrice": ""}
"************************************************************************"

"************************************************************************"
"订单列表-发货"
url_delivery = "http://fctest.guodong.com/api/websnap/snaporder/delivery"
data_delivery = {"weapp_id": 75, "postType": "", "orderId": ""}
"************************************************************************"

"************************************************************************"
"订单列表-修改 备注|地址 （支持批量）"
url_operate = "http://fctest.guodong.com/api/websnap/snaporder/operate"
data_operate = {"weapp_id": 75, "actionName": "", "actionData": "", "orderId[]": ""}
"actionName:操作名称 (mark：备注 |updateaddress:地址）"
"actionData:操作数据"
"orderId[]:订单ID 数组"
"************************************************************************"

"************************************************************************"
"订单列表-订单详情"
url_order_detail = "http://fctest.guodong.com/api/websnap/snaporder/detail"
data_order_detail = {"weapp_id": 75, "order_id": ""}
"************************************************************************"

"************************************************************************"
"商品设置-商品秒杀详情-更新一条"
url_snapconfig_snapidupdate = "http://fctest.guodong.com/api/websnap/snapconfig/snapidupdate"
data_snapconfig_snapidupdate  = {"weapp_id": 75, "snapId": "", "snapPrice":"", "snapNum":""}
"************************************************************************"

"************************************************************************"
"商品设置-商品秒杀详情-删除一条"
url_snapconfig_snapiddel = "http://fctest.guodong.com/api/websnap/snapconfig/snapiddel"
data_snapconfig_snapiddel  = {"weapp_id": 75, "snapId": ""}
"************************************************************************"

"************************************************************************"
"商品设置-商品秒杀详情-获取"
url_snapconfig_snapdetail = "http://fctest.guodong.com/api/websnap/snapconfig/snapdetail"
data_snapconfig_snapdetail  = {"weapp_id": 75, "goodsId": "","startDate":"", "endDate":""}
"************************************************************************"

"************************************************************************"
"商品设置-按日历查看"
url_snapconfig_datelist = "http://fctest.guodong.com/api/websnap/snapconfig/snapdetail"
data_snapconfig_datelist  = {"weapp_id": 75,}
"************************************************************************"

"************************************************************************"
"商品设置-按日历查看-详情"
url_snapconfig_datedetail = "http://fctest.guodong.com/api/websnap/snapconfig/datedetail"
data_snapconfig_datedetail  = {"weapp_id": 75, "snapData":""}
"************************************************************************"

"************************************************************************"
"商品设置-删除一个商品全部秒杀活动"
url_snapconfig_alldel = "http://fctest.guodong.com/api/websnap/snapconfig/datedetail"
data_snapconfig_alldel  = {"weapp_id": 75, "goodId":""}
"************************************************************************"

"************************************************************************"
"商品设置-商品列表(支持搜索了！！！！！)"
url_snapconfig_list = "http://fctest.guodong.com/api/websnap/snapconfig/list"
data_snapconfig_list = {"weapp_id": 75, "current_page":"", "per_page":"", "search":""}
"************************************************************************"

"************************************************************************"
"商品设置-添加秒杀商品-可用开放时间"
url_snapconfig_snaptime = "http://fctest.guodong.com/api/websnap/snapconfig/snaptime"
data_snapconfig_snaptime = {"weapp_id": 75,}
"************************************************************************"

"************************************************************************"
"商品设置-添加秒杀商品-保存"
url_snapconfig_save = "http://fctest.guodong.com/api/websnap/snapconfig/save"
data_snapconfig_save = {"weapp_id": 75,"goodsId":"", "specList":"","snapTime[0]":"",
                        "snapData[0]":"","snapNumLimit":"","snapOrderLimit":""}
"goodsId:商品ID"
"specList:json数据|配置数据 详情见说明|itemId（规格ID） ，snapPrice（秒杀价格），snapNum（秒杀数量）"
"snapTime[]:数组|秒杀时间段 实际是是timeId的数值"
"snapData[]:数组|秒杀日期"
"snapNumLimit:每个订单限制购买数量，填写0表示不限购，默认不限购"
"snapOrderLimit:活动限购订单数，填写0表示不限单，默认不限单"
"************************************************************************"

"************************************************************************"
"商品设置-添加秒杀商品-收索商品"
url_snapconfig_goodsearch = "http://fctest.guodong.com/api/websnap/snapconfig/goodsearch"
data_snapconfig_goodsearch = {"weapp_id": 75,"search":""}
"************************************************************************"

"************************************************************************"
"商品管理-批量处理"
url_snapgoods_Multi = "http://fctest.guodong.com/api/websnap/snapgoods/Multi"
data_snapgoods_Multi = {"goods_id_arr[0]": 1000614, "goods_id_arr[1]": 1000611, "action": "on_sale",
                        "give_integral":"","exchange_integral":"","weapp_id":192}
"goods_id_arr[]:商品iD 数组"
"action:on_sale 上架|off_sale 下下架|del 删除|set_integral 设置积分"
"give_integral:增送的积分"
"exchange_integral:	最大可使用积分"
"************************************************************************"

"************************************************************************"
"商品管理-商品详情"
url_snapgoods_detail = "http://fctest.guodong.com/api/websnap/snapgoods/detail"
data_snapgoods_detail = {"goods_id": "1000614", "weapp_id": 192}
"************************************************************************"

"************************************************************************"
"商品管理-商品添加/修改"
url_snapgoods_save = "http://fctest.guodong.com/api/websnap/snapgoods/save"
data_snapgoods_save = {"goods_name": "testjiekou001", "original_img": "http://wxmiimage.esharex.com/m_1/shop/15490048384763.jpeg",
                       "goods_images[0]": "http://wxmiimage.esharex.com/m_1/shop/15489194475332.jpeg", "shop_price": 199,
                       "original_price": 259, "template_id": 0, "store_count": 99, "support_discount":1, "support_coupon":1,
                       "weapp_id":192, "mobile_content": "<p>hahaha</p>","shipping_type":2}

"************************************************************************"

"************************************************************************"
"商品管理-商品列表（支持搜索了！！！！）"
url_snapgoods_get = "http://fctest.guodong.com/api/websnap/snapgoods/get"
data_snapgoods_get = {"weapp_id": 192, "per_page": 10, "page":1, "onSale": 0, "search":""}
"************************************************************************"


def PostData():
    data2 = parse.urlencode(data_multioperate).encode('utf-8')
    req = request.Request(url_multioperate, headers=head, data=data2)
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


if __name__ == '__main__':
    for t in threads:
        t.start()