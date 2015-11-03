'''
Created on May 15, 2014

@author: cmanning
'''
from OR.locators import locators
from OR.base import selenium_driver
from OR.base.base_page_object import BasePageObject
from OR.base.base_page_element import BasePageElement
from selenium import webdriver
from OR.base.check_is_displayed import check_is_displayed_by_xpath

class DbProjInputElement(BasePageElement):
    def __init__(self):
        self.locator = locators["db_project_search"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)

class DashBoard(BasePageObject):
    db_project_search = DbProjInputElement()
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_displayed_by_xpath(self.driver,locators["logo"])
        self.wait_for_element_displayed_by_xpath(self.driver,locators["log_out_button"])
        self.assertEqual("Studio Balfour", self.driver.title)
        
    def log_out(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["log_out_button"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        self.assertEqual("Login | Studio Balfour", self.driver.title)
        self.assertTrue(check_is_displayed_by_xpath(locators["logged_out"]), "It wasn't true :(")
        
    def db_project(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["db_project"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        #self.wait_for_element_displayed_by_xpath(self.driver,locators["db_project_search"])
        
    def db_project_choice(self):
        driver = selenium_driver.driver
        #self.wait_for_element_displayed_by_xpath(self.driver,locators["db_project_search"])
        db = driver.find_element_by_xpath(locators["db_project_results"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()