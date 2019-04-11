# coding:utf-8
__author__ = "michael"

import unittest

from src.pages.market_main_page_view import MartetMainPage
from src.pages.button_tab_view import ButtonTabView
from src.common.myunit import StartEnd
from src.common.zlqqt_desired_caps import logging


class TestCase(StartEnd):
    def test_click_bottom_tab(self):
        """
        测试点击底部四个tab功能
        :return:
        """
        logging.info('点击底部tab测试用例开始执行')

        t = ButtonTabView(self.driver)
        t.click_main_trade()
        t.click_main_market()
        t.click_main_indexpage()
        t.click_main_account()

    def test_hang_heng_index_skip(self):
        """
        测试行情首页点击恒生指数功能
        :return:
        """
        hang_seng_index_expect_name = '恒生指数'
        logging.info('点击恒生指数')

        t = ButtonTabView(self.driver)
        t.click_main_market()

        mmv = MartetMainPage(self.driver)
        mmv.click_heng_seng_index()
        hang_seng_index_fact_name = mmv.get_heng_seng_index_page_center_title()
        self.assertEqual(hang_seng_index_fact_name, hang_seng_index_expect_name)


if __name__ == '__main__':
    unittest.main()
