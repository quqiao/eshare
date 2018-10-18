from locust import HttpLocust, TaskSet, task
import json
from random import randint


# 定义用户行为
class UserBehavior(TaskSet):
    # def on_start(self):
    #     self.UserLoginAsync()
    # @task(2)
    # def logOut(self):
    #     self.interrupt()
    @task
    def UserLoginAsync(self):
        users = {"user1": 123456, "user2": 111222, "user3": 333444}
        data = randint(1, 3)
        username = "user" + str(data)
        password = users[username]
        head = {
                "Accept": "application/json",
                "Content-Type": "application/json"}
        data = {
                "phone": username,
                "password": password}
        data1 = json.dumps(data)
        with self.client.post("Password/UserLoginAsync", headers=head, data=data1,catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')


class WebsiteUser(HttpLocust):
    host = "http://userpassport.api.guodong.com/"
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    # stop_timeout = 10
    # weight = 1