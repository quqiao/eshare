from locust import HttpLocust, TaskSet, task
import json
from random import randint


# 定义用户行为
class UserBehavior(TaskSet):
    # def on_start(self):
    #     print("start test")
    #
    # @task(2)
    # def logOut(self):
    #     self.interrupt()

    # @task(1)
    # def getProductList(self):
    #
    #     head = {
    #             "Accept": "application/json",
    #             "Content-Type": "application/json"}
    #     data = {"wid": "66",
    #             "id": "117",
    #             "openid": "o9ync4nfrkYNFhh6nKTVfk7cNjBE"
    #             }
    #     data1 = json.dumps(data)
    #     with self.client.post("secKill/getProductList.html", headers=head, data=data1, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure('Failed!')
    with open("C:/Users/Administrator/PycharmProjects/eshare/SAAS/UserId.txt") as f:
        userId = f.readlines()
    test1 = randint(0, 162)
    userIds = []
    for i in userId:
        userIds.append(i)
    userId1 = userIds[test1]
    print(userId1)
    head = {
                "Accept": "application/json",
                "Content-Type": "application/json"}
    data = {"address": "广东省广州市海珠区新港中路397号",
                "openid": userId1, #  "o9ync4nfrkYNFhh6nKTVfk7cNjBE",
                "phone": "020-81167888",
                "productId": "117",
                "productNum": 1,
                "receiver": "张三",
                "wid": "66"
                }
    data1 = json.dumps(data)

    @task(2)
    def submitOrder(self):

        head = {
                "Accept": "application/json",
                "Content-Type": "application/json"}
        data = {"address": "广东省广州市海珠区新港中路397号",
                "openid": "o9ync4nfrkYNFhh6nKTVfk7cNjBE",
                "phone": "020-81167888",
                "productId": "117",
                "productNum": 1,
                "receiver": "张三",
                "wid": "66"
                }
        data1 = json.dumps(data)
        with self.client.post("secKill/submitOrder.html", headers=self.head, data=self.data1, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')




class WebsiteUser(HttpLocust):
    host = "https://wxmi.esharex.com/api/vshop/"
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    stop_timeout = 10
    weight = 1