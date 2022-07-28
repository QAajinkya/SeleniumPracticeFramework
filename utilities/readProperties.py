import configparser

config = configparser.RawConfigParser()
config.read("D:/PracticeFramework/SeleniumPracticeFramework/configurationfiles/config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get("UserCredentials", "baseURL")
        title = config.get("User Credentials", "Title")

        # Now creating the list for calling url and title
        web_url_data = [url, title]

        return web_url_data

    @staticmethod
    def get_user_email():
        username = config.get("UserCredentials", "username")
        return username

    @staticmethod
    def get_user_Password():
        password = config.get("UserCredentials", "password")
        return password

    @staticmethod
    def get_user_details():
        # user details"
        firstname = config.get("UserDetails", "FirstName")
        return firstname

    #     lastname = config.get("UserDetails", "LastName")
    #     birthdate = config.get("UserDetails", "DateOfBirth")
    #     birthmonth = config.get("UserDetails", "BirthMonth")
    #     birthyear = config.get("UserDetails", "BirthYear")
    #
    #     # User Address details
    #     company = config.get("UserAddress", "Company")
    #     Addressline1 = config.get("UserAddress", "AddressLine1")
    #     Addressline2 = config.get("UserAddress", "AddressLine2")
    #     city = config.get("UserAddress", "City")
    #     country = config.get("UserAddress", "Country")
    #     state = config.get("UserAddress", "State")
    #     postalcode = config.get("UserAddress", "PostalCode")
    #     homephone = config.get("UserAddress", "HomePhone")
    #     mobilephone = config.get("UserAddress", "MobilePhone")
    #     aliasaddress = config.get("UserAddress", "AliasAddress")
    #
    #
    #
    # # Now creating the list for all the above parameters
    #     user_details = [firstname, lastname, birthdate, birthmonth, birthyear, company,state, Addressline1,Addressline2,
    #                     city, country, homephone, mobilephone, postalcode, aliasaddress]
    #
    #     return user_details



