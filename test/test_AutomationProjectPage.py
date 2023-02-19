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
import sys
import time
import inspect
import pytest


load_dotenv()
data=data_from_json('../utils/ddt.json')


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
    """
    This test check title of html page
    :param basepage:
    """
    title = os.getenv('URL_TITLE')
    test_name = str(inspect.currentframe().f_code.co_name)
    #test_get_titel = 'test_get_titel'
    try:

        # assert basepage.get_title() == os.getenv('URL_TITLE')
        # testwriteToFile('pass','test_get_titel')

        assert basepage.get_title() == title
        testwriteToFile(test_name + " " + "run with param: " + title + " " + ": TEST PASS",test_name)

    except:
        testwriteToFile(test_name + "run with param: " + title + " " + ": TEST FAILED",test_name)


@pytest.mark.test_get_fname
def test_get_fname(basepage,locator,homepage):
    """
    This test check first name is written on the text box
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            basepage.insert_text(*locator.first_name, text=name['First Name'])
            assert homepage.get_text_from_text_box(*locator.first_name) == name['First Name']
            testwriteToFile(f'input name {name["First Name"]} test pass', 'test_get_fname')
        except:
             testwriteToFile(f'input name {name["First Name"]} test fail','test_get_fname')


@pytest.mark.test_first_name_is_valid
def test_first_name_is_valid(basepage,locator,homepage):
    """
    This test check first name is valid
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            basepage.insert_text(*locator.first_name, text=name['First Name'])
            #time.sleep(5)
            assert homepage.first_name_is_valid()==True
            #assert automation_project_page.first_name_is_valid()==True
            testwriteToFile(f' test of valid first name input name {name["First Name"]} test pass', 'first_name_is_valid')
        except Exception:
            testwriteToFile(f' test of valid first name input name {name["First Name"]} test fail', 'first_name_is_valid')


@pytest.mark.test_get_lname
def test_get_lname(basepage,locator,homepage):
    """
    This test check last name is written on the text box
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            basepage.insert_text(*locator.last_name, text=name['Last Name'])
            assert homepage.get_text_from_text_box(*locator.last_name) == name['Last Name']
            testwriteToFile(f'input name {name["Last Name"]} test pass', 'test_get_lname')
        except:
             testwriteToFile(f'input name {name["Last Name"]} test fail','test_get_lname')


@pytest.mark.test_last_name_is_valid
def test_last_name_is_valid(basepage,locator,homepage):
    """
    This test check last name is valid
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            basepage.insert_text(*locator.last_name, text=name['Last Name'])
            #time.sleep(5)
            assert homepage.last_name_is_valid() == True
            testwriteToFile(f' test of valid last name input name {name["Last Name"]} test pass', 'last_name_is_valid')
        except Exception:
            testwriteToFile(f' test of valid last name input name {name["Last Name"]} test fail', 'last_name_is_valid')


@pytest.mark.test_get_email
def test_get_email(basepage,locator,homepage):
    """
    This test check email is written on the text box
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            basepage.insert_text(*locator.email, text=name['Email'])
            assert homepage.get_text_from_text_box(*locator.email) == name['Email']
            testwriteToFile(f'input email: {name["Email"]} test pass', 'test_get_email')
        except:
             testwriteToFile(f'input email: {name["Email"]} test fail','test_get_email')


@pytest.mark.test_email_is_valid
def test_email_is_valid(basepage,locator,homepage):
    """
    This test check email is valid
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            #automation_project_page.insert_text(*locator.email, text=name['Email'])
            basepage.insert_text(*locator.email, text=name['Email'])
            #time.sleep(5)
            assert homepage.email_is_valid() == True
            testwriteToFile(f' test of valid email input email: {name["EMAIL"]} test pass', 'email_is_valid')
        except Exception:
            testwriteToFile(f' test of valid email input email: {name["Email"]} test fail', 'email_is_valid')


@pytest.mark.test_get_phone
def test_get_phone(basepage,locator):
    """
    This test check phone is written on the text box
    :param basepage,locator:
    """
    for name in data:
        try:
            basepage.insert_text(*locator.phone, text=name['Mobile'])
            assert basepage.get_text_from_text_box(*locator.phone) == name['Mobile']
            testwriteToFile(f'input name {name["Mobile"]} test pass', 'test_get_phone')
        except:
             testwriteToFile(f'input name {name["Mobile"]} test fail','test_get_phone')


