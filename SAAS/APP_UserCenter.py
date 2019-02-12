# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
SAAS_小程序，小程序端_用户中心
'''

from urllib import parse
from urllib import request
import threading
import time

head = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11",
    "Content-Type": "application/x-www-form-urlencoded",
    "token": "92a7b40ccad44110c329f07cd59d8b46"
}

"************************************************************************"
"保存用户的微信账号信息"
url_bind_user_info = "http://fctest.guodong.com/app/usercenter/bind_user_info"
data_bind_user_info = {"userInfo": {"nickName": "hello_word",
                 "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/icc2nhPAgI52YBbZqSBJ"
                }}
"************************************************************************"

"************************************************************************"
"充值设置"
url_setting = "http://fctest.guodong.com/app/usercenter/bind_user_info"
"************************************************************************"

def GetData():
    req = request.Request(url_setting, headers=head)
    page = request.urlopen(req).read()
    page1 = page.decode('utf-8')
    page2 =eval(page1)
    print(page2)
    print(time.time())


def PostData():
    data2 = parse.urlencode(data_bind_user_info).encode('utf-8')
    req = request.Request(url_bind_user_info, headers=head, data=data2)
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
