# coding=utf-8
import unittest

from MarketMainPageView import MartetMainPage
from buttonTabView import buttonTabView
from myunit import StartEnd
from zlqqt_common import Common
from zlqqt_desired_caps import logging


class TestCase(StartEnd):
    def test_hang_heng_index_skip(self):
        hang_seng_index_expect_name = '恒生指数'
        logging.info('点击恒生指数')
        com = Common(self.driver)
        com.start_page()

        t = buttonTabView(self.driver)
        t.click_main_market()

        mmv = MartetMainPage(self.driver)
        mmv.click_heng_seng_index()
        hang_seng_index_fact_name = mmv.get_heng_seng_index_page_center_title()
        self.assertEqual(hang_seng_index_fact_name, hang_seng_index_expect_name)


if __name__ == '__main__':
    unittest.main()
