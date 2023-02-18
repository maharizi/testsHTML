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


@pytest.mark.test_send_button
def test_send_button(automation_project_page,locator):
        try:
            for name in data:
                automation_project_page.insert_text(*locator.first_name, text=name['First Name'])
                automation_project_page.insert_text(*locator.last_name, text=name['Last Name'])
                automation_project_page.insert_text(*locator.phone, text=name['Mobile'])
                automation_project_page.insert_text(*locator.email, text=name['Email'])
                automation_project_page.click_one_checkbox(name['Buttons'])
                automation_project_page.click_one_radio_button(name['GENDER Buttons'])
                assert automation_project_page.find_element(*locator.send).click() == None
                testwriteToFile(f' test of send button test pass', 'send_button_clicked')
        except Exception:
            testwriteToFile(f' test of send button test fail', 'send_button_clicked')


@pytest.mark.test_next_page
def test_next_page(automation_project_page,locator):
        try:
            automation_project_page.get_title_next_page_after_is_opened()
            #automation_project_page.find_element(*locator.next_page).click()
            assert automation_project_page.get_title() == 'Finish'
            testwriteToFile(f' test of next page test pass', 'test_next_page')
        except:
            testwriteToFile(f' test of next page test fail', 'test_next_page')


@pytest.mark.test_windy
def test_windy(automation_project_page,locator):
        try:
            automation_project_page.get_title_windy_after_is_opened()
            #automation_project_page.find_element(*locator.windy).click()
            assert automation_project_page.get_title() == 'Windy: Wind map & weather forecast'
            testwriteToFile(f' test of Windy test pass', 'test_windy')
        except:
            testwriteToFile(f' test of Windy test fail', 'test_windy')


@pytest.mark.test_tera_santa
def test_tera_santa(automation_project_page,locator):
        try:
            automation_project_page.get_title_terra_santa_after_is_opened()
            #automation_project_page.find_element(*locator.tera_santa).click()
            assert automation_project_page.get_title() == 'TERRASANTA SEAKAYAK EXPEDITIONS | טרה סנטה קיאקים ימיים – SEAKAYAK EXPEDITIONS'
            testwriteToFile(f' test of Tera Santa test pass', 'test_tera_santa')
        except:
            testwriteToFile(f' test of Tera Santa test fail', 'test_tera_santa')


@pytest.mark.test_java_book
def test_java_book(automation_project_page,locator):
        try:
            automation_project_page.get_title_java_book_after_is_opened()
            #automation_project_page.find_element(*locator.java_book).click()
            assert automation_project_page.get_title() != '404 Not Found'
            testwriteToFile(f' test of Java Book test pass', 'test_java_book')
        except:
            testwriteToFile(f' test of Java Book test fail', 'test_java_book')


@pytest.mark.test_youtube
def test_youtube(automation_project_page,locator):
        try:
            automation_project_page.get_title_youtube_after_is_opened()
            #automation_project_page.find_element(*locator.youtube).click()
            assert automation_project_page.get_title() == 'YouTube'
            testwriteToFile(f' test of YouTube test pass', 'test_youtube')
        except:
            testwriteToFile(f' test of YouTube test fail', 'test_youtube')


@pytest.mark.test_set_text_from_prompt_alert
def test_set_text_from_prompt_alert(automation_project_page):
    for name in data:
        try:
            assert automation_project_page.set_text_from_prompt_alert(name['Set Text'])
            assert automation_project_page.check_paragraph_content()==name['Set Text']
            testwriteToFile(f' input is: {name["Set Text"]} \n expected result is: {name["Set Text"]} actual result is: {name["Set Text"]} test pass','test_set_text_from_prompt_alert')
        except:
            testwriteToFile(f' input is: {name["Set Text"]} \n expected result is: {name["Set Text"]} actual result is: {name["Set Text"]} test fail','test_set_text_from_prompt_alert')



@pytest.mark.test_get_finish
def test_get_finish(automation_project_page):
    try:
        assert automation_project_page.get_text_after_click_start_loading_button()=="Finish"
        testwriteToFile(f' start loading button has been press expeted Finish to show test pass','test_get_finish')
    except:
        testwriteToFile(f' start loading button has been press expeted Finish to show test fail', 'test_get_finish')

