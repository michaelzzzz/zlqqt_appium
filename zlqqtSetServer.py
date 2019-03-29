# coding=utf-8
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from zlqqt_common import Common
from zlqqt_desired_caps import logging, zlqqt_desired


class zlqqtSetServer(Common):
        #底部tab市场
        market = (By.ID,'com.lphtsccft.zlqqt2:id/main_market')
        #底部tab账户
        account = (By.ID,'com.lphtsccft.zlqqt2:id/main_account')
        #账户页面右上角设置
        account_setting = (By.ID,'com.lphtsccft.zlqqt2:id/account_home_tv_settings')
        #服务器设置
        server_setting = (By.XPATH,'//android.widget.LinearLayout[@index=2]')
        #搜索
        search = (By.ID,'com.lphtsccft.zlqqt2:id/title_bar_right')
        #搜索框
        title_bar_search = (By.ID ,'com.lphtsccft.zlqqt2:id/title_bar_search')
        #交易复选框
        server_kind_trading = (By.ID, 'com.lphtsccft.zlqqt2:id/cb_server_kind_trading')
        #资讯复选框
        server_kind_info = (By.ID, 'com.lphtsccft.zlqqt2:id/cb_server_kind_info')
        #市场复选框
        server_kind_market = (By.ID, 'com.lphtsccft.zlqqt2:id/cb_server_kind_market')
        #端口输入框
        new_server_port = (By.ID, 'com.lphtsccft.zlqqt2:id/et_new_server_port')
        #ip地址输入框
        new_server_address = (By.ID, 'com.lphtsccft.zlqqt2:id/et_new_server_address')
        #添加按钮
        add_new_server_address_port = (By.ID, 'com.lphtsccft.zlqqt2:id/btn_add_new_server_address_port')
        #返回按钮
        return_button = (By.ID, 'com.lphtsccft.zlqqt2:id/title_bar_left')
        #优先使用一下配置
        preference_following_config = (By.ID, 'com.lphtsccft.zlqqt2:id/cb_preferred_configuration')
        #行情服务器
        market_server = (By.ID, 'com.lphtsccft.zlqqt2:id/spn_market_server')
        #交易服务器
        trade_server = (By.ID, 'com.lphtsccft.zlqqt2:id/spn_trading_server')
        #资讯服务器
        info_server = (By.ID, 'com.lphtsccft.zlqqt2:id/spn_info_server')
        #选择行情服务器
        select_market_server = (By.XPATH,'//android.widget.TextView[@index=5]')
        #选择交易服务器
        select_trade_server = (By.XPATH, '//android.widget.TextView[@index=5]')
        #选择资讯服务器
        select_info_server = (By.XPATH, '//android.widget.TextView[@index=5]')
        #服务器设置确定按钮
        server_setting_confirm = (By.ID, 'com.lphtsccft.zlqqt2:id/btn_confirm')
        #服务器设置确定弹框
        server_setting_confirm_up = (By.ID, 'com.lphtsccft.zlqqt2:id/dialog_btn_left')


        #参数
        ps = '.zztzt'
        ip = '122.96.150.162'
        market_port = '17100'
        trade_port = '17300'
        info_port = '17200'

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

        def click_tradeing_check_box(self):
                logging.info('取消勾选交易按钮...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.server_kind_trading))
                self.driver.find_element(*self.server_kind_trading).click()

        def click_info_check_box(self):
                logging.info('取消勾选资讯按钮...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.server_kind_info))
                self.driver.find_element(*self.server_kind_info).click()

        def click_market_check_box(self):
                logging.info('取消勾选行情按钮...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.server_kind_market))
                self.driver.find_element(*self.server_kind_market).click()

        def send_new_market_address(self):
                logging.info('输入ip...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.new_server_address))
                self.driver.find_element(*self.new_server_address).send_keys(self.ip)


        def send_new_market_port(self,port):
                logging.info('输入行情port...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.new_server_port))
                self.driver.find_element(*self.new_server_port).send_keys(port)

        def add_address_port(self):
                logging.info('添加行情ip和端口号...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.add_new_server_address_port))
                self.driver.find_element(*self.add_new_server_address_port).click()

        def clear_port_input_box(self):
                logging.info('清空端口号输入框...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.new_server_port))
                self.driver.find_element(*self.new_server_port).clear()

        def click_return_button(self,num=1):
                logging.info('设置完成，点击返回按钮...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.return_button))
                for i in range(num):
                        self.driver.find_element(*self.return_button).click()

        def click_account(self):
                logging.info('点击账户...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.account))
                self.driver.find_element(*self.account).click()

        def ckick_account_setting(self):
                logging.info('点击账户页面设置...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.account_setting))
                self.driver.find_element(*self.account_setting).click()

        def click_server_setting(self):
                logging.info('点击服务器设置...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.server_setting))
                self.driver.find_element(*self.server_setting).click()

        def click_preference_following_config(self):
                logging.info('点击优先使用一下配置...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.preference_following_config))
                self.driver.find_element(*self.preference_following_config).click()

        def click_market_server(self):
                logging.info('点击行情服务器...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.market_server))
                self.driver.find_element(*self.market_server).click()

        def click_select_market_server(self):
                logging.info('选择行情服务器...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.select_market_server))
                self.driver.find_element(*self.select_market_server).click()

        def click_trade_server(self):
                logging.info('点击交易服务器...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.trade_server))
                self.driver.find_element(*self.trade_server).click()

        def click_select_trade_server(self):
                logging.info('选择交易服务器...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.select_trade_server))
                self.driver.find_element(*self.select_trade_server).click()

        def click_info_server(self):
                logging.info('点击资讯服务器...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.info_server))
                self.driver.find_element(*self.info_server).click()

        def click_select_info_server(self):
                logging.info('选择资讯服务器...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.select_info_server))
                self.driver.find_element(*self.select_info_server).click()

        def click_server_setting_confirm(self):
                logging.info('点击服务器设置确定按钮...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.server_setting_confirm))
                self.driver.find_element(*self.server_setting_confirm).click()

        def click_server_setting_confirm_up(self):
                logging.info('点击服务器设置确定弹框...')
                WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.server_setting_confirm_up))
                self.driver.find_element(*self.server_setting_confirm_up).click()


if __name__ == '__main__':
        driver = zlqqt_desired()
        com = Common(driver)
        com.start_page()

        zl = zlqqtSetServer(driver)
        zl.click_market()
        zl.click_search()
        zl.send_pskeys()
        zl.click_tradeing_check_box()
        zl.click_info_check_box()
        zl.send_new_market_address()
        zl.send_new_market_port(zlqqtSetServer.market_port)
        zl.add_address_port()

        zl.clear_port_input_box()

        zl.click_market_check_box()
        zl.click_tradeing_check_box()
        zl.send_new_market_port(zlqqtSetServer.trade_port)
        zl.add_address_port()

        zl.clear_port_input_box()

        zl.click_tradeing_check_box()
        zl.click_info_check_box()
        zl.send_new_market_port(zlqqtSetServer.info_port)
        zl.add_address_port()

        zl.click_return_button(2)

        zl.click_account()
        zl.ckick_account_setting()
        zl.click_server_setting()
        zl.click_preference_following_config()

        zl.click_market_server()
        zl.click_select_market_server()

        zl.click_trade_server()
        zl.click_select_trade_server()

        zl.click_info_server()
        zl.click_select_info_server()

        zl.click_server_setting_confirm()
        zl.click_server_setting_confirm_up()

        zl.click_return_button(2)






