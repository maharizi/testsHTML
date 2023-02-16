#<<<<<<< HEAD
import inspect
import pytest
#from selenium.webdriver import Chrome, ActionChains
from page.BasePage import *
import time
#=======
from selenium.webdriver import Chrome
from page.BasePage import BasePage
#>>>>>>> 58d1f89f46691788496a5c5fafc0a0625de9c2e0
from locator.LocatorAutomationProjectPage import Locator
from dotenv import load_dotenv

import os
import sys
import time
import inspect
import pytest


#<<<<<<< HEAD
url_title=os.getenv('Automation Project')
#driver = Chrome()
#base=BasePage(driver)

#class AutoTest():
@pytest.fixture()
def base():
      #driver1 = Chrome()
      return BasePage()

def test_gete(base):
   # print(base.base_url)
    #assert base.get_title()=='affa'
    assert base.printa()==5


#=======
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
#>>>>>>> 58d1f89f46691788496a5c5fafc0a0625de9c2e0




