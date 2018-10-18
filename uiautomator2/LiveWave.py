# coding: utf-8

import uiautomator2 as u2
import unittest
import time

class LiveWaveTestCase(unittest.TestCase):

    global d
    d = u2.connect("2bb4c0bd")
    # def setUp(self):
    #     d.app_start("com.guodong.guodong")  # 启动app
    #
    # def tearDown(self):
    #     d.app_stop("com.guodong.guodong")  # 关闭app

    def test_01(self):
        '''打开手机'''
        d.screen_on()   # 打开屏幕
        time.sleep(1)
        d.drag(0.5, 0.8, 0.5, 0.1)  # 滑动解锁
        time.sleep(2)
        for i in range(4):
            d(resourceId="com.android.systemui:id/key7").click()

    def test_02(self):
        '''登录'''
        d.app_start("com.guodong.guodong")  # 启动app
        # time.sleep(2)
        # d(text="开始体验").click()
        time.sleep(2)  # 删除文本框内容
        d.set_fastinput_ime(True)   # 切换输入法，使用专用输入法
        d.clear_text()
        d(text="请输入手机号").set_text("18008062016")
        time.sleep(2)
        d.click(0.339, 0.337)  # 下一行
        time.sleep(1)
        d.clear_text()
        d(text="请输入密码").set_text("123456")
        time.sleep(2)
        d(text="登录").click()
        d.set_fastinput_ime(False)  # 切换输入法，关闭专用输入法
        time.sleep(2)
        d.watcher("允许").when(text="允许").click(text="允许")  # 点击可能的系统弹框
        self.assertFalse(d(text="Status Bar").wait(timeout=3))  # 检查不存在

    def test_03(self):
        '''首页'''
        d = u2.connect("2bb4c0bd")    # 连接手机
        time.sleep(1)
        d.click(0.081, 0.29)  # 点击我的家族
        self.assertTrue(d(text="家族贡献榜").wait(timeout=2))  # 检查存在
        time.sleep(1)
        d.click(0.066, 0.065)  #返回首页
        time.sleep(1)
        d.click(0.562, 0.287)
        time.sleep(1)
        d.click(0.113, 0.056)

    # def test_02(self):
    #     '''退出登录'''
    #     time.sleep(3)
    #     d.click(0.791, 0.892)  # 点击个人
    #     time.sleep(3)
    #     d.drag(0.48, 0.82, 0.48, 0.32)  # 向下滑动
    #     time.sleep(2)
    #     d(text="设置").click()
    #     time.sleep(2)
    #     d(text="退出登录").click()
    #     time.sleep(2)

if __name__ == '__main__':
    unittest.main()