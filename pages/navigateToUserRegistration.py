from base.basefile import BaseClass
from utilities import CustomLogger as cl
from utilities.readProperties import ReadConfig


class createuseraccount(BaseClass):
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_Password()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for the home and sign in page
    homepage_Number = "shop-phone"  # class
    clickon_signin = "//a[@title='Log in to your customer account']"  # xpath
    signin_page_dis = "login_form"  # id
    enteremailid = "email_create"  # id
    click_create_accountbutton = "//button[@id='SubmitCreate']"  # xpath

    # Verified Home page is loaded on loading the URL

    def verify_home_page_loaded(self):
        element = self.is_displayed(self.homepage_Number, "class")
        assert element == True
        cl.allureLogs("****Verified as Home Page is loaded and displayed*********")

    # Click on Sign in
    def click_on_signin(self):
        self.click_on_element(self.clickon_signin, "xpath")
        cl.allureLogs("*****Clicked on the Signin button on the Homepage*****")

    # Verify the Create an account page is loaded
    def verify_login_form_loaded(self):
        formDisp = self.is_displayed(self.signin_page_dis, "id")
        assert formDisp == True
        cl.allureLogs("******Create account form is loaded and displayed******")

    # Enter email address
    def enter_email_id(self):
        self.send_text(createuseraccount.user_email, self.enteremailid, "id")
        cl.allureLogs("*******Entered the Email id specified above************")

    # Click on "Create an account"
    def submit_button_click(self):
        self.click_on_element(self.click_create_accountbutton, "xpath")
        cl.allureLogs("*******Clicked on the Create an Account button*********")
