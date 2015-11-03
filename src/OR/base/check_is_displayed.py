'''
Created on May 14, 2014

@author: cmanning
'''
from OR.base import selenium_driver
from selenium.common.exceptions import NoSuchElementException
                      
def check_is_displayed(klass_name):
    driver = selenium_driver.driver
    try:
        return driver.find_element_by_class_name(klass_name).is_displayed()
    except NoSuchElementException as nse:
        print nse.message
        
def check_is_displayed_by_xpath(xpath):
    driver = selenium_driver.driver
    try:
        return driver.find_element_by_xpath(xpath).is_displayed()
    except NoSuchElementException as nse:
        print nse.message
        
def check_is_displayed_by_css_selector(css):
    driver = selenium_driver.driver
    try:
        return driver.find_element_by_css_selector(css).is_displayed()
    except NoSuchElementException as nse:
        print nse.message
        
    