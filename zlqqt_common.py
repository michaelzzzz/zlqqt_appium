from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ZlqqtBaseView import ZlqqtBaseView
from zlqqt_desired_caps import logging
from zlqqt_desired_caps import zlqqt_desired

class Common(ZlqqtBaseView):
    permitBtn = (By.ID,'com.android.packageinstaller:id/permission_allow_button')
    confirmBtn = (By.ID,'com.lphtsccft.zlqqt2:id/guide_page_tv_confirm')

    def check_permitBtn(self):
        '''
        点击允许获取手机权限按钮
        :return:
        '''
        logging.info('点击允许获取权限按钮')
        try:
            element = self.driver.find_element(*self.permitBtn)
        except NoSuchElementException:
            logging.info('permitBtn is not found!')
        else:
            logging.info('click permitBtn')
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.permitBtn))
            element.click()

    def check_confirmBtn(self):
        '''
        点击确认按钮进入app
        :return:
        '''
        logging.info('点击确定按钮...')
        try:
            element = self.driver.find_element(*self.confirmBtn)
        except NoSuchElementException:
            logging.info('confirm is not found!')
        else:
            logging.info('click confirmBtn')
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.confirmBtn))
            element.click()

    def swiptleft(self,num=1):
        logging.info('开始滑动')
        for i in range(num):
            ZlqqtBaseView(self.driver).swipt_left()
            sleep(0.5)


    def experienceBtn(self):
        logging.info("点击立即体验")
        l = ZlqqtBaseView(self.driver).get_size()
        ZlqqtBaseView(self.driver).touch_tap(l[0] * 0.5, l[1] * 0.9375)

if __name__ == '__main__':
    driver = zlqqt_desired()
    com = Common(driver)
    com.check_permitBtn()
    com.check_confirmBtn()
    sleep(1)
    com.swiptleft()
    sleep(1)
    com.experienceBtn()