@pytest.mark.test_phone_is_valid
def test_phone_is_valid(basepage,locator,homepage):
    """
    This test check phone is valid
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            basepage.insert_text(*locator.phone, text=name['Mobile'])
            #time.sleep(5)
            assert homepage.phone_number_is_valid() == True
            testwriteToFile(f' test of valid phone input name {name["Mobile"]} test pass', 'phone_is_valid')
        except Exception:
            testwriteToFile(f' test of valid phone input name {name["Mobile"]} test fail', 'phone_is_valid')


@pytest.mark.test_one_radio_button_is_selected
def test_one_radio_button_is_selected(basepage,locator,homepage):
    """
    This test check one radio button is selected
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            homepage.click_one_radio_button(name['GENDER Buttons'])
            #time.sleep(5)
            assert homepage.one_radio_button_is_selected()==True
            testwriteToFile(f' test of radio_button input name {name["GENDER Buttons"]} test pass', 'one_radio_button_is_selected')
        except Exception:
            testwriteToFile(f' test of radio_button input name {name["GENDER Buttons"]} test fail', 'one_radio_button_is_selected')


@pytest.mark.test_at_least_one_check_box_is_selected
def test_at_least_one_check_box_is_selected(basepage,locator,homepage):
    """
    This test check at least one check box is selected
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            homepage.click_one_checkbox(name['Buttons'])
            #time.sleep(5)
            assert homepage.at_least_one_check_box_is_selected()==True
            testwriteToFile(f' test of checkbox input name {name["Buttons"]} test pass', 'at_least_one_check_box_is_selected')
        except Exception:
            testwriteToFile(f' test of checkbox input name {name["Buttons"]} test fail', 'at_least_one_check_box_is_selected')


@pytest.mark.test_clear_button
def test_clear_button(basepage,locator,homepage):
    """
    This test check clear button clear all the information
    :param basepage,locator,homepage:
    """
    for name in data:
        basepage.insert_text(*locator.first_name, text=name['First Name'])
        basepage.insert_text(*locator.last_name, text=name['Last Name'])
        basepage.insert_text(*locator.phone, text=name['Mobile'])
        basepage.insert_text(*locator.email, text=name['Email'])
        homepage.click_one_checkbox(name['Buttons'])
        homepage.click_one_radio_button(name['GENDER Buttons'])
        try:
            assert homepage.check_clear(True)==True
            testwriteToFile(f' input is: {name} \n expected result is True actual result is True test pass', 'test_clear_button')
        except:
             testwriteToFile(f' input is: {name} \n expected result is True actual result is False test fail','test_clear_button')


@pytest.mark.test_send_button
def test_send_button(basepage,locator,homepage):
    """
    This test check all information is valid and send button clicked
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
                basepage.insert_text(*locator.first_name, text=name['First Name'])
                basepage.insert_text(*locator.last_name, text=name['Last Name'])
                #automation_project_page.insert_text(*locator.phone, text=name['Mobile'])
                basepage.insert_text(*locator.email, text=name['Email'])
                #assert automation_project_page.insert_text(*locator.email,text='')
                #automation_project_page.click_one_checkbox(name['Buttons'])
               # automation_project_page.click_one_radio_button(name['GENDER Buttons'])
                assert basepage.find_element(*locator.send).click() == None
                assert homepage.first_name_is_valid()==True
                assert homepage.last_name_is_valid()==True
                assert homepage.email_is_valid() == True

                testwriteToFile(f'test of send button test pass', 'send_button_clicked')
        except Exception:
                testwriteToFile(f'test of send button test fail\none ot more of the fields are not valid or missing:\nfirst name:{name["First Name"]} last name:{name["Last Name"]} email:{name["Email"]}\n', 'send_button_clicked')


