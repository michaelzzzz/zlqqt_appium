# coding:utf-8
import multiprocessing
import subprocess
from time import ctime

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
# with open('./config/desired_caps.yaml', 'r') as file:
#     data = yaml.load(file)
#
# devices_list = ['127.0.0.1:62001','127.0.0.1:62026']
#
# def zlqqt_desired(udid,port):
#     desired_caps={}
#     desired_caps['platformName']=data['platformName']
#     desired_caps['platformVersion']=data['platformVersion']
#     desired_caps['deviceName']=data['deviceName']
#     desired_caps['udid']=udid
#
#     desired_caps['app']=data['app']
#     desired_caps['appPackage']=data['appPackage']
#     desired_caps['appActivity']=data['appActivity']
#     desired_caps['noReset']=data['noReset']
#
#     print('appium port:%s start run %s at %s' %(port, udid, ctime()))
#     logging.info('===================启动app，开始测试=======================')
#     driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub', desired_caps)
#     #driver.implicitly_wait(5)
#     return driver
#
# #构建desired进程租
# desired_process=[]
#
# #加载desied进程
# for i in range(len(devices_list)):
#     port = 4723 + 2 * i
#     desired=multiprocessing.Process(target=zlqqt_desired,args=(devices_list[i],port))
#     desired_process.append(desired)
#
# if __name__ == '__main__':
#     # 启动多设备执行测试
#     for desired in desired_process:
#         desired.start()
#     for desired in desired_process:
#         desired.join()