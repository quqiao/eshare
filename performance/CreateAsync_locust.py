from locust import HttpLocust, TaskSet, task
import json


# 定义用户行为
class UserBehavior(TaskSet):
    def on_start(self):
        print("start test")

    @task(2)
    def logOut(self):
        self.interrupt()

    @task(1)
    def UserLoginAsync(self):

        head = {
                "Accept": "application/json",
                "Content-Type": "application/json"}
        data = {"productInfo": {"gameId": "5b96086a00018201a8c05688",
                                "areaId": "5b9608b400018201a8c05688",
                                "serverId ": "5b9608d100018201a8c05688",
                                "categoryId": "5b9608f200018201a8c05688",
                                "sellerId": "5abb073d00016301a8c05d1b",
                                "safeguardId": 0,
                                "tradeType": 2,
                                "attributes": [
                                  {"attributeId": "5b960a0c00018201a8c078f0",
                                   "attributeValue": 111},    # 商品标题
                                  {"attributeId": "5b960a2d00018201a8c078f0",
                                   "attributeValue": 222},       # 商品单件
                                  {"attributeId": "5b960a3d00018201a8c078f0",
                                   "attributeValue": 20},       # 发布数量
                                  {"attributeId": "5b960a4800018201a8c078f0",
                                   "attributeValue": 333},       # 单价数量
                                  {"attributeId": "5b960abd00018201a8c078f0",
                                   "attributeValue": 444},       # 商品描述
                                  {"attributeId": "5b960d3900018201a8c078f0",
                                   "attributeValue": 555},       # 发货方式
                                      ]},
                "accountInfo": {"attributes": [
                                            {"attributeId": "5b96097100018201a8c078f0",
                                             "attributeValue": "test11"},       # 游戏账号
                                            {"attributeId": "5b96099200018201a8c078f0",
                                             "attributeValue": "test12"},       # 游戏角色
                                            {"attributeId": "5b9609ac00018201a8c078f0",
                                             "attributeValue": 123456},       # 联系方式
                                            {"attributeId": "5b9609c000018201a8c078f0",
                                             "attributeValue": 123456}        # 密码
                              ]},
                "serviceInfo": {"isPledge": True,
                                "tradeStartTime": "17:00",
                                "tradeEndTime": "24:00",
                                "validity": 15,
                                "enabledPledge": True},
                "payCallBackUrl": "http://useraccount.api.guodong.com/callback"
            }
        data1 = json.dumps(data)
        with self.client.post("Product/CreateAsync", headers=head, data=data1,catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')


class WebsiteUser(HttpLocust):
    host = "http://product.api.guodong.com/"
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    stop_timeout = 10
    weight = 1