# coding=utf-8
'''
Created on 2019年01月23日
@author: quqiao
菜鸟教程的爬虫基础讲解
'''

# 爬虫：一段自动抓取互联网信息的程序，从互联网上抓取对于我们有价值的信息

# 爬虫架构：1.调度器：相当于一台电脑的CPU,主要负责调度URL管理器，下载器，解析器之间的协调工作
#           2.URL管理器：包括待爬取的URL地址和已爬取的URL地址，防止重复抓取URL和循环抓取URL，实现URL管理器主要用三种
#             方式，通过内存，数据库，缓存数据库来实现
#           3.网页下载器：通过传入一个URL地址来下载网页，将网页转换成一个字符串，网页下载器有urllib2(官方基础模块)包
#             括需要登录，代理和cookie，request（第三方包）
#           4.网页解析器：将一个网页字符串进行解析，可以按照我们的要求来提取出我们有用的信息
#           5.应用程序：就是从网页中提取的有用数据组成的一个应用

# urllib实现下载网页的三种方式
