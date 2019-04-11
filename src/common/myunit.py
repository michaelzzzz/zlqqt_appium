# coding:utf-8
__author__ = "michael"

import unittest

from src.common.zlqqt_common import Common
from src.common.zlqqt_desired_caps import logging, zlqqt_desired


class StartEnd(unittest.TestCase):
    """
    testcase单个执行，每执行一个testcase还原app系统设置，即重新启动
    """
    # def setUp(self):
    #     logging.info('==================setUp=====================')
    #     self.driver = zlqqt_desired()
    #     logging.info('启动app过渡页面')
    #     com = Common(self.driver)
    #     com.start_page()
    #
    # def tearDown(self):
    #     logging.info('==================tearDown==================')
    #     sleep(5)
    #     self.driver.close_app()
    #     self.driver.quit()
    """
    执行完一个py里面的testcase 还原app系统设置，即重新启动
    """
    @classmethod
    def setUpClass(cls):
        """
        app初始化
        """
        driver = zlqqt_desired()
        cls.driver = driver
        logging.info('启动app过渡页面')
        com = Common(driver)
        com.start_page()


    @classmethod
    def tearDownClass(cls):
        """
        测试结束
        """
        cls.driver.quit()