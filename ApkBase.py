#!usr/bin/python
# -*- coding:utf-8 -*-
import os
import subprocess

import yaml

cmd = "aapt dump badging ./zlgapp-release-unsigned.apk | findstr versionName"
cmd1 = "adb --version"
print(cmd)
result = ""
p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)


(statoutdata, staterr) = p.communicate()
# print(statoutdata)
# print(staterr)
# print(p.communicate())
if statoutdata != "":
    result = statoutdata.split()[3].decode()[12:]
print (result)


cmd = "aapt dump badging " + "./zlgapp-release-unsigned.apk" + " | findstr application-label: "
result = ""
p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
if output != "":
        result = output.split()[0].decode()[18:]
print (result)

cmd = "aapt dump badging " + "./zlgapp-release-unsigned.apk" + " | findstr package:"
result = ""
p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
if output != "":
    result = output.split()[1].decode()[6:-1]
print(result)

cmd = "aapt dump badging " + "./zlgapp-release-unsigned.apk" + " | findstr versionCode"
result = ""
p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
if output != "":
    result = output.split()[2].decode()[12:]
print(result)

filepath = os.path.abspath(os.path.dirname(__file__)) + '\config\config.yaml'
print(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.dirname(__file__))
print(filepath)
with open(filepath, 'rb') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print('yaml读取有误')
        print(exc)
    finally:
        stream.close()