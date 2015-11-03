'''
Created on May 9, 2014

@author: cmanning
'''
import unittest
from OR.base import selenium_driver
from OR.login import LoginPageObject
from OR.umb import User_Menu_Bar
from OR.umb_admin_db_proj_admin import SearchProject
from OR.umb_admin_db_proj_admin import CreateProject
from OR.umb_admin_db_proj_admin import UpdateProject
from OR.umb_admin_db_proj_admin_create_proj import CreateProj
from OR.locators import locators
from OR.test_info import test_info
import time
import logging

module_logger = logging.getLogger('testlogger')

# tests creating a project via the FE Project Admin Create Project Page
class TestFeCreateProject(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.base_url = selenium_driver.base_url
 
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
 
    def test_create_project(self):
        module_logger.info('Started FE Create Project Test')
        # logs in and navigates to proj admin
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.do_login(test_info["login_username"], test_info["login_pword"])
        module_logger.info('logged in')
        User_Menu_Bar(self.driver).proj_admin()
        module_logger.info('@ project admin page')
        # clicks create project and proceeds to do so
        CreateProject(self.driver).create_proj()
        cp = CreateProj(self.driver)
        module_logger.info('@ create proj page')
        cp.cust_num = test_info["cust_num"]
        cp.proj_num = test_info["proj_num"]
        cp.proj_name = test_info["proj_name"]
        cp.proj_des = test_info["proj_des"]
        cp.pg_num = test_info["proj_pg_ct"]
        cp.create_submit()
        module_logger.info('project created')
        # searches for newly created project then selects to update said project
        sp = SearchProject(self.driver)
        time.sleep(5)
        sp.project_search()
        sp.search = test_info["proj_num"]
        sp.proj_search_results()
        UpdateProject(self.driver).update_project()
        ## asserts that the newly created project's data is what was entered above
        module_logger.info('new project found')    
        self.assertEquals(test_info["proj_des"], self.driver.find_element_by_css_selector(locators["cp_proj_des"]).get_attribute("value"))
        module_logger.info('Data is Correct. FE Create Project Test Complete')
        
if __name__ == "__main__":
    import nose
    nose.run(argv=["", "test_fe_create_project", "--verbosity=2"])
        
        