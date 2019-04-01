# coding=utf-8
import unittest

from MarketMainPageView import MartetMainPage
from buttonTabView import buttonTabView
from myunit import StartEnd
from zlqqt_common import Common
from zlqqt_desired_caps import logging


class TestCase(StartEnd):
    def test_click_bottom_tab(self):
        logging.info('点击底部tab测试用例开始执行')
        com = Common(self.driver)
        com.start_page()

        t = buttonTabView(self.driver)
        t.click_main_trade()
        t.click_main_market()
        t.click_main_indexpage()
        t.click_main_account()


if __name__ == '__main__':
    unittest.main()
