import inspect
#from selenium.webdriver import Chrome, ActionChains
from page.BasePage import *
import time
from locator.LocatorAutomationProjectPage import *
from utils.Util import *
from selenium.webdriver import Chrome
from page.BasePage import BasePage
from page.AutomationProjectPage import HomePage
from locator.LocatorAutomationProjectPage import Locator
from dotenv import load_dotenv
import os
import sys
import time
import inspect
import pytest


load_dotenv()
data=data_from_json('../utils/ddt.json')
# path=os.getenv('PATH')
# data=data_from_json(path)
first_name=os.getenv('FIRST_NAME')
last_name=os.getenv('Last Name')
email=os.getenv('EMAIL')
mobile=os.getenv('MOBILE')
gender_buttons=os.getenv('GENDER_BUTTONS')
buttons=os.getenv('BUTTONS')
set_text=os.getenv('SET_TEXT')

param=os.getenv('PARAM')
is_valid=os.getenv('IS_VALID')
is_not_valid=os.getenv('IS_NOT_VALID')
expected=os.getenv('EXPECTED')
test_pass=os.getenv('TEST_PASS')
test_fail=os.getenv('TEST_FAIL')

tera_santa_title=os.getenv('TERRASANTA')
windy_title=os.getenv('WINDY')
youtube_title=os.getenv('YOUTUBE')

test_name=None



@pytest.fixture
def basepage():
    driver = Chrome()
    return BasePage(driver)


@pytest.fixture
def locator():
    return Locator()

@pytest.fixture
def homepage(basepage):
    driver1 = Chrome()
    return HomePage(basepage.driver)


@pytest.mark.test_get_title
def test_get_title(basepage):
    title = os.getenv('URL_TITLE')
    test_name = str(inspect.currentframe().f_code.co_name)
    #test_get_titel = 'test_get_titel'
    try:

        # assert basepage.get_title() == os.getenv('URL_TITLE')
        # testwriteToFile('pass','test_get_titel')

        assert basepage.get_title() == title
        testwriteToFile(test_name + " " + param + title + " " + ": "+ test_pass,test_name)

    except:
        testwriteToFile(test_name + param + title + " " + ":"+ test_fail,test_name)


