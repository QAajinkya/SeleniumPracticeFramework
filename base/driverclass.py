from selenium import webdriver


class webdriverClass:

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "Chrome":
            driver = webdriver.Chrome("C:/Users/ajinkyas.shukla_info/Desktop/Selenium/drivers/chromedriver.exe")
        elif browserName == "Safari":
            driver = webdriver.Safari()
        elif browserName == "Firefox":
            driver = webdriver.Firefox(
                executable_path="C:/Users/ajinkyas.shukla_info/Desktop/Selenium/drivers/geckodriver.exe")

        return driver
