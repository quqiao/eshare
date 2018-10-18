# coding: utf-8

import uiautomator2 as u2
import unittest
import time
import uiautomator2.ext.htmlreport as htmlreport
import HTMLTestReportCN

class youyuLiveTestCase(unittest.TestCase):

    global d   # 全局变量
    d = u2.connect("4176a878")    # 连接手机
    global hrp
    hrp = htmlreport.HTMLReport(d)
    hrp.patch_click()
    # def setUp(self):
    #     d.app_start("com.youyu.youyulive")  # 启动app
    #
    # def tearDown(self):
    #     d.app_stop("com.youyu.youyulive")  # 关闭app


    def test_01(self):
        '''登录'''
        # time.sleep(2)
        # d(text="开始体验").click()
        d.app_start("com.youyu.youyulive")  # 启动app
        time.sleep(2)
        d.set_fastinput_ime(True)   # 切换输入法，使用专用输入法
        d.clear_text()
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/login_phone").set_text("18008062016")
        time.sleep(2)
        d(resourceId="com.youyu.youyulive:id/login_password").set_text("123456")
        time.sleep(2)
        d(text="登录").click()
        d.set_fastinput_ime(False)  # 切换输入法，关闭专用输入法
        d.watcher("允许").when(text="允许").click(text="允许")  # 点击可能的系统弹框
        d.watcher("领取").when(text="领取").click(text="领取")  # 点击可能的系统弹框
        self.assertTrue(d(text="关注123").wait(timeout=3))  # 检查不存在

    def test_02(self):
        '''首页中页面检查'''
        time.sleep(2)
        d(text="热门").click()
        time.sleep(1)
        d(text="关注").click()
        time.sleep(1)
        d(text="最新").click()
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/main_index_imgbtn_chat").click()  # 信息按钮
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/jmui_return_btn_m").click()  # 返回
        self.assertTrue(d(resourceId="com.youyu.youyulive:id/jmui_return_btn_m").wait(timeout=3))  # 判断返回按钮已经不在

    def test_03(self):
        '''看直播'''
        time.sleep(2)
        d(text="热门").click()
        time.sleep(1)
        d(className="android.widget.LinearLayout", instance=10).click()  # 点击第一个直播
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/room_imgbtn_public_chat").click()  # 点击消息
        time.sleep(1)
        d.click(0.5, 0.3)  # 关闭消息
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/room_imgbtn_prvchat").click()  # 点击信息
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/chat_sysback").click()  # 返回
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/room_imgbtn_setting").click()  # 点击设置
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/setting_cancel").click()  # 点击取消
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/room_imgbtn_share").click()  # 点击分享
        time.sleep(1)
        d.click(0.5, 0.3)  # 关闭消息
        time.sleep(300)
        d(resourceId="com.youyu.youyulive:id/room_imgbtn_close").click()  # 点击关闭
        time.sleep(1)
        self.assertTrue(d(resourceId="com.youyu.youyulive:id/index_hot_btn").wait(timeout=3))  # 检查返回热门界面


    def test_04(self):
        '''直播'''
        d(resourceId="com.youyu.youyulive:id/main_paly").click()  # 直播
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/room_create_btn_start_live").click()  # 普通直播
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/previewBtn").click()  # 开始直播
        time.sleep(2)
        d(resourceId="com.youyu.youyulive:id/dialog_message_commit").click()  # 确定开始直播
        time.sleep(5)
        d(resourceId="com.youyu.youyulive:id/room_imgbtn_close").click()  # 关闭直播
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/dialog_message_commit").click()  # 确定关闭
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/dialog_room_finish_btn_finish").click()  # 返回首页
        time.sleep(1)
        self.assertTrue(d(resourceId="com.youyu.youyulive:id/index_hot_btn").wait(timeout=3))  # 检查返回热门界面

    def test_05(self):
        '''个人中头像检查'''
        d(resourceId="com.youyu.youyulive:id/main_rl_me").click()  # 点击个人
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/my_me_photo").click()  # 点击头像
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/edit_avatar_imgbtn_back").click()  # 点击返回
        time.sleep(1)
        self.assertTrue(d(resourceId="com.youyu.youyulive:id/my_me_photo").wait(timeout=3))  # 判断头像出现

    def test_06(self):
        '''个人中直播检查'''
        d(resourceId="com.youyu.youyulive:id/item_playback").click()  # 点击直播
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/imgbtn_toolbar_back").click()  # 点击返回
        time.sleep(1)
        self.assertTrue(d(resourceId="com.youyu.youyulive:id/my_me_photo").wait(timeout=3))  # 判断头像出现

    def test_07(self):
        '''个人中等级检查'''
        d(resourceId="com.youyu.youyulive:id/item_level").click()  # 点击等级
        time.sleep(1)
        d(text=u"主播").click()
        time.sleep(1)
        d(text=u"土豪").click()
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/imgbtn_toolbar_back").click()  # 返回
        time.sleep(1)
        self.assertTrue(d(resourceId="com.youyu.youyulive:id/my_me_photo").wait(timeout=3))  # 判断头像出现

    def test_08(self):
        '''个人中账户检查'''
        d(resourceId="com.youyu.youyulive:id/item_money").click()  # 账户
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/imgbtn_toolbar_back").click()  # 返回
        time.sleep(1)
        self.assertTrue(d(resourceId="com.youyu.youyulive:id/my_me_photo").wait(timeout=3))  # 判断头像出现

    def test_09(self):
        '''个人中师徒收益'''
        d(resourceId="com.youyu.youyulive:id/fragment_me_item_master_bonus").click()  # 师徒收益
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/bonus_taking").click()  # 提取收益
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/imgbtn_toolbar_back").click()  # 返回
        time.sleep(1)
        self.assertTrue(d(text="师徒收益").wait(timeout=3))  # 检查返回设置

    def test_10(self):
        '''个人中邮箱'''
        d(resourceId="com.youyu.youyulive:id/fragment_me_item_email").click()  # 邮箱
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/email_send_box_btn").click()  # 发件箱
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/send_email_btn").click()  # 发邮件
        time.sleep(1)
        time.sleep(2)
        d.set_fastinput_ime(True)   # 切换输入法，使用专用输入法
        d(resourceId="com.youyu.youyulive:id/user_id").set_text("123456")  # 输入用户
        time.sleep(2)
        d(resourceId="com.youyu.youyulive:id/send_email_title").set_text("输入标题")  # 输入标题
        time.sleep(2)
        d(resourceId="com.youyu.youyulive:id/send_email_content").set_text("输入内容")  # 输入内容
        time.sleep(2)
        d(resourceId="com.youyu.youyulive:id/send_email_btn").click()
        d.set_fastinput_ime(False)  # 切换输入法，关闭专用输入法
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/imgbtn_toolbar_back").click()  # 返回
        time.sleep(1)
        d(resourceId="com.youyu.youyulive:id/imgbtn_toolbar_back").click()  # 返回


    def test_11(self):
        '''退出登录'''
        time.sleep(3)
        d.drag(0.48, 0.82, 0.48, 0.32)  # 向下滑动
        time.sleep(2)
        d(text="设置").click()
        time.sleep(2)
        d(text="退出登录").click()
        time.sleep(2)
        self.assertFalse(d(text="退出登录").wait(timeout=3))  # 检查退出登录按钮已不在


    #添加Suite
def Suite():
    #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    #将测试用例加入到容器
    suiteTest.addTest(youyuLiveTestCase("test_01"))
    suiteTest.addTest(youyuLiveTestCase("test_02"))
    suiteTest.addTest(youyuLiveTestCase("test_03"))
    suiteTest.addTest(youyuLiveTestCase("test_04"))
    suiteTest.addTest(youyuLiveTestCase("test_05"))
    suiteTest.addTest(youyuLiveTestCase("test_06"))
    suiteTest.addTest(youyuLiveTestCase("test_07"))
    suiteTest.addTest(youyuLiveTestCase("test_08"))
    suiteTest.addTest(youyuLiveTestCase("test_09"))
    suiteTest.addTest(youyuLiveTestCase("test_10"))
    suiteTest.addTest(youyuLiveTestCase("test_11"))
    return suiteTest

if __name__ == '__main__':
    # unittest.main()
        #确定生成报告的路径
    filePath ='D:\\report\HTMLTestReportCN.html'
    fp = open(filePath, 'wb')
    #生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        #description='详细测试用例结果',
        tester='quqiao'
        )
    #运行测试用例
    runner.run(Suite())
    fp.close()