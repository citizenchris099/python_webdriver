'''
Created on May 13, 2014

@author: cmanning
'''
import unittest
from OR.base import selenium_driver
from OR.login import LoginPageObject
from OR.umb import User_Menu_Bar
from OR.umb_profile import UpdateProfile
from OR.test_info import test_info
from OR.locators import locators
import time
from OR.base.check_is_displayed import check_is_displayed
from OR.umb_db import DashBoard
import logging

module_logger = logging.getLogger('testlogger')

# tests updating user profile on the front. additionally tests behavior of site under differing input scenarios 
class TestFeUpdateProfile(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.driver = selenium_driver.connect()
        self.base_url = selenium_driver.base_url
        self.log_in()     
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
    def test_prof_update_change_pword(self):
        module_logger.info('Started FE Update Profile / Change Password Test')
        up = UpdateProfile(self.driver)
        #changes password / logs out
        self.info_entry(up)
        self.password_entry(up)
        up.update_profile_submit()
        module_logger.info('profile updated')
        self.log_out()
        # logs in w/new password
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.username = test_info["login_username"]
        lpo.password = test_info["new_pword_strong"]
        lpo.submit()
        User_Menu_Bar(self.driver).profile()
        module_logger.info('logged in w/new password')
        # changes password back to original / verifies user can log back in using original password
        self.info_entry(up)
        up.current_pword = test_info["new_pword_strong"]
        up.new_pword = test_info["login_pword"]
        up.con_pword = test_info["login_pword"]
        up.update_profile_submit()
        self.log_out()
        self.log_in()
        module_logger.info('password set back to original. Change Password Test Complete ')
        
    def test_wrong_phone_format (self):
        # enters a bad phone format / asserts that error displays
        module_logger.info('Started FE Update Profile / Wrong Phone Format Test')
        up = UpdateProfile(self.driver)
        up.first_name = test_info["first_name"]
        up.last_name = test_info["last_name"]
        up.email = test_info["email"]
        up.phone = "8675309"
        self.password_entry(up)
        up.update_profile_submit()
        module_logger.info('new data entered')
        self.assertTrue(check_is_displayed(locators["required"]), "It wasn't true :(")
        module_logger.info('error message detected. Wrong Phone Format Test Complete')
        
    def test_no_name (self):
        # fills out form but omits name entry
        module_logger.info('Started FE Update Profile / No First Name Test')
        up = UpdateProfile(self.driver)
        up.first_name = ""
        up.last_name = test_info["new_last_name"]
        up.email = test_info["new_email"]
        up.phone = test_info["new_phone"]
        self.password_entry(up)
        up.update_profile_submit()
        module_logger.info('new data entered')
        self.assertTrue(check_is_displayed(locators["required"]), "It wasn't true :(")
        module_logger.info('error message detected. No First Name Test Complete')
        
    def test_no_cur_pword (self):
        # fills out form but omits name entry
        module_logger.info('Started FE Update Profile / No Current Password Test')
        up = UpdateProfile(self.driver)
        self.new_data_entry(up)
        up.update_profile_submit()
        module_logger.info('new data entered')
        self.assertTrue(check_is_displayed(locators["required"]), "It wasn't true :(")
        module_logger.info('error message detected. No Current Password Test Complete')
        
    def test_wrong_cur_pword (self):
        # fills out form but omits name entry
        module_logger.info('Started FE Update Profile / Wrong Current Password Test')
        up = UpdateProfile(self.driver)
        self.new_data_entry(up)
        up.current_pword = "meatisevill"
        up.update_profile_submit()
        module_logger.info('new data entered')
        self.assertTrue(check_is_displayed(locators["required"]), "It wasn't true :(")
        module_logger.info('error message detected. Wrong Current Password Test Complete')
        
    def test_short_pword (self):
        # fills out form but omits name entry
        module_logger.info('Started FE Update Profile / Short Password Test')
        up = UpdateProfile(self.driver)
        self.new_data_entry(up)
        up.current_pword = test_info["login_pword"]
        up.new_pword = test_info["new_pword_short"]
        up.update_profile_submit()
        module_logger.info('new data entered')
        self.assertEquals("short", self.driver.find_element_by_xpath(locators["strength"]).get_attribute("value"))
        module_logger.info('correct strength message. Short Password Test Complete')
        
    def test_mismatch_pword (self):
        # fills out form but omits name entry
        module_logger.info('Started FE Update Profile / Mismatch Password Test')
        up = UpdateProfile(self.driver)
        self.new_data_entry(up)
        up.current_pword = test_info["login_pword"]
        up.new_pword = test_info["new_pword_short"]
        up.con_pword = test_info["login_pword"]
        up.update_profile_submit()
        module_logger.info('new data entered')
        self.assertEquals("mismatch", self.driver.find_element_by_xpath(locators["strength"]).get_attribute("value"))
        module_logger.info('correct strength message. Mismatch Password Test Complete')
        
    def test_bad_pword (self):
        # fills out form but omits name entry
        module_logger.info('Started FE Update Profile / Bad Password Test')
        up = UpdateProfile(self.driver)
        self.new_data_entry(up)
        up.current_pword = test_info["login_pword"]
        up.new_pword = test_info["new_pword_bad"]
        up.update_profile_submit()
        module_logger.info('new data entered')
        self.assertEquals("bad", self.driver.find_element_by_xpath(locators["strength"]).get_attribute("value"))
        module_logger.info('correct strength message. Bad Password Test Complete')
        
    def test_good_pword (self):
        # fills out form but omits name entry
        module_logger.info('Started FE Update Profile / Good Password Test')
        up = UpdateProfile(self.driver)
        self.new_data_entry(up)
        up.current_pword = test_info["login_pword"]
        up.new_pword = test_info["new_pword_good"]
        up.update_profile_submit()
        module_logger.info('new data entered')
        self.assertEquals("good", self.driver.find_element_by_xpath(locators["strength"]).get_attribute("value"))
        module_logger.info('correct strength message. Good Password Test Complete')
        
    def test_strong_pword (self):
        # fills out form but omits name entry
        module_logger.info('Started FE Update Profile / Strong Password Test')
        up = UpdateProfile(self.driver)
        self.new_data_entry(up)
        up.current_pword = test_info["login_pword"]
        up.new_pword = test_info["new_pword_strong"]
        up.update_profile_submit()
        module_logger.info('new data entered')
        self.assertEquals("strong", self.driver.find_element_by_xpath(locators["strength"]).get_attribute("value"))
        module_logger.info('correct strength message. Strong Password Test Complete')
       
    def test_update_info (self):
        # verifies name, email, phone info retention. 
        module_logger.info('Started FE Update Profile / Update Info Test')
        up = UpdateProfile(self.driver)
        self.new_data_entry(up)
        up.current_pword = "meatisevil"
        up.update_profile_submit()
        module_logger.info('new data submitted')
        self.log_out()
        self.log_in()
        self.assertEquals("Vegan", self.driver.find_element_by_xpath(locators["prof_first"]).get_attribute("value"))
        self.assertEquals("Smurfins", self.driver.find_element_by_xpath(locators["prof_last"]).get_attribute("value"))
        self.assertEquals("fake@balfour.com", self.driver.find_element_by_xpath(locators["prof_email"]).get_attribute("value"))
        self.assertEquals("(817)867-5309", self.driver.find_element_by_xpath(locators["prof_phone"]).get_attribute("value"))
        module_logger.info('new data is correct')
        #resets the info back to original state
        self.info_entry(up)
        up.current_pword = "meatisevil"
        up.update_profile_submit()
        module_logger.info('Info reset. Info Update Test Complete')
        
    def log_in(self):
        lpo = LoginPageObject(self.driver, self.base_url)
        lpo.do_login(test_info["login_username"], test_info["login_pword"])
        module_logger.info('logged in')
        User_Menu_Bar(self.driver).profile()
        module_logger.info('@ FE Profile page')

    def log_out(self):
        time.sleep(10)
        self.assertEqual("Admin Dashboard | Studio Balfour", self.driver.title)
        User_Menu_Bar(self.driver).dashboard_button()
        DashBoard(self.driver).log_out()
        module_logger.info('logged out')

    def info_entry(self, up):
        up.first_name = test_info["first_name"]
        up.last_name = test_info["last_name"]
        up.email = test_info["email"]
        up.phone = test_info["phone"]

    def password_entry(self, up):
        up.current_pword = test_info["login_pword"]
        up.new_pword = test_info["new_pword_strong"]
        up.con_pword = test_info["new_pword_strong"]

    def new_data_entry(self, up):
        up.first_name = test_info["new_first_name"]
        up.last_name = test_info["new_last_name"]
        up.email = test_info["new_email"]
        up.phone = test_info["new_phone"]

        
if __name__ == "__main__":
    import nose
    nose.run(argv=["", "test_fe_update_profile", "--verbosity=2"])