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
 
class BackToSb(BasePageObject):
  
    def __init__(self, driver):
        self.driver = driver
        self.assertTrue(check_is_displayed_by_xpath(locators["MY_logo"]), "It wasn't true :(")
        self.assertEqual("MyYear Editor", self.driver.title)
 
    def back_2_sb(self):
        driver = selenium_driver.driver
        usermenu = driver.find_element_by_xpath(locators["user_menu"])
        back2sb = driver.find_element_by_xpath(locators["back_2_sb"])

        actions = webdriver.ActionChains(driver)
        actions.move_to_element(usermenu)
        actions.click(back2sb)
        actions.perform()
        self.assertEqual("Studio Balfour", self.driver.title)
