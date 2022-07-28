import configparser
from base.basefile import BaseClass
from utilities import CustomLogger as cl
from utilities.readProperties import ReadConfig

config = configparser.RawConfigParser()
config.read("D:/PracticeFramework/SeleniumPracticeFramework/configurationfiles/config.ini")


class CreateAccount(BaseClass):
    user_details = ReadConfig.get_user_details()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators of Personal Information
    create_account_page_disp = "account-creation_form"  # id
    select_gender_male = "//input[@id='id_gender1']"  # xpath
    select_gender_female = "//input[@id='id_gender2']"  # xpath
    enter_firstname = "//input[@id='customer_firstname']"  # xpath
    enter_lastname = "//input[@id='customer_lastname']"  # xpath
    enter_email_id = "//a[@title='Log in to your customer account']"  # xpath
    enter_password_user = "//input[@id='passwd'] "  # xpath
    enter_date = "//select[@id='days']"  # xpath
    enter_month = "//select[@id='months']"  # xpath
    enter_year = "//select[@id='years']"  # xpath

    # Locators of Address
    firstname_address = "//input[@name='firstname']"  # xpath
    lastname_address = "//input[@id='lastname']"  # xpath
    company_name = "//input[@id='company']"  # xpath
    address = "address1"  # name
    address_line_two = "address2"  # name
    city = "city"  # id
    state = "//select[@id='id_state']"  # xpath
    postal_code = "postcode"  # id
    country = "United States"
    home_phone = "//input[@id='phone']"  # xpath
    mobile_phone = "//input[@id='phone_mobile']"  # xpath
    assign_Address_alias = "//input[@id='alias']"  # xpath
    click_Register = "//button[@id='submitAccount']"  # xpath

    # login page loaded
    login_page_verify = "//a[@title='View my customer account']"
    sign_out_button = "//a[@class='logout']"

    # Verified Create an Account Form is loaded
    def verify_create_account_page_loaded(self):
        element = self.is_displayed(self.create_account_page_disp, "id")
        assert element == True
        cl.allureLogs("********Verified as Home Page is loaded and displayed******")

    # Enter the data in the form
    # select the Gender as Male
    def select_gender_as_male(self):
        self.click_on_element(self.select_gender_male, "xpath")
        cl.allureLogs("********Verified as Home Page is loaded and displayed******")

    # select the Gender as Female
    def select_gender_as_female(self):
        self.click_on_element(self.select_gender_female, "xpath")
        cl.allureLogs("********** Selected the Gender as Female ***************")

    # Enter the user data
    def enter_first_name(self):
        print(config.get('UserDetails', 'FirstName'))
        self.send_text(config.get('UserDetails', 'FirstName'), self.enter_firstname, "xpath")

    def enter_last_name(self):
        self.send_text(config.get('UserDetails', 'LastName'), self.enter_lastname, "xpath")

    def enter_password(self):
        self.send_text(config.get("UserCredentials", "password"), self.enter_password_user, "xpath")

    def enter_select_date(self):
        self.get_Option_by_Text_Index(config.get("UserDetails", "DateOfBirth"), self.enter_date, "xpath")

    def enter_select_month(self):
        self.get_Option_by_Text_value("April ", self.enter_month, "xpath")

    def enter_select_year(self):
        self.get_Option_by_Text_value("1991  ", self.enter_year, "xpath")

    def enter_address_first_name(self):
        self.send_text(config.get('UserDetails', 'FirstName'), self.firstname_address, "xpath")

    def enter_address_last_name(self):
        self.send_text(config.get('UserDetails', 'LastName'), self.lastname_address, "xpath")

    def enter_company_name(self):
        self.send_text(config.get('UserAddress', 'Company'), self.company_name, "xpath")

    def enter_address_line1_company(self):
        self.send_text(config.get('UserAddress', 'AddressLine1'), self.address, "name")

    def enter_address_line2_company(self):
        self.send_text(config.get('UserAddress', 'AddressLine2'), self.address_line_two, "name")

    def enter_city(self):
        self.send_text(config.get('UserAddress', 'City'), self.city, "id")

    def enter_state(self):
        self.get_Option_by_Text_value(config.get("UserAddress", "State"), self.state, "xpath")

    def enter_postal_code(self):
        self.send_text(config.get("UserAddress", "PostalCode"), self.postal_code, "id")

    def enter_home_phone(self):
        self.send_text(config.get("UserAddress", "HomePhone"), self.home_phone, "xpath")

    def enter_mobile_phone(self):
        self.send_text(config.get("UserAddress", "MobilePhone"), self.mobile_phone, "xpath")

    def enter_alias_address(self):
        self.send_text(config.get("UserAddress", "AliasAddress"), self.assign_Address_alias, "xpath")

    def click_on_register(self):
        self.click_on_element(self.click_Register, "xpath")

    def login_page_loaded(self):
        self.is_displayed(self.login_page_verify, "xpath")
        self.click_on_element(self.sign_out_button, "xpath")
