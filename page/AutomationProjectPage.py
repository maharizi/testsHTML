import os
import re
import dotenv

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locator.LocatorAutomationProjectPage import Locator as A_Locator
from locator.LocatorNextPagePage import Locator as N_Locator
from page.BasePage import BasePage

dotenv.load_dotenv("../test/.env")


class HomePage(BasePage):

    def __init__(self, driver):
        """
        Constructor to this subclass,
        this constructor get driver and move it by super
        to the parent class
        :param driver:
        """
        super().__init__(driver)

    def first_name_is_valid(self):
        """
        This function check if the
        first name is valid by regex
        :return bool:
        """
        first_name = self.get_text_from_text_box(*A_Locator.first_name)
        first_name_regex = "[a-zA-Z]{1,15}$"
        if re.match(first_name_regex, first_name):
            return True
        else:
            raise ValueError(os.getenv("INVALID_FIRST_NAME"))

    def last_name_is_valid(self):
        """
        This function check if the
        last name is valid by regex
        :return bool:
        """
        last_name = self.get_text_from_text_box(*A_Locator.last_name)
        last_name_regex = "[a-zA-Z]{1,15}$"
        if re.match(last_name_regex, last_name):
            return True
        else:
            raise ValueError(os.getenv("INVALID_LAST_NAME"))

    def insert_city(self, city):
        """
        This function get a city as string
        and put it in the city option element.
        if the city is not exist - the function raise an error
        :param city:
        :return:
        """
        try:
            select = Select(self.driver.find_element(*A_Locator.city))
            return  select.select_by_visible_text(city)
        except Exception:
            raise ValueError(os.getenv("INVALID_CITY_NAME"))


    def insert_phone_number(self, phone_number):
        """
        This function get a full phone number
        and put the area code and the number in the
        input elements
        :param phone_number:
        :return:
        """
        try:
            select_area_code = Select(self.driver.find_element(*A_Locator.area_code))
            select_area_code.select_by_visible_text(phone_number[0:3])
            self.insert_text(*A_Locator.phone, text=phone_number[3:])
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def email_is_valid(self):
        """
        This function check if the
        email is valid by regex
        :return bool:
        """
        email = self.get_text_from_text_box(*A_Locator.email)
        email_regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if re.match(email_regex, email):
            return True
        else:
            raise ValueError(os.getenv("INVALID_EMAIL"))

    def phone_number_is_valid(self):
        """
        This function click femail radio button
        :return bool:
        """
        phone_number = self.get_text_from_text_box(*A_Locator.phone)
        phone_number_regex = r'[0-9]{7}$'
        if re.match(phone_number_regex, phone_number):
            return True
        else:
            raise ValueError(os.getenv("INVALID_PHONE_NUMBER"))

    def click_one_radio_button(self, option):
        """
        This function click
        radio-button
        :return null:
        """
        try:
            match option:
                case 'Other':
                    self.driver.find_element(*A_Locator.other).click()
                case 'Male':
                    self.driver.find_element(*A_Locator.male).click()
                case 'Female':
                    self.driver.find_element(*A_Locator.female).click()
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def one_radio_button_is_selected(self):
        """
        This function check if at least one
        radio-button is selected
        :return bool:
        """
        try:
            if self.find_element(*A_Locator.female).is_selected():
                return True
            if self.find_element(*A_Locator.male).is_selected():
                return True
            if self.find_element(*A_Locator.other).is_selected():
                return True
            return False
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def click_one_checkbox(self, options):
        """
        This function click
        checkbox
        :return null:
        """
        try:
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
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def at_least_one_check_box_is_selected(self):
        """
        This function check if at least one checkbox
        is selected
        :return bool:
        """
        try:
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
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def check_clear(self, click_clear=False):
        """
        This function check if all the fields
        were cleared after click clear button manually or automatically
        default is False
        :param click_clear:
        :return bool:
        """
        try:
            if click_clear:
                self.click_button(*A_Locator.clear)
            if self.get_text_from_text_box(*A_Locator.first_name):
                return False
            if self.get_text_from_text_box(*A_Locator.last_name):
                return False
            if self.get_text_from_text_box(*A_Locator.email):
                return False
            if self.get_text_from_text_box(*A_Locator.phone):
                return False
            if self.at_least_one_check_box_is_selected():
                return False
            if self.one_radio_button_is_selected():
                return False
            if self.one_radio_button_is_selected():
                return False
            return True
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def check_paragraph_content(self):
        """
        This function return the text
        from the paragraph content
        :return str:
        """
        try:
            paragraph = self.find_element(*A_Locator.paragraph_set_text)
            return paragraph.text
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def get_text_after_click_start_loading_button(self):
        """
        This function return the text which was changed
        after we click the button and wait some time
        if the text was not changed, this function return None
        :return str:
        """
        self.click_button(*A_Locator.button_start_loading)
        element_text = WebDriverWait(self.driver, 10)
        element_text. \
            until(ec.text_to_be_present_in_element(A_Locator.paragraph_start_loading, text_="Finish"))
        if element_text:
            return self.driver.find_element(*A_Locator.paragraph_start_loading).text
        else:
            raise TimeoutException(os.getenv("ELEMENT_NOT_DISPLAYED"))

    def get_title_next_page_after_is_opened(self):
        """
        This function return the title of the "next page"
        after we click the button which move to "next page"
        if the element from the "next page" is presented so
        the page is loaded
        :return:
        """
        self.click_button(*A_Locator.next_page)
        try:
            element_present = ec.presence_of_element_located(N_Locator.change_title)
            WebDriverWait(self.driver, 5).until(element_present)
            self.click_button(*N_Locator.change_title)
            return self.get_title()
        except Exception:
            raise Exception(os.getenv("WEBSITE_NO_LOADED"))

    def get_title_windy_after_is_opened(self):
        """
        This function return the title of the "windy page"
        after we click the button which move to "windy page"
        :return str:
        """
        self.click_button(*A_Locator.windy)
        try:
            element_present = ec.presence_of_element_located((By.ID, "logo"))
            WebDriverWait(self.driver, 5).until(element_present)
            return self.get_title()
        except Exception:
            raise Exception(os.getenv("WEBSITE_NO_LOADED"))

    def get_title_terra_santa_after_is_opened(self):
        """
        This function return the title of the "terra_santa page"
        after we click the button which move to "terra_santa page"
        :return str:
        """
        self.click_button(*A_Locator.tera_santa)
        try:
            element_present = ec.presence_of_element_located((By.ID, "wrap_all"))
            WebDriverWait(self.driver, 5).until(element_present)
            return self.get_title()
        except Exception:
            raise Exception(os.getenv("WEBSITE_NO_LOADED"))

    def get_title_java_book_after_is_opened(self):
        """
        This function return the title of the "java_book page"
        after we click the button which move to "java_book page"
        :return str:
        """
        try:
            self.click_button(*A_Locator.java_book)
            return self.get_title()
        except Exception:
            raise Exception(os.getenv("WEBSITE_NO_LOADED"))

    def get_title_youtube_after_is_opened(self):
        """
        This function return the title of the "YouTube page"
        after we click the button which move to "YouTube page"
        :return str:
        """
        self.click_button(*A_Locator.youtube)
        try:
            element_present = ec.presence_of_element_located((By.ID, "logo-icon"))
            WebDriverWait(self.driver, 5).until(element_present)
            return self.get_title()
        except Exception:
            raise Exception(os.getenv("WEBSITE_NO_LOADED"))

    def set_text_in_prompt_alert(self, text):
        """
        This function opens prompt alert and set in the
        parameter text, this text will be shown
        in the paragraph content input
        :param text:
        :return:
        """
        try:
            self.driver.find_element(*A_Locator.button_set_text).click()
            WebDriverWait(self.driver, 5).until(ec.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.send_keys(text)
            alert.accept()
            self.driver.implicitly_wait(5)
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))
