'''
Created on May 4, 2014

@author: citizenchris099
'''
from selenium import webdriver
 
class SeleniumWrapper:
    _instance = None
 
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
            return cls._instance
 
    def connect(self, host="https://studio3-qa.balfour.com/dashboard/login/"):
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '28'
        desired_capabilities['platform'] = 'OS X 10.9'
        desired_capabilities['name'] = 'SBv3 Automation Tests'
        self.driver = webdriver.Remote(desired_capabilities=desired_capabilities,command_executor="http://citizenchris:a8f0eeb8-bb02-4788-b6d1-3680f480930c@ondemand.saucelabs.com:80/wd/hub")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = host
        return self.driver
    
    def connect_sbv1(self, host="http://studio.balfour.com/"):
        desired_capabilities = webdriver.DesiredCapabilities.CHROME
        desired_capabilities['version'] = '26'
        desired_capabilities['platform'] = 'Windows 8.1'
        desired_capabilities['name'] = 'SBv1 Automation Tests'
        self.driver = webdriver.Remote(desired_capabilities=desired_capabilities,command_executor="http://citizenchris:a8f0eeb8-bb02-4788-b6d1-3680f480930c@ondemand.saucelabs.com:80/wd/hub")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = host
        return self.driver