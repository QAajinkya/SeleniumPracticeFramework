from configparser import ConfigParser
import configparser

config = configparser.RawConfigParser()

config.read("D:/PracticeFramework/SeleniumPracticeFramework/configurationfiles/config.ini")

print(config.get("UserCredentials", "baseURL"))
