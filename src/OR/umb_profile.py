'''
Created on May 13, 2014

@author: cmanning
'''
'''
Created on May 12, 2014

@author: cmanning
'''
from OR.locators import locators
from OR.base import selenium_driver
from OR.base.base_page_object import BasePageObject
from OR.base.base_page_element import BasePageElement
from selenium import webdriver
from OR.base.check_is_displayed import check_is_displayed_by_xpath

class FirstNameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["prof_first"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class LastNameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["prof_last"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class EmailFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["prof_email"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class PhoneFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["prof_phone"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class CurPwordFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["prof_cur_pword"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class NewPwordFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["prof_pword"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class ConNewPwordFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["prof_con_pword"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class UpdateProfile(BasePageObject):
    first_name = FirstNameElement()
    last_name = LastNameElement()
    email = EmailFieldElement()
    phone = PhoneFieldElement()
    current_pword = CurPwordFieldElement()
    new_pword = NewPwordFieldElement()
    con_pword = ConNewPwordFieldElement()
    
    def __init__(self, driver):
        self.driver = driver
        self.assertTrue(check_is_displayed_by_xpath(locators["prof_submit"]), "It wasn't true :(")
        self.assertEqual("Profile | Studio Balfour", self.driver.title)
        
    def update_profile_submit(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["prof_submit"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        
