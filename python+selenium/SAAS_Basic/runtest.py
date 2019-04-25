# coding=utf-8
'''
Created on 2019年04月23日
@author: quqiao
执行文件
'''

import unittest

# test_dir = 'C:/Users/Administrator/PycharmProjects/eshare/python+selenium/SAAS_Basic/test_case'
test_dir ='./test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)
