from selenium import webdriver

from src.helper.configuration_manager import ConfigurationManager


class BasePage:
    def __init__(self, driver: webdriver, configs: ConfigurationManager):
        self.driver = driver
        self.configs = configs
