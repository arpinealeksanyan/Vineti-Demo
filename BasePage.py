import os, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 

class BasePage:
	
	def __init__(self, driver):
		self.driver=driver

	def do_click(self, locator):
		self.driver.find_element_by_xpath(locator[1]).click()

	def do_send_keys(self, locator, text):
		self.driver.find_element_by_xpath(locator[1]).send_keys(text)

	def get_element_text(self, locator):
		return self.driver.find_element_by_xpath(locator[1]).text

	def return_elements_list(self, locator):
		return self.driver.find_elements_by_xpath(locator[1])

	def return_element(self, locator):
		return self.driver.find_element_by_xpath(locator[1])

	def hover_element(self, element):
		action = ActionChains(self.driver) 
		action.move_to_element(element)
		action.perform()




    	
