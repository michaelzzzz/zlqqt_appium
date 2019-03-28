# coding=utf-8
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from zlqqt_common import Common
from zlqqt_desired_caps import logging, zlqqt_desired


class zlqqtSetServer(Common):
        market = (By.ID,'com.lphtsccft.zlqqt2:id/main_market')
        search = (By.ID,'com.lphtsccft.zlqqt2:id/title_bar_right')
        title_bar_search = (By.ID ,'com.lphtsccft.zlqqt2:id/title_bar_search')
        server_kind_trading = (By.ID, 'com.lphtsccft.zlqqt2:id/cb_server_kind_trading')
        server_kind_info = (By.ID, 'com.lphtsccft.zlqqt2:id/cb_server_kind_info')
        server_kind_market = (By.ID, 'com.lphtsccft.zlqqt2:id/cb_server_kind_market')
        new_server_port = (By.ID, 'com.lphtsccft.zlqqt2:id/et_new_server_port')
        new_server_address = (By.ID, 'com.lphtsccft.zlqqt2:id/et_new_server_address')
        add_new_server_address_port = (By.ID, 'com.lphtsccft.zlqqt2:id/btn_add_new_server_address_port')
        ps = ''
        ip = ''
        market_port = ''
        trade_port = ''
        info_port = ''

        def click_market(self):
                logging.info('点击行情...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.market))
                self.driver.find_element(*self.market).click()


        def click_search(self):
                logging.info('点击搜索...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.search))
                self.driver.find_element(*self.search).click()

        def send_pskeys(self):
                logging.info('输入zztzt...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.title_bar_search))
                self.driver.find_element(*self.title_bar_search).send_keys(self.ps)

        def click_tradeing(self):
                logging.info('取消勾选交易按钮...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.server_kind_trading))
                self.driver.find_element(*self.server_kind_trading).click()

        def click_info(self):
                logging.info('取消勾选资讯按钮...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.server_kind_info))
                self.driver.find_element(*self.server_kind_info).click()

        def send_new_market_address(self):
                logging.info('输入ip...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.new_server_address))
                self.driver.find_element(*self.new_server_address).send_keys(self.ip)


        def send_new_port(self):
                logging.info('输入行情port...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.new_server_port))
                self.driver.find_element(*self.new_server_port).send_keys(self.market_port)

        def add_address_port(self):
                logging.info('添加行情ip和端口号...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.add_new_server_address_port))
                self.driver.find_element(*self.add_new_server_address_port).click()


if __name__ == '__main__':
        driver = zlqqt_desired()
        com = Common(driver)
        com.check_permitBtn()
        com.check_confirmBtn()
        sleep(1)
        com.swiptleft()
        sleep(1)
        com.experienceBtn()

        zl = zlqqtSetServer(driver)
        zl.click_market()
        zl.click_search()
        zl.send_pskeys()
        zl.click_tradeing()
        zl.click_info()
        zl.send_new_market_address()
        zl.send_new_port()
        zl.add_address_port()


        # logging.info('点击行情...')
        # WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.lphtsccft.zlqqt2:id/main_market'))
        # market = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/main_market").click()
        #
        # logging.info('点击搜索...')
        # WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.lphtsccft.zlqqt2:id/title_bar_right'))
        # search = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/title_bar_right").click()
        #
        # logging.info('点击搜索框,输入????')
        # WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id('com.lphtsccft.zlqqt2:id/title_bar_search'))
        # send_keys = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/title_bar_search").send_keys("?????")
        #
        # logging.info('取消勾选交易、资讯按钮...')
        # server_kind_trading = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_trading").click()
        # server_kind_info = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_info").click()
        #
        # logging.info('添加行情ip：port')
        # new_server_ip = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/et_new_server_address").send_keys("122")
        # port = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/et_new_server_port")
        # port.send_keys("hkport")
        # add_ip_port = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/btn_add_new_server_address_port")
        # add_ip_port.click()
        #
        # logging.info('取消勾选行情按钮，勾选交易按钮...')
        # el9 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_market").click()
        # el10 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_trading").click()
        #
        # logging.info('清除行情port，添加交易port...')
        # port.clear()
        # port.send_keys("tradeport")
        # add_ip_port.click()
        #
        # logging.info('取消勾选行情按钮，勾选交易按钮...')
        # el13 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_trading").click()
        # el14 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_info").click()
        #
        # logging.info('清除交易port，添加资讯port...')
        # port.clear()
        # port.send_keys("mesport")
        # add_ip_port.click()
        #
        # el17 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/title_bar_left").click()
        # el18 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/title_bar_left").click()