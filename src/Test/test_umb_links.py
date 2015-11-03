'''
Created on May 4, 2014

@author: citizenchris099
'''
import unittest
from OR.base import selenium_driver
from OR.login import LoginPageObject
from OR.umb import User_Menu_Bar
from OR.umb_siteadmin_wpumb import WpUmb
from OR.test_info import test_info
from OR.umb_db import DashBoard
import logging

module_logger = logging.getLogger('testlogger')

# tests all of the links accessible from the FE UMB by clicking each of them and asserting the page loaded  
class TestUmbLinks(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.driver.implicitly_wait(10)
        self.base_url = selenium_driver.base_url
 
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    
    def test_umb_links(self):
        # logs in
        module_logger.info('Started User Menu Bar Test')
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.username = test_info["login_username"]
        lpo.password = test_info["login_pword"]
        lpo.submit()
        module_logger.info('logged in')
        # proceeds to click the links all of the links
        dash = User_Menu_Bar(self.driver)
        dash.admin_db()
        module_logger.info('@ admin db')
        dash.user_admin()
        module_logger.info('@ user admin')
        dash.proj_admin()
        module_logger.info('@ project admin')
        dash.site_admin()
        module_logger.info('@ site admin')
        wpumb = WpUmb(self.driver)
        wpumb.go_2_FE()
        module_logger.info('@ FE DB')
        dash.dashboard_button()
        dash.user_manager()
        module_logger.info('@ user manager')
        dash.project()
        module_logger.info('@ project')
        dash.profile()
        module_logger.info('@ profile')
        dash.check_user_info()
        module_logger.info('@ check user info')
        dash.balfour_tools()
        module_logger.info('@  bt')
        dash.bt_faq()
        module_logger.info('@  bt faq')
        dash.my_year()
        module_logger.info('@  my year')
        dash.contact()
        module_logger.info('@ contact')
        dash.dashboard_button()
        module_logger.info('@ FE DB')
        DashBoard(self.driver).log_out()
        module_logger.info('logged out')
        module_logger.info('User Menu Bar Test Complete')
        
if __name__ == "__main__":
    import nose
    nose.run(argv=["", "test_umb_links", "--verbosity=2"])