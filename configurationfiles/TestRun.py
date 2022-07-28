import os

# To run the TestRun file
os.system('py.test -rA --disable-pytest-warnings --alluredir=reports/ D:/PracticeFramework/'
          'SeleniumPracticeFramework/test/TestSuite.py')

# To generate the allure reports
#os.system('allure serve D:/PracticeFramework/SeleniumPracticeFramework/reports/SeleniumPracticeAllureReports')
