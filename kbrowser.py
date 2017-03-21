#  -*- coding:utf-8 -*-
import logging
import logging.config
import json

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# def PrintInfo(info):
# #    print unicode(info,'utf-8').decode('gbk')
#     print info.decode('utf-8').encode('utf-8')  
import threading
#单例类
class Singleton():
    instance=None
    mutex=threading.Lock()
    def _init__(self):
        pass
    @staticmethod
    def GetInstance():
        if(Singleton.instance==None):
            Singleton.mutex.acquire()
            if(Singleton.instance==None):
                #logger.debug('浏览器对象初始化')
                Singleton.instance=webdriver.Firefox()
            #else:
                #logger.debug('浏览器对象已经实例化')
            Singleton.mutex.release()
        #else:
            #logger.debug('浏览器对象已经实例化')
           
        return Singleton.instance
    @staticmethod
    def Destroy():
        Singleton.instance.quit()
        Singleton.instance=None
        return Singleton.instance



