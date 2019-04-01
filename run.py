# coding=utf-8
#指定测试用例和测试报告的路径
import logging
import time
import unittest


from BSTestRunner import BSTestRunner

test_dir = './test_case'
report_dir = './reports'

#加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern = 'test*.py')

#定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
report_name = report_dir + '/' + now + 'test_report.html'

#运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="ZLQQT Test Report", description="zlqqt Android app Test Report")
    logging.info('start run testcase...')
    runner.run(discover)