'''
Created on May 9, 2014

@author: cmanning
'''
import unittest
import logging
from OR.locators import locators
from OR.test_info import test_info
from OR.base import selenium_driver
from OR.login import LoginPageObject
from OR.umb import User_Menu_Bar
from OR.umb_user_manager import UserManager
from OR.umb_user_manager_create_user import UmCreateUser
import time
from OR.base.check_is_displayed import check_is_displayed_by_xpath

module_logger = logging.getLogger('testlogger')

# tests the creation of a new user in the WP BE then verifies said user can in fact log in
class TestFeCreateUser(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.base_url = selenium_driver.base_url
 
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
 
    def test_user_create(self):
        # logs in and navigates to FE User Manager
        module_logger.info('Starting FE Create User Test')
        '''
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.username = test_info["login_username"]
        lpo.password = test_info["login_pword"]
        lpo.submit()
        '''
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.do_login(test_info["login_username"], test_info["login_pword"])
        module_logger.info('logged in')
        User_Menu_Bar(self.driver).user_manager()
        module_logger.info('@ user manager page')
        # Clicks to create a new user from the User Manager page then proceeds to create user
        um = UserManager(self.driver)
        um.um_create_user()
        module_logger.info('@ user manager create user page')
        cu = UmCreateUser(self.driver)
        cu.user_name = test_info["test_username"]
        cu.first_name = test_info["new_first_name"]
        cu.last_name = test_info["new_last_name"]
        cu.email = test_info["new_email"]
        cu.phone = test_info["new_phone"]
        cu.new_pword = test_info["new_pword_strong"]
        cu.con_pword = test_info["new_pword_strong"]
        cu.user_role(locators["um_role_adviser"])
        cu.create_user_submit()
        time.sleep(10)
        um.um_search_user()
        um.um_search_field = test_info["new_first_name"]
        time.sleep(5)
        self.assertTrue(check_is_displayed_by_xpath(locators["um_search_results"]), "It wasn't true :(")
        module_logger.info('FE Create User Test complete')
        
if __name__ == "__main__":
    import nose
    nose.run(argv=["", "test_be_create_user", "--verbosity=2"])