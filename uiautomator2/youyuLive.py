# coding: utf-8

import uiautomator2 as u2
import unittest
import time

class youyuLiveTestCase(unittest.TestCase):
    @classmethod     # 类方法
    def setUpClass(cls):
        cls.d = u2.connect("2bb4c0bd")     # 连接手机
        cls.d.set_orientation('natural')

    def setUp(self):
        self.sess = self.d.session("com.youyu.youyulive")
        self.sess.watchers.remove()

    def tearDown(self):
        self.sess.watchers.remove()

    def test_login(self):
        d = self.sess
        # time.sleep(2)
        # d(text="开始体验").click()
        time.sleep(2)
        d.set_fastinput_ime(True)   # 切换输入法，使用专用输入法
        d(text="请输入手机号或您的ID号").set_text("18008062016")
        time.sleep(2)
        d(text="请输入账户密码").set_text("123456")
        time.sleep(2)
        d(text="登录").click()
        d.set_fastinput_ime(False)  # 切换输入法，关闭专用输入法
        time.sleep(3)
        d.click(0.791, 0.892)  # 点击个人
        time.sleep(3)
        d.drag(0.48, 0.82, 0.48, 0.32)  # 向下滑动
        time.sleep(2)
        d(text="设置").click()
        time.sleep(2)
        d(text="退出登录").click()
        time.sleep(2)

    # def test_tip(self):
    #
    #     for i in range(5):
    #         time.sleep(1)
    #         d(text="允许").click()   # 选择系统允许设置
    #     d(text="领取").click()

    # def test_exit(self):
    #     d = self.sess
    #     time.sleep(2)
    #     d.xpath("//android.widget.RelativeLayout").click()  # 点击个人
    #     time.sleep(2)
    #     d.drag(0.48, 0.82, 0.48, 0.52)  # 向下滑动
    #     time.sleep(2)
    #     d(text="设置").click()
    #     time.sleep(2)
    #     d(text="退出").click()
    #     time.sleep(2)


if __name__ == '__main__':
    unittest.main()