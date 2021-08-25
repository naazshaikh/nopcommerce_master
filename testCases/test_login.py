import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("******Test_001_Login******")
        self.logger.info("******test_homePageTitle started******")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("******test_homePageTitle passed******")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error("******test_homePageTitle failed******")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("******test_login started******")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("******test_login passed******")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.warn("******test_login failed ******")
            self.driver.close()
            assert False
