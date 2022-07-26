from base.basefile import BaseClass
from utilities import CustomLogger as cl


class loginFile(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for the home and sign in page
    _homepageNumber = "shop-phone"  # class
    _clickonSignin = "//a[@title='Log in to your customer account']"  # xpath
    _signinPageDis = "login_form"  # id
    _enteremailid = "email_create"  # id
    _clickCreateAccountbutton = "//button[@id='SubmitCreate']"  # xpath

    # Verified Home page is loaded on loading the URL

    def verify_home_page_loaded(self):
        element = self.is_displayed(self._homepageNumber, "class")
        assert element == True
        cl.allureLogs("****Verified as Home Page is loaded and displayed*********")

    # Click on Sign in
    def click_on_signin(self):
        self.clickOnElement(self._clickonSignin, "xpath")
        cl.allureLogs("*****Clicked on the Signin button on the Homepage*****")

    # Verify the Create an account page is loaded
    def verify_login_form_loaded(self):
        formDisp = self.is_displayed(self._signinPageDis, "id")
        assert formDisp == True
        cl.allureLogs("******Create account form is loaded and displayed******")

    # Enter email address
    def enter_email_id(self):
        self.send_text("abcmagic@gmail.com", self._enteremailid, "id")
        cl.allureLogs("*******Entered the Email id specified above************")

    # Click on "Create an account"
    def submit_button_click(self):
        self.clickOnElement(self._clickCreateAccountbutton, "xpath")
        cl.allureLogs("*******Clicked on the Create an Account button*********")
