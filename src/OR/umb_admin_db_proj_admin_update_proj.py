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

class CustNumFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["up_cust_num"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class ProjNumFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["up_proj_num"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class ProjNameFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["up_proj_name"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class ProjDesFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["up_proj_des"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class PgNumFieldElement(BasePageElement):
    def __init__(self):
        self.locator = locators["up_num_pages"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).clear()
        driver.find_element_by_css_selector(self.locator).send_keys(value)
        
class UpdateProj(BasePageObject):
    cust_num = CustNumFieldElement()
    proj_num = ProjNumFieldElement()
    proj_name = ProjNameFieldElement()
    proj_des = ProjDesFieldElement()
    pg_num = PgNumFieldElement()
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_displayed_by_xpath(self.driver,locators["up_submit"])
        self.assertEqual("Project Admin | Studio Balfour", self.driver.title)
        
    def update_submit(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["up_submit"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
