'''
Created on May 9, 2014

@author: cmanning
'''
import unittest
from OR.base import selenium_driver
from OR.login import LoginPageObject
from OR.test_info import test_info
from OR.umb import User_Menu_Bar
from OR.umb_siteadmin_wpdb import WpDb
from OR.umb_siteadmin_wpdb_wpusers import Wpusers
from OR.umb_siteadmin_wpdb_wpusers_addnew import AddNewUser
from OR.locators import locators
from OR.umb_siteadmin_wpumb import WpUmb
import logging

module_logger = logging.getLogger('testlogger')

# tests the creation of a new user in the WP BE then verifies said user can in fact log in
class TestBeCreateUser(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.base_url = selenium_driver.base_url
 
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
 
    def test_user_create(self):
        module_logger.info('Starting BE Create User Test')
        # logs in and navigates to WP BE
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.do_login(test_info["login_username"], test_info["login_pword"])
        module_logger.info('logged in')
        # navigates to WP Users page then clicks to create new user
        User_Menu_Bar(self.driver).site_admin()
        module_logger.info('@ WP BE')
 
        WpDb(self.driver).wp_users()
        module_logger.info('@ BE User Page')
       
        Wpusers(self.driver).add_new()
        module_logger.info('@ create user page')
        # enters the new user info
        anu = AddNewUser(self.driver)
        anu.username = test_info["test_username"]
        anu.email = test_info["new_email"]
        anu.pword = test_info["new_pword_strong"]
        anu.rep_pword = test_info["new_pword_strong"]
        anu.user_role(locators["nu_role_adviser"])
        anu.project()
        anu.project_num = test_info["new_user_proj"]
        anu.project_choice()
        # navigates back to SBv3 FE
        WpUmb(self.driver).go_2_FE()
        module_logger.info('@ FE DB')
        
if __name__ == "__main__":
    import nose
    nose.run(argv=["", "test_be_create_user", "--verbosity=2"])