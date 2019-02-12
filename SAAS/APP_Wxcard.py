# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，小程序端_卡券
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
"领卡-领卡回调与用户建立联系"
url_code = "https://fctest.guodong.com/app/weapp/wxcard/code"
data_code = {"code": ""}
"************************************************************************"

"************************************************************************"
"领卡-获取会员卡信息"
url_code = "https://fctest.guodong.com/app/weapp/wxcard/info"
data_code = {"code":"","cardId":""}
"************************************************************************"

"************************************************************************"
"领卡-领取卡券"
url_add = "https://fctest.guodong.com/app/weapp/wxcard/add"
data_add = {"cardExt": "", "cardId": ""}
"************************************************************************"


def PostData():
    data2 = parse.urlencode(data_add).encode('utf-8')
    req = request.Request(url_add, headers=head, data=data2)
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