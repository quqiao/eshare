# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，小程序端_用户
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
    "token":"737611bf031309f09ec661024026a8fe"}

"************************************************************************"
"用户登录"
url_user = "http://fctest.guodong.com/api/weapp/gettoken"
data_user = {"js_code": "",
            "weapp_id": "https://wx.qlogo.cn/mmopen/vi_32/icc2nhPAgI52YBbZqSBJ",
            "key":""}
"************************************************************************"


def PostData():
    data2 = parse.urlencode(data_user).encode('utf-8')
    req = request.Request(url_user, headers=head, data=data2)
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