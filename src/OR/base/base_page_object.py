'''
Created on May 4, 2014

@author: citizenchris099
'''

import unittest
import time
 
class BasePageObject(unittest.TestCase):
    '''
    def wait_for_element_displayed_by_xpath(self, driver, locator, timeout=60, msg="[error] element is not found" ):
        for i in range(timeout):
            try:
                if driver.find_element_by_xpath(locator).is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail(msg)
            
            
    def wait_for_element_displayed_by_css_selector(self, driver, locator, timeout=60, msg="[error] element is not found" ):
        for i in range(timeout):
            try:
                if driver.find_element_by_css_selector(locator).is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail(msg)
    '''
    def wait_for_element_displayed_by_xpath(self, driver, locator, timeout=60, msg="[error] element is not found" ):
        for i in range(timeout):
            if driver.find_element_by_xpath(locator).is_displayed(): 
                return
            else: 
                time.sleep(1)
        self.fail(msg)
        return
    
    def wait_for_element_displayed_by_css_selector(self, driver, locator, timeout=60, msg="[error] element is not found" ):
        for i in range(timeout):
            if driver.find_element_by_css_selector(locator).is_displayed(): 
                return
            else: 
                time.sleep(1)
        self.fail(msg)
        return
    
    def wait_for_element_displayed_by_class_name(self, driver, locator, timeout=60, msg="[error] element is not found" ):
        for i in range(timeout):
            if driver.find_element_by_class_name(locator).is_displayed(): 
                return
            else: 
                time.sleep(1)
        self.fail(msg)
        return
                
        