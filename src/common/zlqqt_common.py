# coding:utf-8
__author__ = "James"

from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.common.ZlqqtBaseView import ZlqqtBaseView
from src.common.zlqqt_desired_caps import logging
from src.common.zlqqt_desired_caps import zlqqt_desired


class Common(ZlqqtBaseView):
    # 允许获取手机权限按钮
    permitBtn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    # 确定按钮
    confirmBtn = (By.ID, 'com.lphtsccft.zlqqt2:id/guide_page_tv_confirm')
    # 今日有新股申购关闭按钮
    new_stock_widget_close = (By.ID, 'com.lphtsccft.zlqqt2:id/ipo_dialog_close')

    def check_permitBtn(self):
        """
        点击允许获取手机权限按钮
        :return:
        """
        logging.info('点击允许获取权限按钮...')
        try:
            element = self.driver.find_element(*self.permitBtn)
        except NoSuchElementException:
            logging.info('permitBtn is not found!')
        else:
            logging.info('click permitBtn')
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.permitBtn))
            element.click()

    def check_confirmBtn(self):
        """
        点击确认按钮进入app
        :return:
        """
        try:
            element = self.driver.find_element(*self.confirmBtn)
        except NoSuchElementException:
            logging.info('confirm is not found!')
        else:
            logging.info('click confirmBtn')
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.confirmBtn))
            element.click()

    def get_size(self):
        """
        获取屏幕分辨率
        :param driver:
        :return: x:横屏;y:竖屏
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipt_left(self):
        """
        对屏幕进行左滑操作
        :return:
        """
        l = self.get_size()
        x1 = int(l[0] * 0.90)
        x2 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.50)
        return self.driver.swipe(x1, y1, x2, y1, 1000)

    def swipt_right(self):
        """
        对屏幕进行右滑操作
        :return:
        """
        l = self.get_size()
        x1 = int(l[0] * 0.10)
        x2 = int(l[0] * 0.90)
        y1 = int(l[1] * 0.50)
        return self.driver.swipt(x1, y1, x2, y1, 1000)

    def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        """
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_tap(277,431)      #277.431为点击某个元素的x与y值
        """
        # 获取当前屏幕的宽
        screen_width = self.driver.get_window_size()['width']
        # 获取当前屏幕的高
        screen_height = self.driver.get_window_size()['height']
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        return self.driver.tap([(x1, y1), (x1, y1)], duration)

    def swiptleft_bootpage(self, num=1):
        """
        app引导图左滑
        :param num: 左滑次数
        """
        logging.info('开始滑动')
        for i in range(num):
            self.swipt_left()
            sleep(0.5)

    def experience_button(self):
        """
        点击立即体验
        """
        logging.info("点击立即体验")
        l = self.get_size()
        self.touch_tap(l[0] * 0.5, l[1] * 0.9375)

    def click_new_stock_widget_close(self):
        """
        点击今日新股申购弹窗关闭按钮
        """
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*self.new_stock_widget_close))
        self.driver.find_element(*self.new_stock_widget_close).click()

    def start_page(self):
        """
        启动app页面
        :return:
        """
        self.check_permitBtn()
        self.check_confirmBtn()
        sleep(1)
        self.swiptleft_bootpage(3)
        sleep(1)
        self.experience_button()
        self.click_new_stock_widget_close()


if __name__ == '__main__':
    driver = zlqqt_desired()
    com = Common(driver)
    com.start_page()
