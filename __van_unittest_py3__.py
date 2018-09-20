import unittest, sys

sys.path.append(r"C:\Users\VAN\Desktop\test")
sys.path.append(".")
import HTMLTestRunner_PY3
import __createtestreporter__
import io


class Mytest(unittest.TestCase):
    def setUp(self):
        print("这是van的测试报告")

    def tearDown(self):
        print("执行完毕")

    def test_1(self):
        '''你是一只gui'''
        self.assertEqual(1, 1)


if __name__ == '__main__':
    # unittest.main()
    # test.main()
    test_suite = unittest.TestSuite()
    test_suite.addTest(Mytest('test_1'))
    __createtestreporter__.createreporter(object=test_suite)
