# coding=utf-8
'''
Created on 2019年04月23日
@author: quqiao
selenium2学习之获取信息和事件
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

# 获取输入框大小
size = browser.find_element_by_xpath(".//*[@id='kw']").size
print(size)

# 获取信息
text = browser.find_element_by_xpath(".//*[@id='cp']").text
print(text)

# 返回元素属性值，可以是id,name,type或其他属性
attribute = browser.find_element_by_xpath(".//*[@id='cp']").get_attribute("type")
print(attribute)

# 返回元素是否可见
result = browser.find_element_by_xpath(".//*[@id='cp']").is_displayed()
print(result)

# 获取元素上文字
error_msg = browser.find_element_by_xpath("//*[contains(@id,'TANGRAM__PSP_10__error')]").text
print(error_msg)
try:
    assert error_msg == "请您输入手机/邮箱/用户名"
    print(error_msg)
except Exception as e:
    print('msg fail, msg=%s'% error_msg)




# 鼠标事件：鼠标操作的方法封装在ActionChains中
# 常用方法：1)perform():执行所有ActionChains中存储的行为
#           2)context_click():右击
#           3)double_click():双击
#           4)drag_and_drop():拖动
#           5)move_to_element():鼠标悬停
# 双击
# DC = browser.find_element_by_xpath(".//*[@id='u1']/a[8]")
# ActionChains(browser).double_click(DC).perform()


# 键盘事件：

# 输入
browser.find_element_by_id("kw").send_keys("selenium")

# 删除
browser.fin_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键+教程
browser.find_element_by_id("kw").send_keys(Keys.SPACE)
browser.find_element_by_id("kw").send_keys("面试题")

# ctrl+a 全选，ctrl+x 剪切， ctrl+v 粘贴
browser.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
browser.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
browser.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

# 回车  代替单机
browser.find_element_by_id("kw").send_keys(Keys.ENTER)

