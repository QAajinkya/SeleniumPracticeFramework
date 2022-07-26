from selenium import webdriver
import utilities.CustomLogger as cl
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "Chrome":
<<<<<<< HEAD
            driver = webdriver.Chrome(ChromeDriverManager().install())
=======
            driver = webdriver.Chrome("C:/Users/ajin/Desktop/Selenium/drivers/chromedriver.exe")
>>>>>>> 62405b59513be86d0ad1e5e07a36ff3cc20d13dc
            self.log.info("Chrome browser is initialised")
        elif browserName == "Safari":
            driver = webdriver.Safari()
            self.log.info("Safari browser is initialised")
        elif browserName == "Firefox":
<<<<<<< HEAD
            driver = webdriver.Firefox(GeckoDriverManager.install())
=======
            driver = webdriver.Firefox(
                executable_path="C:/Users/ajin/Desktop/Selenium/drivers/geckodriver.exe")
>>>>>>> 62405b59513be86d0ad1e5e07a36ff3cc20d13dc
            self.log.info("Firefox browser is initialised")

        return driver
