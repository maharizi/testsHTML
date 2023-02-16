import os
import pytest as pytest
from selenium import webdriver

from locator.LocatorAutomationProjectPage import Locator
from page.BasePage import BasePage

driver = webdriver.Chrome()
locator_automation_project = Locator()
url_title=os.getenv('Automation Project')


@pytest.fixture
def base_page():
    """
    This function init pytest
    and return instance of BasePage
    :return instance of BasePage:
    """
    return BasePage(driver)


@pytest.mark.test_first_test
def test_first_name(base_page):
    assert base_page.first_name_is_valid() == True
