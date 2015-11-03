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
from OR.base.check_is_displayed import check_is_displayed_by_css_selector

class UserNameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["um_uname"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)

class FirstNameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["um_fname"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class LastNameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["um_lname"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class EmailFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["um_email"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class PhoneFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["um_tel"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class NewPwordFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["um_pword"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class ConNewPwordFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["um_con_pword"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class UmCreateUser(BasePageObject):
    user_name = UserNameElement()
    first_name = FirstNameElement()
    last_name = LastNameElement()
    email = EmailFieldElement()
    phone = PhoneFieldElement()
    new_pword = NewPwordFieldElement()
    con_pword = ConNewPwordFieldElement()
    
    def __init__(self, driver):
        self.driver = driver
        self.assertTrue(check_is_displayed_by_css_selector(locators["um_submit"]), "It wasn't true :(")
        self.assertEqual("User Manager | Studio Balfour", self.driver.title)
        
    def user_role(self, xpath):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(xpath).click()
        
    def create_user_submit(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_css_selector(locators["um_submit"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        
