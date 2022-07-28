from base.basefile import BaseClass
from utilities import CustomLogger as cl
from utilities.readProperties import ReadConfig


class loginUserFile(BaseClass):
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_Password()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for the home and sign in page
    user_name_login = "//input[@id='email']"  # xpath
    user_passwd_login = "//input[@id='passwd']"  # xpath
    click_signin_button = "//button[@id='SubmitLogin']"  # xpath
    sign_out_button = "//a[@class='logout']"


    # Enter email address
    def enter_login_user_email_id(self):
        self.send_text(loginUserFile.user_email, self.user_name_login, "xpath")
        cl.allureLogs("*******Entered the Email id ************")

    # Enter Password
    def enter_login_user_password_id(self):
        self.send_text(loginUserFile.password, self.user_passwd_login, "xpath")
        cl.allureLogs("*******Entered the password ************")

    # Enter Password
    def click_sign_in(self):
        self.click_on_element(self.click_signin_button, "xpath")
        self.click_on_element(self.sign_out_button, "xpath")
        cl.allureLogs("*******Clicked on SignIon************")
