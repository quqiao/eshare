# coding=utf-8
'''
Created on 2019年04月22日
@author: quqiao
selenium2+Python用于SAAS系统
'''

from selenium import webdriver
import time

# 启动浏览器
browser = webdriver.Chrome()

# 浏览器运行
browser.get("https://www.365fengchao.com/")

# 全屏
browser.maximize_window()
time.sleep(2)

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

# 关闭页面
time.sleep(5)
browser.close()

