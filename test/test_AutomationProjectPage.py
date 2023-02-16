from selenium.webdriver import Chrome
from page.BasePage import BasePage
from locator.LocatorAutomationProjectPage import Locator
from dotenv import load_dotenv

import os
import sys
import time
import inspect
import pytest


@pytest.fixture
def automation_project_page():
    driver = Chrome()
    return BasePage(driver)


@pytest.mark.test
def test_get_title(automation_project_page):
    assert automation_project_page.get_title() == "Automation Project"


# @pytest.mark.test_first_test
# def test_first_name(base_page):
#     assert base_page.first_name_is_valid() == True
