'''
Created on Jun 3, 2014

@author: cmanning
'''
import unittest
from OR.base import selenium_driver
from OR.login import LoginPageObject
from OR.test_info import test_info
from OR.umb_db import DashBoard
import logging

module_logger = logging.getLogger('testlogger')

# tests assigning a project(s) to a user on the FE
class TestFeAssignProject(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.base_url = selenium_driver.base_url
 
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
 
    def test_assign_project(self):
        module_logger.info('Starting FE Assign Project Test')
        # logs in and navigates to WP BE
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.do_login(test_info["login_username"], test_info["login_pword"])
        module_logger.info('logged in')
        db = DashBoard(self.driver)
        db.db_project()
        db.db_project_search = test_info["project_search"]
        db.db_project_choice()
        
if __name__ == "__main__":
    import nose
    nose.run(argv=["", "test_be_create_user", "--verbosity=2"])