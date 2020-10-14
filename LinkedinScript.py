
#---------------Imports----------------

import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#---------------SETTINGS----------------

USERNAME = 'your@email'
PASSWORD = 'password'
SEARCH_TERM = 'Recruiter' #['Apple', 'Facebook', 'Intel', 'Microsoft', 'Checkpoint']
LOCATION = 'Israel'
MAX_PEOPLE = 50 #for maximum results set to 50


#---------------------------------------



def main():
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver')
	driver = webdriver.Chrome(DRIVER_PATH)

	driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

	#---LOGIN---
	try:
		driver.find_element_by_id("username").send_keys(USERNAME)
		driver.find_element_by_id("password").send_keys(PASSWORD)
		driver.find_element_by_id("password").send_keys(Keys.RETURN)
	except:
		print("Exception in logging in")
		driver.quit()

	#---SEARCH SETTINGS---
	time.sleep(1)
	driver.get("https://www.linkedin.com/search/results/people/?origin=DISCOVER_FROM_SEARCH_HOME")
	time.sleep(1)
	driver.find_element_by_id("ember157").click()
	
	location_input = driver.find_element_by_xpath("//div[@id='ember161']/input")
	location_input.send_keys(LOCATION)
	location_input.click()
	time.sleep(1)
	location_input.send_keys(Keys.DOWN)
	location_input.send_keys(Keys.RETURN)

	time.sleep(1)
	location_form = driver.find_elements_by_class_name("search-s-facet__form")[1]
	location_form.find_element_by_class_name("facet-collection-list__apply-button").click()

	time.sleep(1)
	search_term = driver.find_element_by_class_name("search-global-typeahead__input")
	search_term.send_keys(SEARCH_TERM)
	search_term.send_keys(Keys.RETURN)
	time.sleep(5)
	#---CONNECTIONS---
	all_people = driver.find_elements_by_class_name("search-result__action-button")
	
	#for people in all_people:
	count=0
	while count<MAX_PEOPLE:
		for li in all_people:
			if li.text == 'Connect':
				li.click()
				time.sleep(0.5)
				try:
					button = driver.find_elements_by_class_name("artdeco-button--3")[1]
					button.click()
				except:
					pass
				count+=1

		#next_btn_location = pyautogui.locateOnScreen('next_btn_img.PNG')
		#print(next_btn_location)
		#pyautogui.click(next_btn_location)

	time.sleep(100)
    










if __name__ == '__main__':
	main()
