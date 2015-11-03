'''
Created on May 9, 2014

@author: cmanning
'''
import unittest
import time
import logging
from OR.base import selenium_driver
from OR.login import LoginPageObject
from OR.umb import User_Menu_Bar
from OR.umb_admin_db_proj_admin import SearchProject
from OR.umb_admin_db_proj_admin import UpdateProject
from OR.umb_admin_db_proj_admin_update_proj import UpdateProj
from OR.locators import locators
from OR.test_info import test_info

module_logger = logging.getLogger('testlogger')

# tests that projects accessed using the FE Project Update page retain updates entered
class TestFeUpdateProject(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.driver.implicitly_wait(10)
        self.base_url = selenium_driver.base_url
 
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
 
    def test_update_proj(self):
        # log in
        module_logger.info('Started Update Project Test')
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.do_login(test_info["login_username"], test_info["login_pword"])
        module_logger.info('Logged In')
        # navigates to project admin and waits for list to populate
        User_Menu_Bar(self.driver).proj_admin()
        module_logger.info('@ Project Admin Page')
        time.sleep(10)
        # searches for project / clicks to update / enters new proj name
        sp = SearchProject(self.driver)
        self.search_project(sp)    
        up = UpdateProj(self.driver)
        up.proj_des = "Veggie Smurf School"
        up.update_submit()
        module_logger.info('back @ Project Admin Page') 
        # re-searches for project and assets new proj name update was retained 
        time.sleep(10)
        self.search_project(sp) 
        module_logger.info('back @ Project Page')   
        self.assertEquals("Veggie Smurf School", self.driver.find_element_by_css_selector(locators["up_proj_des"]).get_attribute("value"))
        module_logger.info('Update Project Test Complete')

    def search_project(self, sp):
        sp.project_search()
        sp.search = test_info["first_name"]
        sp.proj_search_results()
        UpdateProject(self.driver).update_project()
        module_logger.info('@ Project Page')

        
if __name__ == "__main__":
    import nose
    nose.run(argv=["", "test_fe_update_project", "--verbosity=2"])
        