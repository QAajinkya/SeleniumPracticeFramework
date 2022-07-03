import time

import utilities.CustomLogger as cl
import unittest
import pytest
from base.basefile import BaseClass
from pages.LoginFile import loginFile


@pytest.mark.usefixtures("beforeClass","beforeMethod")
class SignInTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.sp = loginFile(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_HomePage(self):
        self.sp.verifyHomePageLoaded()
        time.sleep(3)
        self.sp.clickOnSignin()
        self.sp.verifyLoginFormloaded()

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.sp.clickOnSignin()
        self.sp.verifyLoginFormloaded()
        self.sp.enterEmailId()
        self.sp.submitButtonClick()
