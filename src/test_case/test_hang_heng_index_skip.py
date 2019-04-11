# coding=utf-8
__author__ = "michael"
import unittest

from src.pages.market_main_page_view import MartetMainPage
from src.pages.button_tab_view import ButtonTabView
from src.common.myunit import StartEnd
from src.common.zlqqt_desired_caps import logging


class TestCase(StartEnd):
    def test_hang_heng_index_skip(self):
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
