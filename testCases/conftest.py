from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\NaazA\PycharmProjects\nopcommerce\Browser\chromedriver.exe")
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path="C:\\Users\\NaazA\\PycharmProjects\\nopcommerce\\Browser"
                                                "\\msedgedriver.exe")
    else:
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\NaazA\PycharmProjects\nopcommerce\Browser\chromedriver.exe")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##############pytest HTML Reports ##############

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['tester'] = 'Naaz'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
