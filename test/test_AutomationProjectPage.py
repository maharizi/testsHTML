import inspect
import pytest
#from selenium.webdriver import Chrome, ActionChains
from page.BasePage import *
import time
from locator.LocatorAutomationProjectPage import *
from utils.Util import *
from selenium.webdriver import Chrome
from page.BasePage import BasePage
from locator.LocatorAutomationProjectPage import Locator
from dotenv import load_dotenv
import os
import sys
import time
import inspect


load_dotenv()
data=data_from_json()





@pytest.fixture
def automation_project_page():
    driver = Chrome()
    return BasePage(driver)

@pytest.fixture
def locator():
    return Locator()

@pytest.mark.test
def test_get_title(automation_project_page):
    for i in range (20):
        try:
            assert automation_project_page.get_title() == os.getenv('URL_TITLE')
            testwriteToFile('pass','test_get_name')

        except:
            testwriteToFile('fail','test_get_name')



def test_get_fname(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.first_name,text=name['First Name'])
            assert automation_project_page.get_text_from_text_box(*locator.first_name)=='shlomo'
            testwriteToFile(f'input name {name["First Name"]} test pass', 'test_get_name')
        except:
             testwriteToFile(f'input name {name["First Name"]} test fail','test_get_name')

def test_first_name_is_valid(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.first_name, text=name['First Name'])
            #time.sleep(5)
            assert automation_project_page.first_name_is_valid()==True
            testwriteToFile(f' test of valid first name input name {name["First Name"]} test pass', 'first_name_is_valid')
        except:
            testwriteToFile(f' test of valid first name input name {name["First Name"]} test fail', 'first_name_is_valid')




