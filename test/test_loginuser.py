import time
import utilities.CustomLogger as cl
import unittest
import pytest

from pages.login_user import loginUserFile
from pages.userRegistrationScreen import CreateAccount
from pages.navigateToUserRegistration import createuseraccount


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class loginTestUser(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ca = CreateAccount(self.driver)
        self.sp = createuseraccount(self.driver)
        self.lf = loginUserFile(self.driver)


    @pytest.mark.run(order=1)
    def test_HomePage(self):
        self.sp.verify_home_page_loaded()
        time.sleep(3)

    @pytest.mark.run(order=2)
    def test_login_with_user(self):
        cl.allureLogs("Automation started")
        self.sp.click_on_signin()
        self.sp.verify_login_form_loaded()
        self.lf.enter_login_user_email_id()
        self.lf.enter_login_user_password_id()
        self.lf.click_sign_in()
