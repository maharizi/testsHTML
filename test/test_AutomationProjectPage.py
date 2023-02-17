import inspect
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
import pytest


load_dotenv()
data=data_from_json()


@pytest.fixture
def automation_project_page():
    driver = Chrome()
    return BasePage(driver)


@pytest.fixture
def locator():
    return Locator()


@pytest.mark.test_get_title
def test_get_title(automation_project_page):
    try:
        assert automation_project_page.get_title() == os.getenv('URL_TITLE')
        testwriteToFile('pass','test_get_titel')

    except:
        testwriteToFile('fail','test_get_titel')


@pytest.mark.test_get_fname
def test_get_fname(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.first_name,text=name['First Name'])
            assert automation_project_page.get_text_from_text_box(*locator.first_name)==name['First Name']
            testwriteToFile(f'input name {name["First Name"]} test pass', 'test_get_fname')
        except:
             testwriteToFile(f'input name {name["First Name"]} test fail','test_get_fname')


@pytest.mark.test_first_name_is_valid
def test_first_name_is_valid(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.first_name, text=name['First Name'])
            #time.sleep(5)
            assert automation_project_page.first_name_is_valid()==True
            testwriteToFile(f' test of valid first name input name {name["First Name"]} test pass', 'first_name_is_valid')
        except Exception:
            testwriteToFile(f' test of valid first name input name {name["First Name"]} test fail', 'first_name_is_valid')


@pytest.mark.test_get_lname
def test_get_lname(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.last_name,text=name['Last Name'])
            assert automation_project_page.get_text_from_text_box(*locator.last_name)==name['Last Name']
            testwriteToFile(f'input name {name["Last Name"]} test pass', 'test_get_lname')
        except:
             testwriteToFile(f'input name {name["Last Name"]} test fail','test_get_lname')


@pytest.mark.test_last_name_is_valid
def test_last_name_is_valid(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.last_name, text=name['Last Name'])
            #time.sleep(5)
            assert automation_project_page.last_name_is_valid()==True
            testwriteToFile(f' test of valid last name input name {name["Last Name"]} test pass', 'last_name_is_valid')
        except Exception:
            testwriteToFile(f' test of valid last name input name {name["Last Name"]} test fail', 'last_name_is_valid')


@pytest.mark.test_get_email
def test_get_email(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.email,text=name['Email'])
            assert automation_project_page.get_text_from_text_box(*locator.email)==name['Email']
            testwriteToFile(f'input name {name["Email"]} test pass', 'test_get_email')
        except:
             testwriteToFile(f'input name {name["Email"]} test fail','test_get_email')


@pytest.mark.test_email_is_valid
def test_email_is_valid(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.email, text=name['Email'])
            #time.sleep(5)
            assert automation_project_page.email_is_valid()==True
            testwriteToFile(f' test of valid email input name {name["EMAIL"]} test pass', 'email_is_valid')
        except Exception:
            testwriteToFile(f' test of valid email input name {name["Email"]} test fail', 'email_is_valid')


@pytest.mark.test_get_phone
def test_get_phone(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.phone,text=name['Mobile'])
            assert automation_project_page.get_text_from_text_box(*locator.phone)==name['Mobile']
            testwriteToFile(f'input name {name["Mobile"]} test pass', 'test_get_phone')
        except:
             testwriteToFile(f'input name {name["Mobile"]} test fail','test_get_phone')


@pytest.mark.test_phone_is_valid
def test_phone_is_valid(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.insert_text(*locator.phone, text=name['Mobile'])
            #time.sleep(5)
            assert automation_project_page.phone_number_is_valid()==True
            testwriteToFile(f' test of valid phone input name {name["Mobile"]} test pass', 'phone_is_valid')
        except Exception:
            testwriteToFile(f' test of valid phone input name {name["Mobile"]} test fail', 'phone_is_valid')


@pytest.mark.test_one_radio_button_is_selected
def test_one_radio_button_is_selected(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.click_one_radio_button(name['GENDER Buttons'])
            #time.sleep(5)
            assert automation_project_page.one_radio_button_is_selected()==True
            testwriteToFile(f' test of radio_button input name {name["GENDER Buttons"]} test pass', 'one_radio_button_is_selected')
        except Exception:
            testwriteToFile(f' test of radio_button input name {name["GENDER Buttons"]} test fail', 'one_radio_button_is_selected')


@pytest.mark.test_at_least_one_check_box_is_selected
def test_at_least_one_check_box_is_selected(automation_project_page,locator):
    for name in data:
        try:
            automation_project_page.click_one_checkbox(name['Buttons'])
            #time.sleep(5)
            assert automation_project_page.at_least_one_check_box_is_selected()==True
            testwriteToFile(f' test of checkbox input name {name["Buttons"]} test pass', 'at_least_one_check_box_is_selected')
        except Exception:
            testwriteToFile(f' test of checkbox input name {name["Buttons"]} test fail', 'at_least_one_check_box_is_selected')

@pytest.mark.test_clear_button
def test_clear_button(automation_project_page,locator):
    for name in data:
        automation_project_page.insert_text(*locator.first_name, text=name['First Name'])
        automation_project_page.insert_text(*locator.last_name, text=name['Last Name'])
        automation_project_page.insert_text(*locator.phone, text=name['Mobile'])
        automation_project_page.insert_text(*locator.email, text=name['Email'])
        automation_project_page.click_one_checkbox(name['Buttons'])
        automation_project_page.click_one_radio_button(name['GENDER Buttons'])
        try:
            assert automation_project_page.check_clear(True)==True
            testwriteToFile(f' input is: {name} \n expected result is True actual result is True test pass', 'test_clear_button')
        except:
             testwriteToFile(f' input is: {name} \n expected result is True actual result is False test fail','test_clear_button')