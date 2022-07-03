# 1. Import the files
import unittest
from test.test_signInPage import SignInTest
#from SeleniumFrameWork.tests.test_EnterTextTest import EnterTextTest


# 2. Create the object of the class using unitTest
si = unittest.TestLoader().loadTestsFromTestCase(SignInTest)
#et = unittest.TestLoader().loadTestsFromTestCase(EnterTextTest)


# 3. Create TestSuite
regressionTest = unittest.TestSuite([si])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

# Note : All the methods in test files should define in proper run order