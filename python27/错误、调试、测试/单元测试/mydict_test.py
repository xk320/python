#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 编写mydict_test.py单元测试
# 为了编写单元测试，我们需要引入python自带的unittest模块
import unittest
from mydict import Dict


class TestDict(unittest.TestCase):
    def setUp(self):
        print 'setUp.....'

    def tearDown(self):
        print 'tearDown....'

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
# 对每一个类测试都需要编写一个test_xxx()方法，由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以
# 断言输出是否是我们所期望的，最常用的断言是assertEquals()：
if __name__ == '__main__':
    unittest.main()

    # setUp和tearDown
    # 可以在单元测试中编写两个特殊的setUP()和tearDown()方法，这两个方法分别在每调用一个测试方法的前后分别被执行。
    # setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()
    # 方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

    # 小结
    # 单元测试可以有效的测试某个程序模块的行为，是未来重构代码的信息保证
    # 单元测试可的测试用例要富态常用的输入组合，边界条件和异常
    # 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身可能有bug
    # 单元测试通过了并不意味着程序就没有bug，但是不通过程序肯定有bug
