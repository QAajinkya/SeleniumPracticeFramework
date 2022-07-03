from base.basefile import BaseClass
from utilities import CustomLogger as cl

class loginFile(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for the home and sign in page
    _homepageNumber = "shop-phone"  # class
    _clickonSignin = "//a[@title='Log in to your customer account']" #xpath
    _signinPageDis = "login_form"  # id
    _enteremailid = "email_create"  # id
    _clicksubmitbutton = "SubmitCreate"  # name

    def verifyHomePageLoaded(self):
        element = self.isElementDisplayed(self._homepageNumber, "class")
        assert element == True
        cl.allureLogs(" Verified as Home Page element is displayed")

    def clickOnSignin(self):
        self.clickOnElement(self._clickonSignin, "xpath")
        cl.allureLogs("Clicked on the Signin button on the Homepage")

    def verifyLoginFormloaded(self):
        formDisp = self.isElementDisplayed(self._signinPageDis, "id")
        assert formDisp == True
        cl.allureLogs("Verified form is loaded and displayed")

    def enterEmailId(self):
        self.sendText("abcmagic@gmail.com", self._enteremailid, "id")
        cl.allureLogs("Entered the Email id specified above")

    def submitButtonClick(self):
        self.clickOnElement(self._clicksubmitbutton, "name")
        cl.allureLogs("Clicked on the Submit button")
