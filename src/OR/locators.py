'''
Created on May 4, 2014

@author: citizenchris099
'''
locators = {}
# SBv3
# log in page
locators["login_username"] = "*[name^='usern']"
locators["login_password"] = "*[name^='passw']"
locators["login.submit"] = "//*[@id='b4enfold_login_form']/form/p[3]"
locators["logged_out"] = "//*[@id='b4enfold_login_form']/p"

# user menu 
locators["logo"]="//*[@id='logo']/img"
locators["umb"]="//*[@id='navigation']"

# user menu buttons
# admin dashboard
locators["admin_db"]="//*[@id='menu-item-27']/a"
## user admin
locators["user_admin"]="//*[@id='menu-item-28']/a"
## project admin
locators["proj_admin"]="//*[@id='menu-item-29']/a"

### project admin page
locators["pa_create_proj"]="//*[@id='createProjectButton']"
locators["pa_update_proj"]="//*[@id='updateProjectButton']"
locators["pa_search"]="//*[@id='b4enfold_project_admin_view']/div[1]/span"
locators["pa_search_field"]="//*[@id='projectSearch']"
locators["pa_search_results"]="//*[@id='b4enfold_proj_grid']/div[5]/div/div[1]/div[1]"


#### create project page
locators["cp_cust_num"]="*[name$='proj_custnum']"
locators["cp_proj_num"]="*[name$='proj_number']"
locators["cp_proj_name"]="*[name$='proj_name']"
locators["cp_proj_des"]="*[name$='proj_desc']"
locators["cp_num_pages"]="*[name$='proj_numpages']"
locators["cp_submit"]="//*[@id='submitButton']"

#### update project page
locators["up_cust_num"]="*[name$='custnum']"
locators["up_proj_num"]="*[name$='number']"
locators["up_proj_name"]="*[name$='name']"
locators["up_proj_des"]="*[name$='proj_desc']"
locators["up_num_pages"]="*[name$='proj_numpages']"
locators["up_submit"]="//*[@id='submitButton']"

## site admin
locators["site_admin"]="//*[@id='menu-item-43']/a"

### site admin page  aka WP dashboard
locators["users"]="//*[@id='menu-users']/a/div[3]"
locators["wp_db_logo"]="//*[@id='wpbody-content']/div[3]/h2"

### WP UMB
locators["wp_umb"]="//*[@id='wp-admin-bar-site-name']/a"

#### WP BE user page
locators["addnewuser"]="//*[@id='wpbody-content']/div[3]/h2/a"
locators["searchfield"]="//*[@id='user-search-input']"
locators["searchbutton"]="//*[@id='search-submit']"
locators["bulkactions"]="//*[@id='wpbody-content']/div[4]/form/div[1]/div[1]/select"
locators["applybulkactions"]="//*[@id='doaction']"
locators["chrolepd"]="//*[@id='new_role']"
locators["chroleb"]="//*[@id='changeit']"
locators["userckbox"]="*[name^='users']"
locators["namecolumn"]="//*[@id='user-1']/td[2]"
locators["rolecolumn"]="//*[@id='user-5']/td[4]"
locators["usersearchresult"]="*[id^='user-']"
locators["deleted_message"]="//*[@id='message']/p"

##### WP BE create user page
locators["nu_uname"]="//*[@id='user_login']"
locators["nu_email"]="//*[@id='email']"
locators["nu_pword"]="//*[@id='pass1']"
locators["nu_rep_pword"]="//*[@id='pass2']"
locators["nu_role_adviser"]="//select[@id='role']/option[@value='e_adviser']"
locators["nu_project"]="html/body/div[1]/div[3]/div[2]/div[1]/div[3]/form/div/table/tbody/tr[1]/td/div/a"
locators["nu_project_input"]="html/body/div[1]/div[3]/div[2]/div[1]/div[3]/form/div/table/tbody/tr[1]/td/div/div/div/input"
locators["nu_project_choice"]="html/body/div[1]/div[3]/div[2]/div[1]/div[3]/form/div/table/tbody/tr[1]/td/div/div/ul/li"
locators["nu_anu"]="//*[@id='createusersub']"

