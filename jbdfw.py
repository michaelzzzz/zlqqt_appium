#coding=utf-8
from datetime import time
from time import sleep

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '9e6585dd'
desired_caps['appPackage'] = 'com.jbdfw.nearme.gamecenter'
desired_caps['appActivity'] = 'com.superh5game.ewan.EwanGameActivity'
desired_caps['noReset'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

sleep(10)
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

l = get_size()
print(l)


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

touch_tap(l[0]*0.5,l[1]*0.88)


sleep(15)

touch_tap(l[0]*0.5,l[1]*0.60)

sleep(3)

for i in range(10000000):
    touch_tap(l[0] * 0.5, l[1] * 0.325)