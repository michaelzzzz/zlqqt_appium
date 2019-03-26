#coding=utf-8
from datetime import time
from time import sleep

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import yaml
import logging

from selenium.webdriver.support.wait import WebDriverWait

file = open('./config/desired_caps.yaml','r')
data = yaml.load(file)

logging.basicConfig(level=logging.INFO,filename='runlog.log',format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['platformVersion'] = data['platformVersion']
desired_caps['deviceName'] = data['deviceName']
desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
desired_caps['app'] = data['app']
desired_caps['noReset'] = data['noReset']
logging.info('-------------------------开始测试-------------------------')
driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
logging.info('点击允许按钮...')
try:
    permit_button = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')

except NoSuchElementException:
    print('no permit_button')
else:
    permit_button.click()

logging.info('点击确定按钮进入app...')
try:
    confirm_button = driver.find_element_by_id('com.lphtsccft.zlqqt2:id/guide_page_tv_confirm')
except NoSuchElementException:
    print('no confirm_button')
else:
    confirm_button.click()

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

l = get_size()
logging.info(l)

def swiptleft():
    l = get_size()
    x1 = int(l[0]*0.9)
    x2 = int(l[0]*0.1)
    y1 = int(l[1]*0.5)
    driver.swipe(x1,y1,x2,y1,1000)

sleep(1)

logging.info('开始滑动...')
for i in range(3):
    swiptleft()
    sleep(0.5)

sleep(1)


def touch_tap(x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
    '''
    method explain:点击坐标
    parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
    Usage:
        device.touch_tap(277,431)      #277.431为点击某个元素的x与y值
    '''
    screen_width = driver.get_window_size()['width']  # 获取当前屏幕的宽
    screen_height = driver.get_window_size()['height']  # 获取当前屏幕的高
    a = (float(x) / screen_width) * screen_width
    x1 = int(a)
    b = (float(y) / screen_height) * screen_height
    y1 = int(b)
    driver.tap([(x1, y1), (x1, y1)], duration)

driver.implicitly_wait(3)
touch_tap(l[0]*0.5,l[1]*0.9375)

sleep(1)

try:
    close_button = driver.find_element_by_id('com.lphtsccft.zlqqt2:id/ipo_dialog_close')
except NoSuchElementException:
    logging.info("no close_button")
else:
    close_button.click()

logging.info('点击市场...')
WebDriverWait(driver,5).until(lambda x:x.find_element_by_id('com.lphtsccft.zlqqt2:id/main_market'))
market = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/main_market").click()

logging.info('点击搜索...')
WebDriverWait(driver,5).until(lambda x:x.find_element_by_id('com.lphtsccft.zlqqt2:id/title_bar_right'))
search = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/title_bar_right").click()

logging.info('点击搜索框,输入????')
WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('com.lphtsccft.zlqqt2:id/title_bar_search'))
send_keys = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/title_bar_search").send_keys("?????")

logging.info('取消勾选交易、资讯按钮...')
server_kind_trading = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_trading").click()
server_kind_info = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_info").click()

logging.info('添加行情ip：port')
new_server_ip = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/et_new_server_address").send_keys("122")
port = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/et_new_server_port")
port.send_keys("hkport")
add_ip_port = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/btn_add_new_server_address_port")
add_ip_port.click()

logging.info('取消勾选行情按钮，勾选交易按钮...')
el9 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_market").click()
el10 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_trading").click()

logging.info('清除行情port，添加交易port...')
port.clear()
port.send_keys("tradeport")
add_ip_port.click()

logging.info('取消勾选行情按钮，勾选交易按钮...')
el13 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_trading").click()
el14 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/cb_server_kind_info").click()

logging.info('清除交易port，添加资讯port...')
port.clear()
port.send_keys("mesport")
add_ip_port.click()

el17 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/title_bar_left").click()
el18 = driver.find_element_by_id("com.lphtsccft.zlqqt2:id/title_bar_left").click()

logging.info('测试结束...')