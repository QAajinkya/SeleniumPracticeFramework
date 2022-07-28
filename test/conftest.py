import configparser
import time
import pytest
from base.basefile import BaseClass
from base.driverclass import WebDriverClass

config = configparser.RawConfigParser()
config.read("D:/PracticeFramework/SeleniumPracticeFramework/configurationfiles/config.ini")


@pytest.fixture(scope='class')
def beforeClass(request):
    test_url = config.get('UserCredentials', 'baseURL')
    title = config.get('UserCredentials', 'Title')
    print('Before Class')
    print('Start Browser')
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("Chrome")
    bp = BaseClass(driver)
    bp.launchWebPage(test_url, title)
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
