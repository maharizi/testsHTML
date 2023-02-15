from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re


class BasePage(object):
    def __init__(self, driver, url="file:///C:/Users/rafae/PycharmProjects/pom_project/test/Automation%20Project.html"):
        self.base_url = url
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def insert_text(self, *locator, text):
        text_box = self.find_element(*locator)
        text_box.clear()
        text_box.send_keys(text)

    def click_button(self, *locator):
        button = self.driver.find_element(*locator)
        button.click()

    def get_text_from_text_box(self, *locator):
        text_box = self.find_element(self, *locator)
        return text_box.get_attribute('value')

    def first_name_is_valid(self):
        # is not done
        location_first_nane = "<<const location of text box element for first namw>>"
        first_name = self.get_text_from_text_box(location_first_nane)
        if re.match("[a-zA-Z]{1,15}$", first_name):
            return True
        else:
            return False

    def last_name_is_valid(self):
        # is not done
        location_last_name = "<<const location of text box element for first namw>>"
        last_name = self.get_text_from_text_box(location_last_name)
        if re.match("[a-zA-Z]{1,15}$", last_name):
            return True
        else:
            return False

    def email_is_valid(self):
        location_email = "<<const location of text box element for first namw>>"
        email = self.get_text_from_text_box(location_email)
        if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
            return True
        else:
            return False

    def phone_number_is_valid(self):
        location_phone_number = "<<const location of text box element for first namw>>"
        phone_number = self.get_text_from_text_box(location_phone_number)
        if re.match(r'[0-9]{7}$', phone_number):
            return True
        else:
            return False

    def one_radio_button_is_selected(self):
        location_radio_button_female = "<<locator>>"
        location_radio_button_male = "<<locator>>"
        location_radio_button_other = "<<locator>>"
        radio_button_female = \
            self.driver.findElement(*location_radio_button_female).isSelected()
        radio_button_male = \
            self.driver.findElement(*location_radio_button_male).isSelected()
        radio_button_other = \
            self.driver.findElement(*location_radio_button_other).isSelected()
        if radio_button_other or radio_button_male or radio_button_female:
            return True
        else:
            return False
