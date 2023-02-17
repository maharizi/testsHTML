from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from locator.LocatorAutomationProjectPage import Locator as A_Locator
from locator.LocatorNextPagePage import Locator as N_Locator
import re


class BasePage(object):
    def __init__(self, driver, url="file:///C:/AutomationProject.html"):
        """
        Constructor to this class,
        this function get webdriver and url
        :param driver:
        :param url:
        """
        self.base_url = url
        self.driver = driver
        self.driver.get(self.base_url)

    def find_element(self, *locator):
        """
        This function get location of element
        and return object of this element
        :param locator:
        :return element:
        """
        return self.driver.find_element(*locator)

    def get_title(self):
        """
        This function return the title
        of the current page
        :return title:
        """
        return self.driver.title

    def get_url(self):
        """
        This function return the url
        of the current page
        :return url:
        """
        return self.base_url

    def insert_text(self,*locator,  text):
        """
        This function get location of text box
        and put in the parameter text
        :param locator:
        :param text:
        """
        text_box = self.find_element(*locator)
        text_box.clear()
        text_box.send_keys(text)

    def click_button(self, *locator):
        """
        This function get location
        of button and click it
        :param locator:
        :return:
        """
        button = self.driver.find_element(*locator)
        button.click()

    def get_text_from_text_box(self, *locator):
        """
        This function get location of text box
        and return the current value
        :param locator:
        :return value:
        """
        text_box = self.find_element(*locator)
        return text_box.get_attribute('value')

    def first_name_is_valid(self):
        """
        This function check if the
        first name is valid by regex
        :return bool:
        """
        first_name = self.get_text_from_text_box(*A_Locator.first_name)
        if re.match("[a-zA-Z]{1,15}$", first_name):
            return True
        else:
            return False

    def last_name_is_valid(self):
        """
        This function check if the
        last name is valid by regex
        :return bool:
        """
        last_name = self.get_text_from_text_box(*A_Locator.last_name)
        if re.match("[a-zA-Z]{1,15}$", last_name):
            return True
        else:
            return False

    def email_is_valid(self):
        """
        This function check if the
        email is valid by regex
        :return bool:
        """
        email = self.get_text_from_text_box(*A_Locator.email)
        if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
            return True
        else:
            return False

    def phone_number_is_valid(self):
        """
        This function click femail radio button
        :return bool:
        """
        phone_number = self.get_text_from_text_box(*A_Locator.phone)
        if re.match(r'[0-9]{7}$', phone_number):
            return True
        else:
            return False

    def click_one_radio_button(self, option):
        """
        This function click
        radio-button
        :return null:
        """
        match option:
            case 'Other':
                self.driver.find_element(*A_Locator.other).click()
            case 'Male':
                self.driver.find_element(*A_Locator.male).click()
            case 'Female':
                self.driver.find_element(*A_Locator.female).click()

    def one_radio_button_is_selected(self):
        """
        This function check if at least one
        radio-button is selected
        :return bool:
        """
        if self.find_element(*A_Locator.female).is_selected():
            return True
        if self.find_element(*A_Locator.male).is_selected():
            return True
        if self.find_element(*A_Locator.other).is_selected():
            return True
        return False

    def click_one_checkbox(self, options):
        """
        This function click
        checkbox
        :return null:
        """
        for option in options:
            match option:
                case 'Math':
                    self.driver.find_element(*A_Locator.math).click()
                case 'Physics':
                    self.driver.find_element(*A_Locator.physics).click()
                case 'POP':
                    self.driver.find_element(*A_Locator.pop).click()
                case 'DUD':
                    self.driver.find_element(*A_Locator.dud).click()
                case 'Biology':
                    self.driver.find_element(*A_Locator.biology).click()
                case 'Chemistry':
                    self.driver.find_element(*A_Locator.chemistry).click()
                case 'English':
                    self.driver.find_element(*A_Locator.english).click()

    def at_least_one_check_box_is_selected(self):
        """
        This function check if at least one checkbox
        is selected
        :return bool:
        """
        if self.find_element(*A_Locator.math).is_selected():
            return True
        if self.find_element(*A_Locator.biology).is_selected():
            return True
        if self.find_element(*A_Locator.physics).is_selected():
            return True
        if self.find_element(*A_Locator.pop).is_selected():
            return True
        if self.find_element(*A_Locator.dud).is_selected():
            return True
        if self.find_element(*A_Locator.english).is_selected():
            return True
        if self.find_element(*A_Locator.chemistry).is_selected():
            return True
        return False

    def check_clear(self, click_clear=False):
        """
        This function check if all the fields
        were cleared after click clear button manually or automatically
        default is False
        :param click_clear:
        :return bool:
        """
        if not click_clear:
            self.click_button(*A_Locator.clear)
        if self.get_text_from_text_box(*A_Locator.first_name):
            return False
        if self.get_text_from_text_box(*A_Locator.last_name):
            return False
        if self.get_text_from_text_box(*A_Locator.email):
            return False
        if self.get_text_from_text_box(*A_Locator.phone):
            return False
        if not self.at_least_one_check_box_is_selected():
            return False
        if not self.one_radio_button_is_selected():
            return False
        return True

    def check_paragraph_content(self):
        """
        This function return the text
        from the paragraph content
        :return str:
        """
        paragraph = self.find_element(*A_Locator.paragraph_set_text)
        return paragraph.Text()

    def get_text_after_click_start_loading_button(self):
        """
        This function return the text which was changed
        after we click the button and wait some time
        if the text was not changed, this function return None
        :return str:
        """
        self.click_button(*A_Locator.button_start_loading)
        element_text = WebDriverWait(self.driver, 10)
        element_text.until(ec.text_to_be_present_in_element(*A_Locator.paragraph_start_loading, "Finish"))
        if element_text:
            return self.driver.find_element(*A_Locator.paragraph_start_loading).text
        else:
            return None

    def get_title_next_page_after_is_opened(self):
        """
        This function return the title of the "next page"
        after we click the button which move to "next page"
        if the element from the "next page" is presented so
        the page is loaded
        :return:
        """
        self.click_button(*N_Locator.next_page)
        try:
            element_present = ec.presence_of_element_located(*N_Locator.change_title)
            WebDriverWait(self.driver, 5).until(element_present)
            return self.get_title()
        except TimeoutException:
            return 0

