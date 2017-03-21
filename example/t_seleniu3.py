from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import json

browser = webdriver.Firefox()

browser.get('http://127.0.0.1:3023')

#def get_element(self,by=By.ID,location):

	
def isGetElement(by=By.ID,location='input_text'):

	try:
	 	#elem.find_element_by_id("input_text")
	 	browser.find_element(by,location)
	 	return True
	except Exception ,err :
		return False

def  findElement(by=By.ID,location='input_text'):

	res=None

	if isGetElement(by,location):
		res=browser.find_element(by,location)
		return res

	if isGetElement(By.XPATH,"//iframe"):
		
		elems=browser.find_elements(By.XPATH,"//iframe")
		for index in range(len(elems)):

		 	browser.switch_to_frame(index)
		 		#elem.find_element_by_id("input_text")
		 	if(isGetElement(by,location)):
		 		res=browser.find_element(by,location)
		 		break
		 	else:
		 		browser.switch_to_default_content()

	if res is None:
	   raise WebDriverException("Can't find element"+location)
	else:
	   return res

	

	# if isGetElement(By.XPATH,"//iframe"):
		
	# 	elems=browser.find_elements(By.XPATH,"//iframe")
	# 	for index in range(len(elems)):

	# 	 	browser.switch_to_frame(index)
	# 	 		#elem.find_element_by_id("input_text")
	# 	 	if(isGetElement(by,location)):
	# 	 		res=browser.find_element(by,location)
	# 	 		break
	# 	 	else:
	# 	 		browser.switch_to_default_content()

    # if res is None:
    # 	print "exception"
    # 	#raise WebDriverException("can't find element"+location)
    # else:
    # 	return res

findElement().send_keys('abc')


