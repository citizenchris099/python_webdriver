'''
Created on May 4, 2014
@author: citizenchris099
'''
from OR.locators import locators
from OR.base import selenium_driver
from OR.base.base_page_object import BasePageObject
#from OR.base.base_page_element import BasePageElement
#from selenium.webdriver.common.keys import Keys
from OR.base.check_is_displayed import check_is_displayed_by_xpath
from selenium import webdriver
 
class LaunchMyYear(BasePageObject):
  
    def __init__(self, driver):
        self.driver = driver
        self.assertTrue(check_is_displayed_by_xpath(locators["pop_link_my"]), "It wasn't true :(")
        self.assertEqual("Studio Balfour", self.driver.title)
 
    def my_launch(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["pop_link_my"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
