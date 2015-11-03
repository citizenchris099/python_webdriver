'''
Created on May 4, 2014
@author: citizenchris099
'''
from OR.locators import locators
from OR.base import selenium_driver
from OR.base.base_page_object import BasePageObject
from OR.base.base_page_element import BasePageElement
#from selenium.webdriver.common.keys import Keys
from OR.base.check_is_displayed import check_is_displayed_by_xpath
from selenium import webdriver


class ProjectElement(BasePageElement):
    def __init__(self):
        self.locator = locators["sbv1_project"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)

class UsernameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["sbv1_uname"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)
 
class PasswordElement(BasePageElement):
    def __init__(self):
        self.locator = locators["sbv1_pword"]
 
    def __set__(self, instance, value):
        driver = selenium_driver.driver
        driver.find_element_by_xpath(self.locator).send_keys(value)
 
class LoginPageObject(BasePageObject):
    project = ProjectElement()
    username = UsernameElement()
    password = PasswordElement()
 
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.driver.get(base_url)
        self.assertTrue(check_is_displayed_by_xpath(locators["sbv1_project"]), "It wasn't true :(")
        self.assertEqual("Studio Balfour", self.driver.title)
 
    def submit(self):
        driver = selenium_driver.driver
        db = driver.find_element_by_xpath(locators["sbv1_login_submit"])
        webdriver.ActionChains(driver).move_to_element(db).click(db).perform()
        
    def do_login(self, project, username, password):
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.project = project
        lpo.username = username
        lpo.password = password
        lpo.submit()