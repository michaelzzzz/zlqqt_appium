# coding:utf-8
__author__ = "James"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.common.zlqqt_common import Common
from src.common.zlqqt_desired_caps import logging, zlqqt_desired


class ButtonTabView(Common):
    main_indexpage = (By.ID, 'com.lphtsccft.zlqqt2:id/main_indexpage')
    main_market = (By.ID, 'com.lphtsccft.zlqqt2:id/main_market')
    main_trade = (By.ID, 'com.lphtsccft.zlqqt2:id/main_trade')
    main_account = (By.ID, 'com.lphtsccft.zlqqt2:id/main_account')

    def click_main_indexpage(self):
        logging.info('点击首页...')
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.main_indexpage))
        self.driver.find_element(*self.main_indexpage).click()

    def click_main_market(self):
        logging.info('点击行情...')
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.main_market))
        self.driver.find_element(*self.main_market).click()

    def click_main_trade(self):
        logging.info('点击交易...')
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.main_trade))
        self.driver.find_element(*self.main_trade).click()

    def click_main_account(self):
        logging.info('点击账户...')
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.main_account))
        self.driver.find_element(*self.main_account).click()

if __name__ == '__main__':
    driver = zlqqt_desired()
    bt = ButtonTabView(driver)
    bt.common_openation()
    bt.click_main_indexpage()
    bt.click_main_account()
    bt.click_main_trade()
    bt.click_main_market()

