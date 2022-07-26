from base.basefile import BaseClass
from utilities import CustomLogger as cl


class CreateAccount(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators of Personal Information
    _createAccountPageDisp = "account-creation_form"  # id
    _selectGenderMale = "//input[@id='id_gender1']"  # xpath
    _selectGenderFemale = "//input[@id='id_gender2']"  # xpath
    _enterFirstName = "//input[@id='customer_firstname']"  # xpath
    _enterLastName = "//input[@id='customer_lastname']"  # xpath
    _enterEmailId = "//a[@title='Log in to your customer account']"  # xpath
    _enterPassword = "//input[@id='passwd'] "  # xpath
    _enterDate = "//select[@id='days']"  # xpath
    _enterMonth = "//select[@id='months']"  # xpath
    _enterYear = "//select[@id='years']"  # xpath

    # Locators of Address
    _firstNameAddress = "//input[@name='firstname']"  # xpath
    _lastNameAddress = "//input[@id='lastname']"  # xpath
    _companyName = "//input[@id='company']"  # xpath
    _address = "address1"  # name
    _addressLineTwo = "address2"  # name
    _city = "city"  # id
    _state = "//select[@id='id_state']"  # xpath
    _postalCode = "postcode"  # id
    _country = "United States"
    _homePhone = "//input[@id='phone']"  # xpath
    _mobilePhone = "//input[@id='phone_mobile']"  # xpath
    _assignAddressAlias = "//input[@id='alias']"  # xpath
    _clickRegister = "//button[@id='submitAccount']"  # xpath

    # Verified Create an Account Form is loaded
    def verify_create_account_page_loaded(self):
        element = self.is_displayed(self._createAccountPageDisp, "id")
        assert element == True
        cl.allureLogs("********Verified as Home Page is loaded and displayed******")

    # Enter the data in the form
    # select the Gender as Male
    def select_gender_as_male(self):
        self.clickOnElement(self._selectGenderMale, "xpath")
        cl.allureLogs("********Verified as Home Page is loaded and displayed******")

    # select the Gender as Female
    def select_gender_as_female(self):
        self.clickOnElement(self._selectGenderFemale, "xpath")
        cl.allureLogs("********** Selected the Gender as Female ***************")

    # Enter the user data
    def enter_first_name(self):
        self.send_text("TestingUser", self._enterFirstName, "xpath")

    def enter_last_name(self):
        self.send_text("QAAutomation", self._enterLastName, "xpath")

    def enter_password(self):
        self.send_text("12345678", self._enterPassword, "xpath")

    def enter_select_date(self):
        self.get_Option_by_Text_Index(4, self._enterDate, "xpath")

    def enter_select_month(self):
        self.get_Option_by_Text_value('April ', self._enterMonth, "xpath")

    def enter_select_year(self):
        self.get_Option_by_Text_value('2021  ', self._enterYear, "xpath")

    def enter_address_first_name(self):
        self.send_text('TestingUser', self._firstNameAddress, "xpath")

    def enter_address_last_name(self):
        self.send_text('QAAutomation', self._lastNameAddress, "xpath")

    def enter_company_name(self):
        self.send_text('Fresher.inc', self._companyName, "xpath")

    def enter_address_line1_company(self):
        self.send_text('QAAutomation', self._address, "name")

    def enter_address_line2_company(self):
        self.send_text('QAAutomation', self._addressLineTwo, "name")

    def enter_city(self):
        self.send_text('QAAutomation', self._city, "id")

    def enter_state(self):
        self.get_Option_by_Text_value('Kentucky', self._state, "xpath")

    def enter_postal_code(self):
        self.send_text('653-A53', self._postalCode, "id")

    def enter_home_phone(self):
        self.send_text('0731-453242', self._homePhone, "xpath")

    def enter_mobile_phone(self):
        self.send_text('6347565464', self._mobilePhone, "xpath")

    def enter_alias_address(self):
        self.send_text('Home', self._assignAddressAlias, "xpath")

    def click_on_register(self):
        self.clickOnElement(self._clickRegister, "xpath")
