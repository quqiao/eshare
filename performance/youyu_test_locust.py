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
                "Accept": "application/json",
                "Content-Type": "application/json"}
    data = {"count":"1",
            "gift_id":"25",
            "room":"1000160964",
            "seq":"203",
            "to_uid":"160964",
            "token":"a11e77188d9fdb8aa386f4b65fa3d879",
            "user_id":"160964"
}
    data1 = json.dumps(data)

    @task(1)
    def CreateOrder(self):

        with self.client.post("gift/sendnew", headers=self.head, data=self.data1,catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')



class WebsiteUser(HttpLocust):
    host = "https://test1.yoyu8.com/index.php/"
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    stop_timeout = 10
    weight = 1
