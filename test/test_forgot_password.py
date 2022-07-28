import time
import utilities.CustomLogger as cl
import unittest
import pytest

from pages.login_user import loginUserFile
from pages.forgot_password import forgotUserPasswd


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class loginTestUser(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lf = loginUserFile(self.driver)
        self.fp = forgotUserPasswd(self.driver)

    @pytest.mark.run(order=1)
    def test_verify_forgot_password(self):
        self.fp.enter_login_user_email_id()
        self.fp.click_retrieve_password_button()