@pytest.mark.test_set_text_from_prompt_alert
def test_set_text_from_prompt_alert(basepage,homepage):
    """
    This test check text alert write to paragraph
    :param basepage,locator,homepage:
    """
    for name in data:
        try:
            homepage.set_text_in_prompt_alert(name['Set Text'])
            assert homepage.check_paragraph_content()== name['Set Text']
            testwriteToFile(f' input is: {name["Set Text"]} \n expected result is: {name["Set Text"]} actual result is: {name["Set Text"]} test pass','test_set_text_from_prompt_alert')
        except:
            testwriteToFile(f' input is: {name["Set Text"]} \n expected result is: {name["Set Text"]} actual result is: {name["Set Text"]} test fail','test_set_text_from_prompt_alert')


@pytest.mark.test_get_finish
def test_get_finish(homepage):
    """
    This test check text is change after click of start button to "Finish"
    :param homepage:
    """
    try:
        assert homepage.get_text_after_click_start_loading_button() == "Finish"
        testwriteToFile(f' start loading button has been press expeted Finish to show test pass','test_get_finish')
    except:
        testwriteToFile(f' start loading button has been press expeted Finish to show test fail', 'test_get_finish')


@pytest.mark.test_next_page
def test_next_page(basepage,locator,homepage):
    """
    This test check next page link is opened
    :param basepage,locator,homepage:
    """
    try:
        homepage.get_title_next_page_after_is_opened()
        #automation_project_page.find_element(*locator.next_page).click()
        assert basepage.get_title() == 'Finish'
        testwriteToFile(f' test of next page test pass', 'test_next_page')
    except:
        testwriteToFile(f' test of next page test fail', 'test_next_page')


@pytest.mark.test_next_page
def test_next_page(basepage,locator,homepage):
    """
    This test check next page link is opened
    :param basepage,locator,homepage:
    """
    try:
        homepage.get_title_next_page_after_is_opened()
        #automation_project_page.find_element(*locator.next_page).click()
        assert basepage.get_title() == 'Finish'
        testwriteToFile(f' test of next page test pass', 'test_next_page')
    except:
        testwriteToFile(f' test of next page test fail', 'test_next_page')


@pytest.mark.test_windy
def test_windy(basepage,locator,homepage):
    """
    This test check windy link is opened
    :param basepage,locator,homepage:
    """
    try:
        homepage.get_title_windy_after_is_opened()
        #automation_project_page.find_element(*locator.windy).click()
        assert basepage.get_title() == 'Windy: Wind map & weather forecast'
        testwriteToFile(f' test of Windy test pass', 'test_windy')
    except:
        testwriteToFile(f' test of Windy test fail', 'test_windy')


@pytest.mark.test_tera_santa
def test_tera_santa(basepage,locator,homepage):
    """
    This test check tera santa link is opened
    :param basepage,locator,homepage:
    """
    try:
        homepage.get_title_terra_santa_after_is_opened()
        #automation_project_page.find_element(*locator.tera_santa).click()
        assert basepage.get_title() == 'TERRASANTA SEAKAYAK EXPEDITIONS | טרה סנטה קיאקים ימיים – SEAKAYAK EXPEDITIONS'
        testwriteToFile(f' test of Tera Santa test pass', 'test_tera_santa')
    except:
        testwriteToFile(f' test of Tera Santa test fail', 'test_tera_santa')


@pytest.mark.test_java_book
def test_java_book(basepage,locator,homepage):
    """
    This test check java book link is opened
    :param basepage,locator,homepage:
    """
    try:
        homepage.get_title_java_book_after_is_opened()
        #automation_project_page.find_element(*locator.java_book).click()
        assert basepage.get_title() != '404 Not Found'
        testwriteToFile(f' test of Java Book test pass', 'test_java_book')
    except:
        testwriteToFile(f' test of Java Book test fail', 'test_java_book')


@pytest.mark.test_youtube
def test_youtube(homepage,locator,basepage):
    """
    This test check YouTube link is opened
    :param basepage,locator,homepage:
    """
    try:
        homepage.get_title_youtube_after_is_opened()
        #automation_project_page.find_element(*locator.youtube).click()
        assert basepage.get_title() == 'YouTube'
        testwriteToFile(f' test of YouTube test pass', 'test_youtube')
    except:
        testwriteToFile(f' test of YouTube test fail', 'test_youtube')
