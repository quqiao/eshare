# coding=utf-8
'''
Created on 2019年04月24日
@author: quqiao
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver， url, FindElement等
    """
    # 初始化driver, url, pagetitle等
    # 实例化BasePage类时,最先执行的就是__init__方法，该方法的入参，其实是BasePage类的如蚕
    # __init__方法不能有返回值，只能返回None
    # self只实例本身，相较于类Page而言
    def __init__(self, selenium_driver, base_url, pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle

    # 通过title断言进入的页面是否正确
    # 使用title获取当前窗口title,检查输入的title是否在当前title中，返回结果
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 打开页面，并检验页面连接是否加载正确
    # 以单下划线_开头或__双划线的方法，使用import *时，保证该方法为类私有的
    def _open(self, url, pagetitle):
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致，调用on_page()方法
        assert self.on_page(pagetitle),u'打开页面失败%s'(url)

    # 定义open方法，调用_open方法打开链接
    def open(self):
        self._open(self.base_url, self.pagetitle)
        # basepage是类，open是这个类李的方法，想要调用方法，需先创建类的实例，这个过程就是实例化
        # 在定义方法的时候，一定要传递一个实例方法的参数self,这个self相当于实例本身
        # 因为方法是实例的方法，所以如果不把实例当做参数传递过来的话，是没办法调用这个方法的

    # 重写元素定位
    def find_element(self, *loc):
        try:
            # 确保元素是可见的
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里
            # WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u'%s页面未能找到%s元素'(self.loc))

    # 重写switch_frame
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script方法，用于执行js
    def script(self, src):
        self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, value, clear_first=True, click_first= True):
        try:
            loc = getattr(self, '_%s'% loc) # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(u'%s页面未能知道%元素'(self, loc))




