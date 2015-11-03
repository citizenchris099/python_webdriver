'''
Created on May 4, 2014
@author: citizenchris099
'''
from OR.locators import locators
from OR.base import selenium_driver
from OR.base.base_page_object import BasePageObject
from OR.base.base_page_element import BasePageElement
from selenium.webdriver.common.keys import Keys
from OR.base.check_is_displayed import check_is_displayed_by_css_selector



class UsernameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login_username"]
 
    def __set__(self, obj, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).send_keys(value)
 
class PasswordElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login_password"]
 
    def __set__(self, instance, value):
        driver = selenium_driver.driver
        driver.find_element_by_css_selector(self.locator).send_keys(value)
 
class LoginPageObject(BasePageObject):
    username = UsernameElement()
    password = PasswordElement()
 
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.driver.get(base_url)
        self.assertTrue(check_is_displayed_by_css_selector(locators["login_username"]), "It wasn't true :(")
        self.assertEqual("Login | Studio Balfour", self.driver.title)
 
    def submit(self):
        self.driver.find_element_by_css_selector(locators["login_password"]).send_keys(Keys.ENTER)
        self.assertEqual("Studio Balfour", self.driver.title)
        
    def do_login(self, username, password):
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.username = username
        lpo.password = password
        lpo.submit()
        
# class DoLogin(object):
#     @staticmethod