@pytest.mark.test_get_fname
def test_get_fname(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            basepage.insert_text(*locator.first_name, text=name[first_name])
            assert homepage.get_text_from_text_box(*locator.first_name) == name[first_name]
            testwriteToFile(f'{test_name} {param} {name[first_name]} {expected} :{name[first_name]} {test_pass}', test_name)
        except:
             testwriteToFile(f'{test_name} {param} {name[first_name]} {expected} :{name[first_name]} {test_fail}',test_name)


@pytest.mark.test_first_name_is_valid
def test_first_name_is_valid(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            basepage.insert_text(*locator.first_name, text=name[first_name])
            #time.sleep(5)
            assert homepage.first_name_is_valid()==True
            #assert automation_project_page.first_name_is_valid()==True
            testwriteToFile(f'{test_name} {param}  {name[first_name]} {is_valid} {test_pass}',test_name)
        except Exception:
            testwriteToFile(f'{test_name} {param}  {name[first_name]} {is_not_valid} {test_fail}',test_name)


@pytest.mark.test_get_lname
def test_get_lname(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            basepage.insert_text(*locator.last_name, text=name[last_name])
            assert homepage.get_text_from_text_box(*locator.last_name) == name[last_name]
            testwriteToFile(f'{test_name} {param} {name[last_name]} {expected} {name[last_name]} {test_pass}',test_name)
        except:
             testwriteToFile(f'{test_name} {param} {name[last_name]} {expected} {name[last_name]} {test_fail}',test_name)


@pytest.mark.test_last_name_is_valid
def test_last_name_is_valid(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            basepage.insert_text(*locator.last_name, text=name[last_name])
            #time.sleep(5)
            assert homepage.last_name_is_valid() == True
            testwriteToFile(f'{test_name} {param} {name[last_name]} {is_valid} {test_pass}',test_name)
        except Exception:
            testwriteToFile(f'{test_name} {param} {name[last_name]} {is_not_valid} {test_fail}',test_name)


@pytest.mark.test_get_email
def test_get_email(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            basepage.insert_text(*locator.email, text=name[email])
            assert homepage.get_text_from_text_box(*locator.email) == name[email]
            testwriteToFile(f'{test_name} {param} {name[email]} {test_pass}',test_name)
        except:
             testwriteToFile(f'{test_name} {param} {name[email]} {test_fail}',test_name)


@pytest.mark.test_email_is_valid
def test_email_is_valid(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            #automation_project_page.insert_text(*locator.email, text=name['Email'])
            basepage.insert_text(*locator.email, text=name[email])
            #time.sleep(5)
            assert homepage.email_is_valid() == True
            testwriteToFile(f'{test_name} {param} {name[email]} {is_valid} {test_pass}',test_name)
        except Exception:
            testwriteToFile(f'{test_name} {param} {name[email]} {is_not_valid} {test_fail}',test_name)


@pytest.mark.test_get_phone
def test_get_phone(basepage,locator):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            basepage.insert_text(*locator.phone, text=name[mobile])
            assert basepage.get_text_from_text_box(*locator.phone) == name[mobile]
            testwriteToFile(f'{test_name} {param} {name[mobile]} {test_pass}',test_name)
        except:
             testwriteToFile(f'{test_name} {param} {name[mobile]} {test_fail}',test_name)


@pytest.mark.test_phone_is_valid
def test_phone_is_valid(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            basepage.insert_text(*locator.phone, text=name[mobile])
            #time.sleep(5)
            assert homepage.phone_number_is_valid() == True
            testwriteToFile(f'{test_name} {param} {name[mobile]} {test_pass}',test_name)
        except Exception:
            testwriteToFile(f'{test_name} {param} {name[mobile]} {test_fail}',test_name)


@pytest.mark.test_one_radio_button_is_selected
def test_one_radio_button_is_selected(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.click_one_radio_button(name[gender_buttons])
            #time.sleep(5)
            assert homepage.one_radio_button_is_selected()==True
            testwriteToFile(f'{test_name} {param} {name[gender_buttons]} {test_pass}',test_name)
        except Exception:
            testwriteToFile(f'{test_name} {param} {name[gender_buttons]} {test_fail}',test_name)


@pytest.mark.test_at_least_one_check_box_is_selected
def test_at_least_one_check_box_is_selected(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.click_one_checkbox(name[buttons])
            #time.sleep(5)
            assert homepage.at_least_one_check_box_is_selected()==True
            testwriteToFile(f'{test_name} {param} {name[buttons]} {test_pass}',test_name)
        except Exception:
            testwriteToFile(f'{test_name} {param} {name[buttons]} {test_fail}',test_name)


@pytest.mark.test_clear_button
def test_clear_button(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        basepage.insert_text(*locator.first_name, text=name[first_name])
        basepage.insert_text(*locator.last_name, text=name[last_name])
        basepage.insert_text(*locator.phone, text=name[mobile])
        basepage.insert_text(*locator.email, text=name[email])
        homepage.click_one_checkbox(name[buttons])
        homepage.click_one_radio_button(name[gender_buttons])
        try:
            assert homepage.check_clear(True)==True
            testwriteToFile(f'{test_name} {param} {name} \n  {test_pass}',test_name)
        except:
             testwriteToFile(f'{test_name} {param} {name} \n {test_fail}',test_name)


@pytest.mark.test_send_button
def test_send_button(basepage,locator,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
                basepage.insert_text(*locator.first_name, text=name[first_name])
                basepage.insert_text(*locator.last_name, text=name[last_name])
                #automation_project_page.insert_text(*locator.phone, text=name[mobile])
                basepage.insert_text(*locator.email, text=name[email])
                #assert automation_project_page.insert_text(*locator.email,text='')
                #automation_project_page.click_one_checkbox(name[buttons])
               # automation_project_page.click_one_radio_button(name[gender_buttons])
                assert basepage.find_element(*locator.send).click() == None
                assert homepage.first_name_is_valid()==True
                assert homepage.last_name_is_valid()==True
                assert homepage.email_is_valid() == True

                testwriteToFile(f'{test_name} {param} first name:{name[first_name]} last name:{name[last_name]} email:{name[email]}',test_name)
        except Exception:
                testwriteToFile(f'test of send button test fail\none ot more of the fields are not valid or missing:\nfirst name:{name[first_name]} last name:{name[last_name]} email:{name[email]}\n',test_name)


@pytest.mark.test_next_page
def test_next_page(basepage,locator,homepage):
        test_name = str(inspect.currentframe().f_code.co_name)
        try:
            homepage.get_title_next_page_after_is_opened()
            #automation_project_page.find_element(*locator.next_page).click()
            assert basepage.get_title() == 'Finish'
            testwriteToFile(f'{test_name} {test_pass}',test_name)
        except:
            testwriteToFile(f'{test_name}  {test_fail}',test_name)


@pytest.mark.test_windy
def test_windy(basepage,locator,homepage):
        test_name = str(inspect.currentframe().f_code.co_name)
        try:
            assert homepage.get_title_windy_after_is_opened() ==windy_title
            #automation_project_page.find_element(*locator.windy).click()
            #assert basepage.get_title() == 'Windy: Wind map & weather forecast'
            testwriteToFile(f'{test_name} {test_pass}',test_name)
        except:
            testwriteToFile(f'{test_name} {test_fail}',test_name)


@pytest.mark.test_tera_santa
def test_tera_santa(basepage,locator,homepage):
        test_name = str(inspect.currentframe().f_code.co_name)
        try:
            assert homepage.get_title_terra_santa_after_is_opened() == tera_santa_title
            #automation_project_page.find_element(*locator.tera_santa).click()
            #assert basepage.get_title() == 'TERRASANTA SEAKAYAK EXPEDITIONS | טרה סנטה קיאקים ימיים – SEAKAYAK EXPEDITIONS'
            testwriteToFile(f'{test_name} {test_pass}',test_name)
        except:
            testwriteToFile(f'{test_name} {test_fail}',test_name)


@pytest.mark.test_java_book
def test_java_book(basepage,locator,homepage):
        test_name = str(inspect.currentframe().f_code.co_name)
        try:
            assert homepage.get_title_java_book_after_is_opened()!= '404 Not Found'
            #automation_project_page.find_element(*locator.java_book).click()
            #assert basepage.get_title() != '404 Not Found'
            testwriteToFile(f'{test_name} {test_pass}',test_name)
        except:
            testwriteToFile(f'{test_name} {test_fail}',test_name)


@pytest.mark.test_youtube
def test_youtube(homepage,locator,basepage):
        test_name = str(inspect.currentframe().f_code.co_name)
        try:
            homepage.get_title_youtube_after_is_opened()
            #automation_project_page.find_element(*locator.youtube).click()
            assert basepage.get_title() == youtube_title
            testwriteToFile(f'{test_name} {test_pass}',test_name)
        except:
            testwriteToFile(f'{test_name} {test_fail}',test_name)


@pytest.mark.test_set_text_from_prompt_alert
def test_set_text_from_prompt_alert(basepage,homepage):
    test_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.set_text_in_prompt_alert(name[set_text])
            assert homepage.check_paragraph_content()== name[set_text]
            testwriteToFile(f'{test_name} {param} {name[set_text]} \n expected result is: {name[set_text]} actual result is: {name[set_text]} {test_pass}',test_name)
        except:
            testwriteToFile(f'{test_name} {param} {name[set_text]} \n expected result is: {name[set_text]} actual result is: {name[set_text]} {test_fail}',test_name)



@pytest.mark.test_get_finish
def test_get_finish(homepage):
    try:
        assert homepage.get_text_after_click_start_loading_button() == "Finish"
        testwriteToFile(f' start loading button has been press expeted Finish to show {test_pass}','test_get_finish')
    except:
        testwriteToFile(f' start loading button has been press expeted Finish to show {test_fail}', 'test_get_finish')

