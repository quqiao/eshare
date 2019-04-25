# coding=utf-8
'''
Created on 2019年04月23日
@author: quqiao
selenium2学习之unittest
'''

# TestCase和TestSuite
# 单元测试的本身就是用代码去验证另一段代码，而单元测试框架主要的功能：
# 1)提供用例组织与执行
# 2)提供丰富的比较方法
# 3)提供丰富的日志
import unittest
# TestCase类看成是对特定类进行测试的集合
class TestCount(unittest.TestCase):
    # setUp用于测试用例执行前的初始化工作 tearDown与其对应是善后工作
    def setUp(self):
        print("start")

    def test_add01(self):
        j= count(2, 3)
        # 对add()的返回值进行断言，判断是否相等
        self.assertEqual(j.add(), 5)

    def test_add02(self):
        j = count(3,4)

    def tearDown(self):
        print("end")

# main()方法使用TestLoade类来搜索所有包含在该模块以“test”命名开头的测试方法并自动执行
if __name__ == "__main__":
    # 第一种方式
    unittest.main()
    # __name__作为模块的内置属性，就是.py文件的调用方式
    # __main__表示直接使用

    # 第二种方式
    # 构造测试套件
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add01"))
    suite.addTest(TestCount("test_add02"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # 第三种方式
    test_dir = './'
    # test_dir 测试路径 pattern='test*.py'匹配规则test开头.py文件 *表示任意多字符
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)


# 首先引入unittest模块，创建TestCount类继承uinitest的TestCase类
# setUp用于测试用例执行前的初始化工作 tearDown与其对应是善后工作
# 在test_add中先调用count类出啊如要计算的值，然后用assertEqual方法来断言，判断两者的值是否相等



# 断言


# 装饰器skip用法
# @unittest.skip('跳过')
# @unittest.skipIf(3>2,'当条件为TRUE跳过')
# @unittest.skipUnless(3>2,'当条件为TRUE时执行测试')

