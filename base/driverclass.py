from selenium import webdriver
import utilities.CustomLogger as cl


class webdriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "Chrome":
            driver = webdriver.Chrome("C:/Users/ajinkyas.shukla_info/Desktop/Selenium/drivers/chromedriver.exe")
            self.log.info("Chrome browser is initialised")
        elif browserName == "Safari":
            driver = webdriver.Safari()
            self.log.info("Safari browser is initialised")
        elif browserName == "Firefox":
            driver = webdriver.Firefox(
                executable_path="C:/Users/ajinkyas.shukla_info/Desktop/Selenium/drivers/geckodriver.exe")
            self.log.info("Firefox browser is initialised")

        return driver
