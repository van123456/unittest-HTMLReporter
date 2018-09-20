#!/usr/bin/env python
# -*-coding:utf-8-*-
# createtestreporter.py
import sys

sys.path.append(".")
import HTMLTestRunner_PY3


def createreporter(object):
    # 打开一个文件--open一个对象，wb就是byte-write，没有会创建
    fp = open(r"C:\Users\xiewenhua\Desktop\test.html", 'wb')
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title='Mobile TEST Reporter[移动测试报告]',
                                               description='description:专业移动测试30年、专业的移动测试')
    runner.run(object)


if __name__ == '__main__':
    createreporter()
