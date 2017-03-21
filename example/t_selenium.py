from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

browser = webdriver.Firefox()

browser.get('http://127.0.0.1:3023/')
#assert 'Yahoo!' in browser.title


try:

	elem = browser.find_element_by_id('input_text')  # Find the search box
	elem.send_keys('7100' + Keys.RETURN)


except Exception ,e :
	
	print 'exception cjs :',str(e)
else:
	btn=browser.find_element_by_id('input_button')
	btn.click();

#browser.quit()