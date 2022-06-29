import time
from base.driverclass import webdriverClass
import utilities.CustomLogger as cl
from base.basefile import BaseClass

wd = webdriverClass()

driver = wd.getWebDriver("Chrome")
bp = BaseClass(driver)

bp.launchWebPage("https://parabank.parasoft.com/parabank/register.htm", "ParaBank | Register for Free Online Account Access")

Customer_Name = bp.getWebElement("username","name")
# Customer_Name.click()
Customer_Name.send_keys("Ajinkya")


time.sleep(2)
driver.quit()