"""
======================
@author:小谢学测试
@time:2021/9/7:14:48
@email:xie7791@qq.com
======================
"""
import unittest
class test_demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("类的开始")

    def test_02(self):
        print("test_01")
        self.assertEqual(3, 3, "判断相等")
        self.assertIn('h', 'this')
    @classmethod
    def tearDownClass(cls) -> None:
        print("类的结束")


    def setUp(self) -> None:
        print("用例开始执行")
    def tearDown(self) -> None:
        print("用例结束执行")
    def test_01(self):
        print("test_01")
        self.assertEqual(2,2,"判断相等")
        self.assertIn('h','this')
    @unittest.skipIf(1+1==2,"跳过这条用例")  #跳过这条用例，不执行
    def test_03(self):
        print("test_01")
        self.assertEqual(2,2,"判断相等")
        self.assertIn('h','this')
class test_demo_01(unittest.TestCase):
    def test_demo_01(self):
        print("test_demo_01")

    def test_demo_02(self):
        print("test_demo_02")
if __name__ == '__main__':
    # unittest.main()

    #选择单个测试用例进测试套件
    # suite= unittest.TestSuite()
    # suite.addTest(test_demo("test_01"))
    # suite.addTest(test_demo_01("test_demo_01"))
    # unittest.TextTestRunner().run(suite)

    #把测试类加载进测试套件里面
    # suite = unittest.TestLoader().loadTestsFromTestCase(test_demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(test_demo_01)
    # testsuite = unittest.TestSuite([suite,suite1])
    # unittest.TextTestRunner().run(testsuite)

    #匹配某个目录下所有以test_开头的用例
    discover = unittest.defaultTestLoader.discover("./",'test*.py')
    unittest.TextTestRunner().run(discover)


