# coding=utf-8
'''
Created on 2019年04月22日
@author: quqiao
selenium2学习之浏览器基本操作
'''

# Chrome浏览器
from selenium import webdriver
import time

# 启动浏览器
driver = webdriver.Chrome()

# 浏览器运行
driver.get("https://www.365fengchao.com")

# 设置浏览器窗口大小
driver.set_window_size(400, 800)
time.sleep(2)

# 全屏
driver.maximize_window()
time.sleep(2)

# 后退
driver.back()
time.sleep(2)

# 前进
driver.forward()
time.sleep(2)

# 刷新
driver.refresh()
time.sleep(2)

driver.close()


