from selenium.webdriver import Chrome
from page.BasePage import BasePage
from locator.LocatorAutomationProjectPage import Locator
from dotenv import load_dotenv

import os
import sys
import time
import inspect
import pytest


# url_title=os.getenv('Automation Project')
# driver = Chrome()
# base=BasePage(driver)


@pytest.fixture
def automation_project_page():
    driver = Chrome()
    return BasePage(driver)


@pytest.mark.test
def test_get_title(automation_project_page):
    assert automation_project_page.get_title() == "Automation Project"


# def test_gete():
#    # print(base.base_url)
#     assert base.get_title()=='affa'




