from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=r"C:\Users\NaazA\PycharmProjects\nopcommerce\Browser\chromedriver.exe")
    return driver
