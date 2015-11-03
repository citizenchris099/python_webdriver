'''
Created on May 9, 2014

@author: cmanning
'''
from OR.locators import locators
from OR.base import selenium_driver
from OR.base.base_page_object import BasePageObject
from OR.base.base_page_element import BasePageElement
from OR.base.check_is_displayed import check_is_displayed_by_xpath
from selenium import webdriver

class UsernameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["nu_uname"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class EmailElement(BasePageElement):
    def __init__(self):
        self.locator = locators["nu_email"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class PwordElement(BasePageElement):
    def __init__(self):
        self.locator = locators["nu_pword"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class RepPwordElement(BasePageElement):
    def __init__(self):
        self.locator = locators["nu_rep_pword"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class ProjInputElement(BasePageElement):
    def __init__(self):
        self.locator = locators["nu_project_input"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)

class AddNewUser(BasePageObject):
    username = UsernameElement()
    email = EmailElement()
    pword = PwordElement()
    rep_pword = RepPwordElement()
    project_num = ProjInputElement()
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_displayed_by_xpath(self.driver,locators["nu_uname"])
        self.assertTrue('Add New User' in self.driver.title.encode("utf-8"))
        
    def user_role(self, xpath):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(xpath).click()
        
    def project(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["nu_project"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        self.wait_for_element_displayed_by_xpath(self.driver,locators["nu_project_input"])
        
    def project_choice(self):
        driver = selenium_driver.driver
        self.wait_for_element_displayed_by_xpath(self.driver,locators["nu_project_input"])
        db = driver.find_element_by_xpath(locators["nu_project_choice"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        
    def submit_new_user(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["nu_anu"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        self.assertTrue('Users' in self.driver.title.encode("utf-8"))
        
    