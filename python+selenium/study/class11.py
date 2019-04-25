# coding=utf-8
'''
Created on 2019年04月24日
@author: quqiao
selenium2学习之POM设计模式
'''

# 模式简介：Page Object模式是Selenium中的一种测试设计模式
#           Page Object模式是一种自动化测试设计模式，将页面定位和业务操作分开，分离测试对象（元素对象）和测试脚本（用例
#           脚本）,提高用例的可维护性
#           Unittest是一种单元测试框架，用于设计各式各样的测试用例，可调用PageObject设计的页面类（对象）
# POM优点：1)把web ui对象仓库从测试脚本分离，业务代码和测试脚本分离
#          2)每一个页面对应一个页面类，页面的元素写到这个页面类中
#          3)页面类主要包括该页面的元素定位，和这些元素相关的业务操作代码封装的方法
#          4)代码复用，从而减少测试脚本代码量
#          5)层次清晰，同时支持多个编写自动化脚本开发
#          6)建议页面类和业务逻辑方法都给一个有意义的名称，方便他人快速编写脚本和维护脚本



# project: 基础类BasePage，封装所有页面都公用的方法，定义open函数，重定义find_element,switch_frame,send_keys等函数
#          初始化方法中定义驱动driver,基本url,title
#          WebDriverWait提供了显示等待方式
# 代码参考POM_demo