# dashboard
locators["dashboard_button"]="//*[@id='menu-item-30']/a"

### main Dashboard
locators["log_out_button"]="//*[@id='logoutButton']"
locators["db_project"]="html/body/div[1]/div/section/article/section/div[2]/form/p[1]/div/a/span"
locators["db_project_search"]="html/body/div[1]/div/section/article/section/div[2]/form/p[1]/div/div/div/input"
locators["db_project_results"]="html/body/div[1]/div/section/article/section/div[2]/form/p[1]/div/div/ul/li"

## user manager
locators["user_man"]="//*[@id='menu-item-31']/a"

### user manager page
locators["um_create_user"]="//*[@href='https://studio3-qa.balfour.com/dashboard/usermanager/?act=createUserForm']"
locators["um_search"]="//*[@id='b4enfold_user_admin_view']/div[1]/span"
locators["um_search_field"]="//*[@id='lastnameSearch']"
locators["um_search_results"]="//*[@id='b4enfold_user_grid']/div[5]/div/div/div[2]"
locators["um_exs_user"]="//*[@id='users_chosen']/a"
locators["um_exs_user_search"]="//*[@id='users_chosen']/div/div/input"
locators["um_exs_user_choice"]="//*[@id='users_chosen']/div/ul/li"


#### user manager create user page
locators["um_uname"]="*[name$='username']"
locators["um_fname"]="*[name$='first_name']"
locators["um_lname"]="*[name$='last_name']"
locators["um_email"]="*[name$='email']"
locators["um_pword"]="*[name$='password']"
locators["um_con_pword"]="*[name$='confirm_password']"
locators["um_tel"]="*[name$='phone']"
locators["um_role"]="*[name$='role']"
locators["um_role_adviser"]="//select[@name='role']/option[@value='e_adviser']"
locators["um_submit"]="*[name$='submit']"

## project
locators["project"]="//*[@id='menu-item-32']/a"
## profile
locators["profile"]="//*[@id='menu-item-33']/a"

### profile page
locators["prof_first"]="//*[@id='input_4_1_3']"
locators["prof_last"]="//*[@id='input_4_1_6']"
locators["prof_email"]="//*[@id='input_4_2']"
locators["prof_phone"]="//*[@id='input_4_4']"
locators["prof_cur_pword"]="//*[@id='input_4_5']"
locators["prof_pword"]="//*[@id='input_4_3']"
locators["prof_con_pword"]="//*[@id='input_4_3_2']"
locators["prof_submit"]="//*[@id='gform_submit_button_4']"
locators["required"]="gfield_error" #class
locators["there_was_a_problem"]="validation_error" #class
locators["strength"]="//*[@id='input_4_3_strength']"


locators["check_user_info"]="//*[@id='menu-item-53']/a"

# balfour tools
locators["balfour_tools"]="//*[@id='menu-item-42']/a"

## BT_FAQ
locators["BT_FAQ"]="//*[@id='menu-item-98']/a"

# my year
locators["my_year"]="//*[@id='menu-item-54']/a"

# contact
locators["contact"]="//*[@id='menu-item-57']/a"

#SBv1
# log in page
locators["sbv1_project"]="//*[@id='_58_project']"
locators["sbv1_uname"]="//*[@id='_58_login']"
locators["sbv1_pword"]="//*[@id='_58_password']"
locators["sbv1_login_submit"]="//*[@id='_58_signIn']"

# Dashboard / Main Page
locators["sb_logo"]="//*[@id='branding']/img"
locators["pop_link_my"]="//*[@id='softwareLink']/a"
locators["balfour_wesites"]="//*[@id='social-footer']/div[1]/div[2]/a"

# My Year
locators["MY_logo"]="/html/body/div[3]/div[2]/header/a/img"
locators["user_menu"]="//*[@id='user_id']"
locators["back_2_sb"]="/html/body/div[3]/div[2]/header/nav[2]/ul/li/ul/li[4]/a"
