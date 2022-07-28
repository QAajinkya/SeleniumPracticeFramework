import time
import utilities.CustomLogger as cl
import unittest
import pytest
from pages.userRegistrationScreen import CreateAccount
from pages.navigateToUserRegistration import createuseraccount


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class CreateAccountTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ca = CreateAccount(self.driver)
        self.sp = createuseraccount(self.driver)

    @pytest.mark.run(order=1)
    def test_HomePage(self):
        self.sp.verify_home_page_loaded()
        time.sleep(3)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.sp.click_on_signin()
        self.sp.verify_login_form_loaded()
        self.sp.enter_email_id()
        self.sp.submit_button_click()

    @pytest.mark.run(order=3)
    def test_userAccountCreate(self):
        print("User Account Creation Started")
        cl.allureLogs("User Account Creation Started")
        self.ca.verify_create_account_page_loaded()
        time.sleep(6)
        self.ca.select_gender_as_male()
        self.ca.enter_first_name()
        self.ca.enter_last_name()
        self.ca.enter_password()
        self.ca.enter_select_date()
        self.ca.enter_select_month()
        self.ca.enter_select_year()
        self.ca.enter_company_name()
        self.ca.enter_address_line1_company()
        self.ca.enter_address_line2_company()
        self.ca.enter_city()
        self.ca.enter_state()
        self.ca.enter_postal_code()
        self.ca.enter_home_phone()
        self.ca.enter_mobile_phone()
        self.ca.enter_alias_address()
        self.ca.click_on_register()
        self.ca.login_page_loaded()

        # CustomerName = "TestingUser QAAutomation"
        # assert True == CustomerName
        # print("Signup user successfull")
