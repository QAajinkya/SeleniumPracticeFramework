import time
import pytest
from base.basefile import BaseClass
from base.driverclass import WebDriverClass

@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("Chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("http://automationpractice.com/index.php", "My Store")
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
