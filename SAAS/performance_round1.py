#   coding:utf-8

from locust import HttpLocust, TaskSet, task
import json
from random import randint



# 定义用户行为
class UserBehavior(TaskSet):
    # with open("C:/Users/Administrator/PycharmProjects/eshare/performance1/UserId.txt") as f:
    #     userId = f.readlines()
    # test1 = randint(0, 162)
    # userIds = []
    # for i in userId:
    #     userIds.append(i)
    # userId1 = userIds[test1]
    # print(userId1)
    head = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "token": "8c9eb83c88e427edffcf06c3b7b0417a"}
    data = {"goodsinfo":"{\"count\":1,\"discount\":\"10\",\"freight\":0,\"goods_amount\":0.1,\"pay_amount\":0.1,\"mobile\":\"18023565522\",\"consignee\":\"test\",\"address\":\"北京北京市东城区1111\",\"goods\":[{\"goods_id\":\"1000772\",\"item_id\":\"\",\"goods_name\":\"VANS\",\"goods_images\":\"http://wxmiimage.esharex.com/m_115/shop/15504706798742.jpeg\",\"spec_name\":\"\",\"goods_price\":\"0.10\",\"goods_num\":1}],\"remark\":\"\",\"actual_money\":0,\"actual_integral\":\"\",\"get_integral\":\"\",\"coupon_list_id\":0}",
            "action": "orderpay", "type": "immebuy"
            }
    data1 = json.dumps(data)

    # @task(1)
    # def popup(self):
    #     with self.client.get("/fxhb/popup", headers=self.head, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure('Failed!')

    @task(2)
    def detail(self):
        with self.client.get("/weapp/goods/detail?goods_id=1000772", headers=self.head, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')
    #
    # @task(3)
    # def addorder(self):
    #     with self.client.post("/weapporder/addorder", headers=self.head, data=self.data1, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure('Failed!')
    #
    # @task(4)
    # def order_detail(self):
    #     with self.client.get("/weapporder/detail?order_id=242", headers=self.head, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure('Failed!')

    # @task(2)
    # def detail(self):
    #     with self.client.get("/user/test", catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure('Failed!')

class WebsiteUser(HttpLocust):
    host = "https://api.365fengchao.com/app"
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    stop_timeout = 10
    weight = 1