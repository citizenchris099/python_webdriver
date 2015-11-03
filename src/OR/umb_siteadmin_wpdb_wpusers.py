'''
Created on May 9, 2014

@author: cmanning
'''
from OR.locators import locators
from OR.base import selenium_driver
from OR.base.base_page_object import BasePageObject
#from OR.base.base_page_element import BasePageElement
from selenium import webdriver

class Wpusers(BasePageObject):
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_displayed_by_xpath(self.driver,locators["addnewuser"])
        self.assertTrue('Users' in self.driver.title.encode("utf-8"))
        
    def add_new(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["addnewuser"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        self.assertTrue('Add New User' in self.driver.title.encode("utf-8"))