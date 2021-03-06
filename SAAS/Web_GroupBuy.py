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

head= {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "token":"ab7446432aa4c890b58eedcc884462c6"}

"************************************************************************"
"商品设置-商品列表"
url_list = "http://fctest.guodong.com/api/groups/goods/list"
data_list = {"weapp_id": 75}
"************************************************************************"

"************************************************************************"
"商品管理-商品详情"
url_details = "http://fctest.guodong.com/api/groups/goods/details"
data_details = {"groupsId": ""}
"************************************************************************"

"************************************************************************"
"商品管理-删除（支持批量删除）"
url_del = "http://fctest.guodong.com/api/groups/goods/del"
data_del = {"": ""}
"************************************************************************"

"************************************************************************"
"商品管理-商品添加/修改"
url_add = "http://fctest.guodong.com/api/groups/goods/del"
data_add = {"weapp_id": 75, "goods_name":"test12345", "sort":111, "original_img":""}
"************************************************************************"

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