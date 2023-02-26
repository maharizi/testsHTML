from utils.Util import *
from selenium.webdriver import Chrome
from page.AutomationProjectPage import HomePage
from locator.LocatorAutomationProjectPage import Locator
from dotenv import load_dotenv
import inspect
import pytest

load_dotenv()
data = data_from_json('../utils/ddt.json')

first_name = os.getenv('FIRST_NAME')
last_name = os.getenv('LAST_NAME')
email = os.getenv('EMAIL')
mobile = os.getenv('MOBILE')
gender_buttons = os.getenv('GENDER_BUTTONS')
buttons = os.getenv('BUTTONS')
set_text = os.getenv('SET_TEXT')

param = os.getenv('PARAM')
is_valid = os.getenv('IS_VALID')
is_not_valid = os.getenv('IS_NOT_VALID')
expected = os.getenv('EXPECTED')
test_pass = os.getenv('TEST_PASS')
test_fail = os.getenv('TEST_FAIL')

tera_santa_title = os.getenv('TERRASANTA')
windy_title = os.getenv('WINDY')
youtube_title = os.getenv('YOUTUBE')


test_name = os.getenv("TEST")
driver = Chrome()


@pytest.fixture
def locator():
    return Locator()


@pytest.fixture
def homepage():
    return HomePage(driver)

@pytest.mark.test_get_title
def test_get_title(homepage):
    """
    This test check title of html page
    :param homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    title = os.getenv('URL_TITLE')
    try:
        assert homepage.get_title() == title
        testwriteToFile(test_func_name + " " + param + title + " " + ": " + test_pass, test_name)
    except:
        homepage.screenshot(test_name=test_name)
        testwriteToFile(test_func_name + " " + param + title + " " + ":" + test_fail, test_name)


@pytest.mark.test_get_fname
def test_get_fname(locator, homepage):
    """
    This test check first name is written on the text box
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.insert_text(*locator.first_name, text=name[first_name])
            assert homepage.get_text_from_text_box(*locator.first_name) == name[first_name]
            testwriteToFile(f'{test_func_name} {param} {name[first_name]} {expected} :{name[first_name]} {test_pass}',
                            test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[first_name]} {expected} :{name[first_name]} {test_fail}',
                            test_name)


@pytest.mark.test_first_name_is_valid
def test_first_name_is_valid(locator, homepage):
    """
    This test check first name is valid
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.insert_text(*locator.first_name, text=name[first_name])
            assert homepage.first_name_is_valid() == True
            testwriteToFile(f'{test_func_name} {param}  {name[first_name]} {is_valid} {test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param}  {name[first_name]} {is_not_valid} {test_fail}', test_name)


@pytest.mark.test_get_lname
def test_get_lname(locator, homepage):
    """
    This test check last name is written on the text box
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.insert_text(*locator.last_name, text=name[last_name])
            assert homepage.get_text_from_text_box(*locator.last_name) == name[last_name]
            testwriteToFile(f'{test_func_name} {param} {name[last_name]} {expected} {name[last_name]} {test_pass}',
                            test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[last_name]} {expected} {name[last_name]} {test_fail}',
                            test_name)


@pytest.mark.test_last_name_is_valid
def test_last_name_is_valid(locator, homepage):
    """
    This test check last name is valid
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.insert_text(*locator.last_name, text=name[last_name])
            assert homepage.last_name_is_valid() == True
            testwriteToFile(f'{test_func_name} {param} {name[last_name]} {is_valid} {test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[last_name]} {is_not_valid} {test_fail}', test_name)


@pytest.mark.test_get_email
def test_get_email(locator, homepage):
    """
    This test check email is written on the text box
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.insert_text(*locator.email, text=name[email])
            assert homepage.get_text_from_text_box(*locator.email) == name[email]
            testwriteToFile(f'{test_func_name} {param} {name[email]} {test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[email]} {test_fail}', test_name)


@pytest.mark.test_email_is_valid
def test_email_is_valid(locator, homepage):
    """
    This test check email is valid
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.insert_text(*locator.email, text=name[email])
            assert homepage.email_is_valid() == True
            testwriteToFile(f'{test_func_name} {param} {name[email]} {is_valid} {test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[email]} {is_not_valid} {test_fail}', test_name)


@pytest.mark.test_get_phone
def test_get_phone(homepage, locator):
    """
    This test check phone is written on the text box
    :param homepage,locator:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.insert_text(*locator.phone, text=name[mobile])
            assert homepage.get_text_from_text_box(*locator.phone) == name[mobile]
            testwriteToFile(f'{test_func_name} {param} {name[mobile]} {test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[mobile]} {test_fail}', test_name)


@pytest.mark.test_phone_is_valid
def test_phone_is_valid(locator, homepage):
    """
    This test check phone is valid
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.insert_text(*locator.phone, text=name[mobile])
            assert homepage.phone_number_is_valid() == True
            testwriteToFile(f'{test_func_name} {param} {name[mobile]} {is_valid} {test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[mobile]} {is_not_valid} {test_fail}', test_name)


@pytest.mark.test_one_radio_button_is_selected
def test_one_radio_button_is_selected(locator, homepage):
    """
    This test check one radio button is selected
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.click_one_radio_button(name[gender_buttons])
            assert homepage.one_radio_button_is_selected() == True
            testwriteToFile(f'{test_func_name} {param} {name[gender_buttons]} {test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[gender_buttons]} {test_fail}', test_name)


