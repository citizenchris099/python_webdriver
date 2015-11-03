'''
Created on May 7, 2014

@author: cmanning
'''
from OR.locators import locators
from OR.base import selenium_driver
from OR.base.base_page_object import BasePageObject
from OR.base.base_page_element import BasePageElement
from selenium import webdriver

class ProjSearchFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["pa_search_field"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)
        
class SearchProject(BasePageObject):
    search = ProjSearchFieldElement()
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_displayed_by_xpath(self.driver,locators["pa_search"])
        self.assertEqual("Project Admin | Studio Balfour", self.driver.title)
        
    def project_search(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["pa_search"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        
    def proj_search_results(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["pa_search_results"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        
class CreateProject(BasePageObject):
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_displayed_by_xpath(self.driver,locators["pa_create_proj"])
        self.assertEqual("Project Admin | Studio Balfour", self.driver.title)
        
    def create_proj(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["pa_create_proj"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        
class UpdateProject(BasePageObject):
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_displayed_by_xpath(self.driver,locators["pa_update_proj"])
        self.assertEqual("Project Admin | Studio Balfour", self.driver.title)
        
    def update_project(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["pa_update_proj"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()