# 1. Import the files
import unittest
from test.CreateAccounttest import CreateAccountTest

# from SeleniumFrameWork.tests.test_EnterTextTest import EnterTextTest


# 2. Create the object of the class using unitTest
ct = unittest.TestLoader().loadTestsFromTestCase(CreateAccountTest)


# 3. Create TestSuite
# = unittest.TestSuite([ct])
sanityTest = unittest.TestSuite([ct])
# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(sanityTest)

# Note : All the methods in test files should define in proper run order
