# coding=utf-8
'''
Created on 2019年04月23日
@author: quqiao
测试用例
'''

from selenium import webdriver
import time
import unittest

class SaasTest(unittest.TestCase):
    def setUp(self):
        # 启动浏览器
        self.browser = webdriver.Chrome()
        # 浏览器运行
        self.browser.get("https://www.365fengchao.com/")
        # 全屏
        self.browser.maximize_window()
        time.sleep(2)

    # 添加一个小程序
    def test_01(self):
        browser = self.browser
        # 点击登录按钮
        browser.find_element_by_xpath("//*[text()='登录']").click()
        # 输入账号和密码
        browser.find_element_by_name("username").send_keys("quqiao")
        browser.find_element_by_name("password").send_keys("123456")
        time.sleep(2)
        # 点击登录按钮
        browser.find_element_by_xpath("//*[text()='登录']").click()
        # 点击小程序
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/div/ul/div[1]/li/div').click()
        # 点击小程序管理
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div/div[1]/div/ul/div[1]/li/ul/a[2]').click()
        # 添加小程序
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="stepIndex0"]/span').click()
        # 输入小程序名称
        time.sleep(3)
        browser.find_element_by_xpath('//*[@id="add-app-1"]/div/div/div/div/div/div/input').send_keys("test0422")
        # 立即添加小程序
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/section/div[1]/div/div/div/form/div/div[3]/div/div/div/button').click()
        time.sleep(2)

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()