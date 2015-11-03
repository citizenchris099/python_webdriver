'''
Created on May 9, 2014

@author: cmanning
'''
import unittest
from OR.base import selenium_driver
from OR.test_info import test_info
from OR.sbv1_login import LoginPageObject
from OR.sbv1_db import LaunchMyYear
from OR.my_main import BackToSb
import logging

module_logger = logging.getLogger('testlogger')

# tests the creation of a new user in the WP BE then verifies said user can in fact log in
class TestBeCreateUser(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect_sbv1()
        self.base_url = selenium_driver.base_url
 
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
 
    def test_user_create(self):
        module_logger.info('Starting SBv1 launch MY Test')
        # logs into SBv1 and launches My Year
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.do_login(test_info["sbv1_project"],test_info["sbv1_uname"], test_info["sbv1_pword"])
        module_logger.info('logged in')
        #launches My Year
        lmy = LaunchMyYear(self.driver)
        lmy.my_launch()
        my = BackToSb(self.driver)
        my.back_2_sb()
        
       
        
if __name__ == "__main__":
    import nose
    nose.run(argv=["", "test_be_create_user", "--verbosity=2"])