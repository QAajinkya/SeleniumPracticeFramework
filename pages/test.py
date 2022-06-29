import time
from base.driverclass import webdriverClass
import utilities.CustomLogger as cl
from base.basefile import BaseClass

wd = webdriverClass()

driver = wd.getWebDriver("Chrome")
bp = BaseClass(driver)

bp.launchWebPage("https://www.saucedemo.com/", "Swag Labs")

ele = bp.isElementDisplayed("user-name", "id")
print(ele)

bp.sendText("standard_user", "user-name", "id")
bp.sendText("secret_sauce", "password", "id")
bp.clickOnElement("login-button", "id")



#Customer_Name = bp.getWebElement("user-name","name")
# Customer_Name = bp.waitForElement("username","name")
# Customer_Name.send_keys("Ajinkya")

time.sleep(2)
driver.quit()