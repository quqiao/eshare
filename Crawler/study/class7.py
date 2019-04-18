# coding=utf-8
'''
Created on 2019年04月08日
@author: quqiao
第七课：selenium库的使用
'''

# 什么是selenium：一套完整的web应用程序测试系统，包含测试的录制（selenium IDE)，编写及运行（selenium Remote Control)和
#                 测试的并行处理（selenium Grid)。Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以
#                 用于任何支持JavaScript的浏览器
#                 selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题

# selenium基本使用：主要用的是selenium的webdriver,我们通过下面的方式先看看Selenium.Webdriver支持哪些浏览器

# PhantomJS:是一个基于WebKit的服务端JavaScript API，支持Web而不需要浏览器支持，其快速，原生支持各种Web标准，Dom处理
#           CSS选择器，JSON等等，PhantomJS可用于页面自动化，网络监测，网页截屏，以及无界面测试

# 声明浏览器对象：selenium支持很多的浏览器，如果想要声明并调用浏览器则需要
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()

# 访问页面
# browser = webdriver.Chrome()
# browser.get("http://www.baidu.com")
# print(browser.page_source)
# browser.close()

# 查找元素
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()

# 多个元素查找
# browser.get("http://www.taobao.com")
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()

# 元素交互操作：对于获取的元素调用交互方法
# import time
# browser.get("http://www.taobao.com")
# input_str = browser.find_element_by_id('q')
# input_str.send_keys("ipad")
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# time.sleep(5)
# browser.close()

# 交互动作：将动作附加到动作链中串行执行
# from selenium.webdriver import ActionChains
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 执行JavaScript
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# 获取元素属性：get_attribute('class')
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id("zh-top-link-logo")
# print(logo)
# print(logo.get_attribute('class'))

# 获取文本值,ID,位置，标签名
# from selenium import webdriver
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)  # 文本值
# print(input.id)  # ID
# print(input.location)  # 位置
# print(input.tag_name)  # 标签名
# print(input.size)  # 大小

# Frame:很多网页都哟Frame标签，爬取数据涉及到切入到frame以及切出来的问题。通常用switch_to.frame()和switcht_to.parent_frame()
import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Chrome()
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# 等待：隐式等待和显示等待
#       隐式等待：到了一定的时间发现元素还没有加载，则继续等待我们指定的时间，如果超过指定的时间会抛出异常，如果没有需要
#                 要等待的时候就已经加载完毕就会立即执行
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)
# browser.close()
#      显示等待：指定一个等待条件，并且指定一个最长等待时间，会在这个时间内进行判断是否满足等待条件，如果成立就会立即返
#                回，不成立就会一直等待。等待到最长等待时间满足就正常返回，还不满足就抛出异常
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# 浏览器的前进和后退：back()和forward()
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

# cookie操作:get_cookies(),delete_all_cookies(),add_cookie()
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# 选项卡管理：通过执行js命令实现新开选项卡window.open(),不同的选项卡是存在列表里browser.window_handles[0]
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')

# 异常处理
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()