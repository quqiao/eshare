#coding=utf-8
'''
Created on 2018年12月14日
@author: quqiao
'''

import uiautomator2 as u2
import unittest
from time import sleep
import uiautomator2.ext.htmlreport as htmlreport
import HTMLTestReportCN


class RedHatCheckPoint(unittest.TestCase):
    global d   # 全局变量
    d = u2.connect("2bb4c0bd")    # 连接手机
    global hrp
    hrp = htmlreport.HTMLReport(d)
    hrp.patch_click()

    def test_01(self):
        '''登录'''
        # time.sleep(2)
        # d(text="开始体验").click()
        d.app_start("com.youyu.youyulive")  # 启动app
        sleep(2)
        d.set_fastinput_ime(True)   # 切换输入法，使用专用输入法
        sleep(2)
        d.watcher("确定").when(text="确定").click(text="确定")  # 监控是否有权限获取弹出框
        sleep(2)
        for i in range(5):
            d.watcher("允许").when(text="允许").click(text="允许")  # 允许获取权限
        d.clear_text()
        sleep(5)
        d.watcher("知道了").when(text="知道了").click(text="知道了")  # 检测关闭更新提示
        sleep(2)
        d(resourceId="com.youyu.youyulive:id/loginMainPhone").click()  # 点击登录按钮
        sleep(2)
        d(resourceId="com.youyu.youyulive:id/mainAccountEdit").set_text("18008062016")
        sleep(2)
        d(resourceId="com.youyu.youyulive:id/mainPwdEdit").set_text("123456")
        sleep(2)
        d(text="登录").click()
        d.set_fastinput_ime(False)  # 切换输入法，关闭专用输入法
        d.watcher("允许").when(text="允许").click(text="允许")  # 点击可能的系统弹框
        d.watcher("领取").when(text="领取").click(text="领取")  # 点击可能的系统弹框
        self.assertTrue(d(resourceId="com.youyu.youyulive:id/btmMenuMainImg").wait(timeout=3))  # 检查不存在

    def test_02(self):
        "查看直播"
        d(text=u"热门").click()  # 点击热门
        sleep(2)
        d(className="android.widget.ImageView", instance=4).click()  # 选择任意已有直播
        sleep(2)
        d.click(0.113, 0.915)  # 点击对话框
        sleep(1)
        d.click(0.453, 0.678)  # 输入一个字符
        sleep(1)
        d.click(0.481, 0.899)  # 输入
        sleep(1)
        d(text=u"发送").click()  # 点击热门
        sleep(1)
        d.click(0.793, 0.405)  # 退出对话框
        sleep(1)
        d.click(0.932, 0.91)  # 点击送礼物
        sleep(1)
        d.click(0.878, 0.92)  # 点击赠送
        sleep(1)
        d.click(0.957, 0.062)  # 关闭礼物栏
        sleep(1)
        d.click(0.957, 0.062)  # 弹出退出框
        sleep(1)
        d.click(0.691, 0.451)  # 退出直播
        self.assertFalse(d(resourceId="com.youyu.youyulive:id/btmMenuMainImg").wait(timeout=3))  # 检查是否正确

    def test_03(self):
        "发起直播"
        d(resourceId="com.youyu.youyulive:id/btmMenuLiveImg").click()  # 点击发起直播
        sleep(2)
        d(text=u"开启直播").click()  # 点击开启直播
        sleep(2)
        d.watcher("确定").when(text="确定").click(text="确定")  # 点击可能的系统弹框
        sleep(1)
        d.watcher("允许").when(text="允许").click(text="允许")  # 点击可能的系统弹框
        sleep(2)
        d(text=u"开启直播").click()  # 点击开启直播
        sleep(2)
        d(text=u"开启直播").click()  # 点击开启直播
        sleep(30)
        d.press("back")  # 返回键退出
        sleep(2)
        d(text=u"确定").click()  # 确定退出
        self.assertFalse(d(resourceId="com.youyu.youyulive:id/btmMenuMainImg").wait(timeout=3))  # 检查是否正确






# 添加Suite
def Suite():
    # 定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    # 将测试用例加入到容器
    suiteTest.addTest(RedHatCheckPoint("test_01"))
    suiteTest.addTest(RedHatCheckPoint("test_02"))
    suiteTest.addTest(RedHatCheckPoint("test_03"))
    # suiteTest.addTest(RedHatCheckPoint("test_04"))
    # suiteTest.addTest(RedHatCheckPoint("test_05"))
    # suiteTest.addTest(RedHatCheckPoint("test_06"))
    # suiteTest.addTest(RedHatCheckPoint("test_07"))
    # suiteTest.addTest(RedHatCheckPoint("test_08"))
    # suiteTest.addTest(RedHatCheckPoint("test_09"))
    # suiteTest.addTest(RedHatCheckPoint("test_10"))
    # suiteTest.addTest(RedHatCheckPoint("test_11"))
    return suiteTest

if __name__ == '__main__':
    # unittest.main()
        # 确定生成报告的路径
    filePath ='D:\\report\HTMLTestReportCN.html'
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        # description='详细测试用例结果',
        tester='quqiao'
        )
    # 运行测试用例
    runner.run(Suite())
    fp.close()