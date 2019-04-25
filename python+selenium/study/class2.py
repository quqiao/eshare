# coding=utf-8
'''
Created on 2019年04月22日
@author: quqiao
selenium2学习之定位
'''

# 通过元素定位

# 通过name定位：find_element_by_name()
# name可能重复

# 通过class定位：find_element_by_class_name()

# 通过tag定位：find_element_by_tag_name()
# 标签名字最容易重复

# 通过link精确定位：find_element_by_link_text()
# 对一个超链接来说这种定位方法很方便

# 通过link模糊定位：find_element_by_partial_link_text()
# 一个连接文本很长，可以用这种方法，只要输入的这部分信息是这个连接的唯一标识即可



# 通过css定位:CSS(Cascading Style Sheets)是一种语言，用来描述HTML和XML文档的表现，CSS可以较为灵活的选择控件的任意属性，
#             一般情况下会比 XPath快，且语法也比较简洁

# 通过id属性定位：find_element_by_css_selector("#text")
# #表示通过id属性定位

# 通过class属性定位：find_element_by_css_selector(".text")
# .表示通过class属性定位

# 通过标签名定位：find_element_by_css_selector("input")
# 不需要任何符号标识

# 父子关系定位：find_element_by_css_selector("span>input")
# 表示有父元素，标签名span,查找它所有标签名为input的子元素

# 通过属性定位：find_element_by_css_selector("[name='kw']")
# 注意单引号和双引号区分

# 组合定位：find_element_by_css_selector("form.fm>span>input.s_ipt")
# 定位一个标签名为input,class属性为s_ipt,它有个父元素为span,它父元素的父元素标签名为form，class为fm的元素

# 通过by定位元素：find_element(By.ID,'kw')
# 定位类型：By.ID,By.NAME,By.CLASS_NAME,By.TAG_NAME,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.XPATH,By.CSS_SELECTOR


# xpath定位

# id属性：find_element_by_xpath("//input[@id='kw']")

# class属性：find_element_by_xpath("//input[@class='s_ipt']")

# name属性：find_element_by_xpath("//input[@name='wd']")

# maxlength属性：find_element_by_xpath("//input[@maxlenth='255']")

# 组合定位：find_element_by_xpath("//input[@class='s_ipt' and @name='wd']")
# 查找的是input标签下id属性为kw且name属性为wd的元素

# find_element_by_xpath("//*[contain(text(),'xxx')]")
# 查找包含xxx关键字的所有元素


