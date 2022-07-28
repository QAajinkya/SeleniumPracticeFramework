from base.basefile import BaseClass
from utilities import CustomLogger as cl
from utilities.readProperties import ReadConfig


class forgotUserPasswd(BaseClass):
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_Password()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for the home and sign in page
    enter_user_email = "//input[@class='is_required validate account_input form-control']"  # xpath
    back_to_login_btn = "//input[@id='passwd']"  # xpath
    click_retrieve_password = "//button[@id='SubmitLogin']"  # xpath
    success_message = "//p[@class='alert alert-success']"  # xpath

    # Enter email address
    def enter_login_user_email_id(self):
        self.send_text(forgotUserPasswd.user_email, self.enter_user_email, "xpath")
        cl.allureLogs("*******Entered the Email id ************")

    # Enter Password
    def click_back_to_login_button(self):
        self.click_on_element(self.back_to_login_btn, "xpath")
        cl.allureLogs("*******Entered the password ************")

    # Enter Password
    def click_retrieve_password_button(self):
        self.click_on_element(self.click_retrieve_password, "xpath")
        self.is_displayed(self.success_message, "xpath")
        assert True
        self.click_on_element(self.back_to_login_btn, "xpath")
        cl.allureLogs("Verified forgot password")
