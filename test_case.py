# coding=utf-8
import unittest

from buttonTabView import buttonTabView
from myunit import StartEnd
from zlqqt_common import Common
from zlqqt_desired_caps import logging


class TestCase(StartEnd):
    def test_click_bottom_tab_trade(self):
        logging.info('点击底部tab交易按钮...')
        t = buttonTabView(self.driver)
        t.common_openation()
        t.click_main_trade()

if __name__ == '__main__':
    unittest.main