@pytest.mark.test_at_least_one_check_box_is_selected
def test_at_least_one_check_box_is_selected(locator, homepage):
    """
    This test check at least one check box is selected
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.click_one_checkbox(name[buttons])
            assert homepage.at_least_one_check_box_is_selected() == True
            testwriteToFile(f'{test_func_name} {param} {name[buttons]} {test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[buttons]} {test_fail}', test_name)


@pytest.mark.test_clear_button
def test_clear_button(locator, homepage):
    """
    This test check clear button clear all the information
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        homepage.insert_text(*locator.first_name, text=name[first_name])
        homepage.insert_text(*locator.last_name, text=name[last_name])
        homepage.insert_text(*locator.phone, text=name[mobile])
        homepage.insert_text(*locator.email, text=name[email])
        homepage.click_one_checkbox(name[buttons])
        homepage.click_one_radio_button(name[gender_buttons])
        try:
            assert homepage.check_clear(True) == True
            testwriteToFile(f'{test_func_name} {param}\n{name}\n{test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param}\n{name}\n{test_fail}', test_name)


@pytest.mark.test_send_button
def test_send_button(locator, homepage):
    """
    This test check all information is valid and send button clicked
    :param locator,homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.insert_text(*locator.first_name, text=name[first_name])
            homepage.insert_text(*locator.last_name, text=name[last_name])
            homepage.insert_text(*locator.email, text=name[email])
            assert homepage.find_element(*locator.send).click() is None
            assert homepage.first_name_is_valid() == True
            assert homepage.last_name_is_valid() == True
            assert homepage.email_is_valid() == True
            testwriteToFile(
                f'{test_func_name} {param} first name:{name[first_name]} last name:{name[last_name]} email:{name[email]} {test_pass}',
                test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(
                f'{test_func_name} {param} first name:{name[first_name]} last name:{name[last_name]} email:{name[email]} {test_fail}\n',
                test_name)


@pytest.mark.test_next_page
def test_next_page(locator, homepage):
    """
        This test check next page link is opened
        :param locator,homepage:
        """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    try:
        homepage.get_title_next_page_after_is_opened()
        assert homepage.get_title() == 'Finish'
        testwriteToFile(f'{test_func_name} {test_pass}', test_name)
    except:
        homepage.screenshot(test_name=test_name)
        testwriteToFile(f'{test_func_name}  {test_fail}', test_name)


@pytest.mark.test_windy
def test_windy(locator, homepage):
    """
        This test check windy link is opened
        :param locator,homepage:
        """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    try:
        assert homepage.get_title_windy_after_is_opened() == windy_title
        testwriteToFile(f'{test_func_name} {test_pass}', test_name)
    except:
        homepage.screenshot(test_name=test_name)
        testwriteToFile(f'{test_func_name} {test_fail}', test_name)


@pytest.mark.test_tera_santa
def test_tera_santa(locator, homepage):
    """
        This test check tera santa link is opened
        :param locator,homepage:
        """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    try:
        assert homepage.get_title_terra_santa_after_is_opened() == tera_santa_title
        testwriteToFile(f'{test_func_name} {test_pass}', test_name)
    except:
        homepage.screenshot(test_name=test_name)
        testwriteToFile(f'{test_func_name} {test_fail}', test_name)


@pytest.mark.test_java_book
def test_java_book(locator, homepage):
    """
        This test check java book link is opened
        :param locator,homepage:
        """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    try:
        assert homepage.get_title_java_book_after_is_opened() != '404 Not Found'
        testwriteToFile(f'{test_func_name} {test_pass}', test_name)
    except:
        homepage.screenshot(test_name=test_name)
        testwriteToFile(f'{test_func_name} {test_fail}', test_name)


@pytest.mark.test_youtube
def test_youtube(homepage, locator):
    """
        This test check YouTube link is opened
        :param locator,homepage:
        """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    try:
        homepage.get_title_youtube_after_is_opened()
        assert homepage.get_title() == youtube_title
        testwriteToFile(f'{test_func_name} {test_pass}', test_name)
    except:
        homepage.screenshot(test_name=test_name)
        testwriteToFile(f'{test_func_name} {test_fail}', test_name)


@pytest.mark.test_set_text_from_prompt_alert
def test_set_text_from_prompt_alert(homepage):
    """
    This test check text alert write to paragraph
    :param homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    for name in data:
        try:
            homepage.set_text_in_prompt_alert(name[set_text])
            assert homepage.check_paragraph_content() == name[set_text]
            testwriteToFile(f'{test_func_name} {param} {name[set_text]} \n expected result is: {name[set_text]} actual '
                            f'result is: {name[set_text]} {test_pass}', test_name)
        except:
            homepage.screenshot(test_name=test_name)
            testwriteToFile(f'{test_func_name} {param} {name[set_text]} \n expected result is: {name[set_text]} actual '
                            f'result is: {name[set_text]} {test_fail}', test_name)


@pytest.mark.test_get_finish
def test_get_finish(homepage):
    """
    This test check text is change after click of start button to "Finish"
    :param homepage:
    """
    test_func_name = str(inspect.currentframe().f_code.co_name)
    try:
        assert homepage.get_text_after_click_start_loading_button() == "Finish"
        testwriteToFile(f'{test_func_name} start loading button has been press expeted Finish to show {test_pass}',test_name)
    except:
        homepage.screenshot(test_name=test_name)
        testwriteToFile(f'{test_func_name} start loading button has been press expeted Finish to show {test_fail}', test_name)






