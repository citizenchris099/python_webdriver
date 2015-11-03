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

class UserSearchField(BasePageElement):
    def __init__(self):
        self.locator = locators["um_search_field"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class UserManager(BasePageObject):
    um_search_field = UserSearchField()
    
    def __init__(self, driver):
        self.driver = driver
        self.assertTrue(check_is_displayed_by_xpath(locators["um_create_user"]), "It wasn't true :(")
        self.assertEqual("User Manager | Studio Balfour", self.driver.title)
        
    def um_create_user(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["um_create_user"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        
    def um_search_user(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["um_search"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()