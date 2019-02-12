# coding=utf-8
'''
Created on 2019年01月31日
@author: quqiao
SAAS_小程序，小程序端_分裂红包
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

"************************************************************"
"首页弹窗判断"
url_popup = "https://fctest.guodong.com/app/fxhb/popup"
"************************************************************"

"************************************************************"
"分裂红包页面"
url_redpacket = "https://fctest.guodong.com/app/fxhb/redpacket"
"************************************************************"

"************************************************************"
"领取或查看红包"
url_receive = "https://fctest.guodong.com/app/fxhb/receive"
"************************************************************"

"************************************************************"
"拆分分裂红包"
url_split = "https://fctest.guodong.com/app/fxhb/split"
"************************************************************"


def GetData():
    req = request.Request(url_popup, headers=head)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 =eval(page1)
    print(page2)
    print(time.time())


threads = []
for i in range(1):
    t1 = threading.Thread(target=GetData)
    threads.append(t1)
    # t2 = threading.Thread(target=list)
    # threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()