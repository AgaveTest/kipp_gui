#  -*- coding:utf-8 -*-
import logging
import logging.config
import json
import kbrowser

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from time import sleep


def run(data):
	logger.debug("IN GUISERVER")
	#logger.debug(data)
	result=getResult('fail')
	if(getData(data,'keyword')=="open"):
		result=open(data)
	if(getData(data,'keyword')=="type"):
		result=type(data)
	if(getData(data,'keyword')=="close"):
		result=close(data)
	return result

def open(data):
	result=getResult('fail')

	try:
		browser = kbrowser.Singleton.GetInstance()
		open_url=getData(data,'url')
		logger.debug("IN OPEN ["+open_url+"]")
		browser.get(open_url)
		result['result']='success'
		sleep(getData(data,'waittime'))
	except Exception ,e :
		logger.error(e)
		result['errormsg']=str(e)
	finally:
		return result

def type(data):

	logger.debug("IN TYPE")
	result=getResult('fail')
	
	Elements=data['Remotedata']['elements']

	for element in Elements:

		if element['type']=='input':
			result=input(element)
		if element['type']=='button':
			result=click(element)
		sleep(getData(data,'waittime'))

	return result


def input(element):
	logger.debug("IN Input")
	result=getResult('fail')
	try:
		browser = kbrowser.Singleton.GetInstance()
		getElem(element['locations']).send_keys(element['inputValue'])
		logger.debug("In input value:["+element['inputValue']+"]")
		result['result']='success'
			
	except Exception,e:
		logger.error(e)
		result['errormsg']=str(e)
	finally:
		return result


def click(element):
	
	result=getResult('fail')

	try:
		browser = kbrowser.Singleton.GetInstance()
		getElem(element['locations']).click()
		logger.debug("In Click")
		result['result']='success'
			
	except Exception,e:
		logger.error(e)
		result['errormsg']=str(e)

	return result

def close(data):
	logger.debug("IN Close")
	kbrowser.Singleton.Destroy()
	result=getResult('success')
	return result

def getData(idata,name):
	if(name=='keyword'):
		return idata['Remotedata']['keyword']
	if(name=='url'):
		if idata['Remotedata']['url']== None:
			return idata['Commondata']['Gui_dfl_Value']['url']
		return idata['Remotedata']['url']
	if(name=='waittime'):
		dafult_wtime=int(idata['Commondata']['WaitTime']['dafult_wtime'])/1000
		#logger.debug("dafult_wtime type: ",dafult_wtime)
		return dafult_wtime

def getElem(locations):

	browser = kbrowser.Singleton.GetInstance()
	for location in locations:
		if(location['type']=='id'):
			logger.debug("get element by id: ["+location['text']+"]")
			return findElement(By.ID,location['text'])			
		if(location['type']=='name'):
			logger.debug("get element by name: ["+location['text']+"]")
			return findElement(By.NAME,location['text'])		
		if(location['type'])=='xpath':
			logger.debug("get element by xpath: ["+location['text']+"]")
			return findElement(By.XPATH,location['text'])
			#def get_element_by_id(self,location):

# ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"


def isGetElement(by=By.ID,location='input_text'):

	try:
	 	#elem.find_element_by_id("input_text")
	 	kbrowser.Singleton.GetInstance().find_element(by,location)
	 	return True
	except Exception ,err :
		return False

def  findElement(by=By.ID,location='input_text'):

	res=None

	if isGetElement(by,location):
		res=kbrowser.Singleton.GetInstance().find_element(by,location)
		return res

	if isGetElement(By.XPATH,"//iframe"):
		
		elems=kbrowser.Singleton.GetInstance().find_elements(By.XPATH,"//iframe")
		for index in range(len(elems)):

		 	kbrowser.Singleton.GetInstance().switch_to_frame(index)
		 		#elem.find_element_by_id("input_text")
		 	if(isGetElement(by,location)):
		 		res=kbrowser.Singleton.GetInstance().find_element(by,location)
		 		break
		 	else:
		 		kbrowser.Singleton.GetInstance().switch_to_default_content()

	if res is None:
	   raise WebDriverException("Can't find element ["+location+"]")
	else:
	   return res

def getResult(str):
	return {'result':str}











