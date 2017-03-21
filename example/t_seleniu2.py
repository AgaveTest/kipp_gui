from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

browser = webdriver.Firefox()

browser.get('http://127.0.0.1:3023/angular_filter_sort.html')
#assert 'Yahoo!' in browser.title


try:

	elems=browser.find_elements(By.XPATH,"//iframe")

	#elems[0].find_element_by_id("input_text")

	#print elems.get_attribute('src')
	print len(elems)
	for index in range(len(elems)):

		#print elems[index].get_attribute('src')
	 	#print elems[index].get_attribute('frameName')	
	 	try:
	 		browser.switch_to_frame(index)
	 		#elem.find_element_by_id("input_text")
	 		browser.find_element(By.ID,"input_text").send_keys('abc')

	 	except Exception ,err :

	 		print 'exception in:',str(err)
	 	else:
	 		
	 		print 'in else'
	 		break
	 		
	 	finally:
	 		print 'in finally'
	 		browser.switch_to_default_content()
	 	

	 #elem = browser.find_element_by_id('input_text')  # Find the search box

	# elem.send_keys('seleniumhq' + Keys.RETURN)

except Exception ,e :
	
	print 'exception cjs :',e


	# else:
# 	btn=browser.find_element_by_id('su')
# 	btn.click();

#browser.quit()