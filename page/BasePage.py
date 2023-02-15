from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locator.LocatorAutomationProjectPage import Locator
import re


class BasePage(object):
    def __init__(self, driver, url="file:///C:/Users/rafae/PycharmProjects/pom_project/test/Automation%20Project.html"):
        """
        Constructor to this class,
        this function get webdriver and url
        :param driver:
        :param url:
        """
        self.base_url = url
        self.driver = driver

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
        return self.driver.current_url

    def insert_text(self, *locator, text):
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
        text_box = self.find_element(self, *locator)
        return text_box.get_attribute('value')

    def first_name_is_valid(self):
        """
        This function check if the
        first name is valid by regex
        :return bool:
        """
        first_name = self.get_text_from_text_box(*Locator.first_name)
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
        last_name = self.get_text_from_text_box(*Locator.last_name)
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
        email = self.get_text_from_text_box(*Locator.email)
        if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
            return True
        else:
            return False

    def phone_number_is_valid(self):
        """
        This function check if the
        phone number is valid by regex
        :return bool:
        """
        phone_number = self.get_text_from_text_box(Locator.phone)
        if re.match(r'[0-9]{7}$', phone_number):
            return True
        else:
            return False

    def one_radio_button_is_selected(self):
        """
        This function check if at least one
        radio-button is selected
        :return bool:
        """
        radio_button_female = \
            self.driver.findElement(*Locator.female).isSelected()
        radio_button_male = \
            self.driver.findElement(*Locator.male).isSelected()
        radio_button_other = \
            self.driver.findElement(*Locator.other).isSelected()
        if radio_button_other or radio_button_male or radio_button_female:
            return True
        else:
            return False


