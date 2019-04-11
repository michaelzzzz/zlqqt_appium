# coding:utf-8
__author__ = "michael"

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.common.zlqqt_common import Common
from src.common.zlqqt_desired_caps import logging


class MartetMainPage(Common):
    """
    市场行情首页
    """
    #恒生指数
    hang_seng_index = (By.XPATH, '//android.widget.TextView[@text ="恒生指数"]')
    #恒生指数页面
    hang_seng_index_page = (By.ID, 'com.lphtsccft.zlqqt2:id/zll_hq_center_title')

    #国企指数
    hang_seng_china_enterprises_index = (By.XPATH, '//android.widget.TextView[@text ="国企指数"]')
    #红筹指数
    red_chip_index = (By.XPATH, '//android.widget.TextView[@text ="红筹指数"]')
    #变量定义
    # hang_seng_index_expect_name = '恒生指数'
    # hang_seng_china_enterprises_index_expect_name = '国企指数'
    # red_chip_index_expect_name = '红筹指数'

    def click_heng_seng_index(self):
        """
        点击恒生指数
        :return:
        """
        logging.info('点击恒生指数...')
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element(*self.hang_seng_index))
        self.driver.find_element(*self.hang_seng_index).click()
        l = self.get_size()
        self.touch_tap(l[0] * 0.5, l[1] * 0.2578)

    def get_heng_seng_index_page_center_title(self):
        """
        获取恒生指数页面中间title
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*self.hang_seng_index_page))
        except TimeoutException:
            logging.info('超过5秒未找到恒生指数页面中间title')
        else:
            return self.driver.find_element(*self.hang_seng_index_page).text


    def click_hang_seng_china_enterproses_index(self):
        pass
    def click_red_chip_index(self):
        pass