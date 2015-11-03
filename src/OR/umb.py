'''
Created on May 6, 2014

@author: cmanning
'''
from OR.locators import locators
from OR.base import selenium_driver
from OR.base.base_page_object import BasePageObject
#from OR.base.base_page_element import BasePageElement
from selenium import webdriver

class User_Menu_Bar(BasePageObject):
    
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_displayed_by_xpath(self.driver,locators["logo"])
        self.wait_for_element_displayed_by_xpath(self.driver,locators["umb"])
        #self.assertEqual("Studio Balfour", self.driver.title)
        
    def admin_db(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["admin_db"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        self.assertEqual("Admin Dashboard | Studio Balfour", self.driver.title)
        
    def user_admin(self):
        driver = selenium_driver.driver
        admindb = driver.find_element_by_xpath(locators["admin_db"])
        useradmin = driver.find_element_by_xpath(locators["user_admin"])

        actions = webdriver.ActionChains(driver)
        actions.move_to_element(admindb)
        actions.click(useradmin)
        actions.perform()
        self.assertEqual("User Admin | Studio Balfour", self.driver.title)
        
    def proj_admin(self):
        driver = selenium_driver.driver
        admindb = driver.find_element_by_xpath(locators["admin_db"])
        useradmin = driver.find_element_by_xpath(locators["proj_admin"])

        actions = webdriver.ActionChains(driver)
        actions.move_to_element(admindb)
        actions.click(useradmin)
        actions.perform()
        self.assertEqual("Project Admin | Studio Balfour", self.driver.title)
        
    def site_admin(self):
        driver = selenium_driver.driver
        admindb = driver.find_element_by_xpath(locators["admin_db"])
        useradmin = driver.find_element_by_xpath(locators["site_admin"])

        actions = webdriver.ActionChains(driver)
        actions.move_to_element(admindb)
        actions.click(useradmin)
        actions.perform()
                
        self.assertTrue('Dashboard' in self.driver.title.encode("utf-8"))
        
    def dashboard_button(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["dashboard_button"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        self.assertEqual("Studio Balfour", self.driver.title)
        
    def user_manager(self):
        driver = selenium_driver.driver
        admindb = driver.find_element_by_xpath(locators["dashboard_button"])
        useradmin = driver.find_element_by_xpath(locators["user_man"])

        actions = webdriver.ActionChains(driver)
        actions.move_to_element(admindb)
        actions.click(useradmin)
        actions.perform()
        self.assertEqual("User Manager | Studio Balfour", self.driver.title)
        
    def project(self):
        driver = selenium_driver.driver
        admindb = driver.find_element_by_xpath(locators["dashboard_button"])
        useradmin = driver.find_element_by_xpath(locators["project"])

        actions = webdriver.ActionChains(driver)
        actions.move_to_element(admindb)
        actions.click(useradmin)
        actions.perform()
        self.assertEqual("Project | Studio Balfour", self.driver.title)
        
    def profile(self):
        driver = selenium_driver.driver
        admindb = driver.find_element_by_xpath(locators["dashboard_button"])
        useradmin = driver.find_element_by_xpath(locators["profile"])

        actions = webdriver.ActionChains(driver)
        actions.move_to_element(admindb)
        actions.click(useradmin)
        actions.perform()
        self.assertEqual("Profile | Studio Balfour", self.driver.title)
        
    def check_user_info(self):
        driver = selenium_driver.driver
        admindb = driver.find_element_by_xpath(locators["dashboard_button"])
        useradmin = driver.find_element_by_xpath(locators["check_user_info"])

        actions = webdriver.ActionChains(driver)
        actions.move_to_element(admindb)
        actions.click(useradmin)
        actions.perform()
        self.assertEqual("Check User Info | Studio Balfour", self.driver.title)
        
    def balfour_tools(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["balfour_tools"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        self.assertEqual("Balfour Tools | Studio Balfour", self.driver.title)
        
    def bt_faq(self):
        driver = selenium_driver.driver
        admindb = driver.find_element_by_xpath(locators["balfour_tools"])
        useradmin = driver.find_element_by_xpath(locators["BT_FAQ"])

        actions = webdriver.ActionChains(driver)
        actions.move_to_element(admindb)
        actions.click(useradmin)
        actions.perform()
        self.assertEqual("FAQ | Studio Balfour", self.driver.title)    
        
    def my_year(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["my_year"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        self.assertEqual("My Year | Studio Balfour", self.driver.title)
        
    def contact(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["contact"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        self.assertEqual("Contact | Studio Balfour", self.driver.title)