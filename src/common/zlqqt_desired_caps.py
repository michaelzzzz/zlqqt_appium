# coding:utf-8
__author__ = "James"

from appium import webdriver
import yaml
import logging
import logging.config

CON_LOG = './config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def zlqqt_desired():
    """
    app启动配置信息
    :return: driver
    """
    with open('./config/desired_caps.yaml', 'r') as file:
        data = yaml.load(file)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['app'] = data['app']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    logging.info('===================启动app，开始测试=======================')
    # driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    zlqqt_desired()
