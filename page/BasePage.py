import os
from datetime import datetime
import dotenv

dotenv.load_dotenv("../test/.env")


class BasePage(object):

    def __init__(self, driver, url='file:///C:/AutomationProject.html'):
        """
        Constructor to this class,
        this function get webdriver and url
        :param driver:
        :param url:
        """
        self.url = url
        self.driver = driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def find_element(self, *locator):
        """
        This function get location of element
        and return object of this element
        :param locator:
        :return element:
        """
        try:
            return self.driver.find_element(*locator)
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

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
        return self.url

    def insert_text(self, *locator, text):
        """
        This function get location of text box
        and put in the parameter text
        :param locator:
        :param text:
        :return:
        """
        try:
            text_box = self.find_element(*locator)
            text_box.clear()
            text_box.send_keys(text)
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def click_button(self, *locator):
        """
        This function get location
        of button and click it
        :param locator:
        :return:
        """
        try:
            button = self.driver.find_element(*locator)
            button.click()
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def get_text_from_text_box(self, *locator):
        """
        This function get location of text box
        and return the current value
        :param locator:
        :return value:
        """
        try:
            text_box = self.find_element(*locator)
            return text_box.get_attribute('value')
        except Exception:
            raise Exception(os.getenv("LOCATOR_NOT_FOUND"))

    def screenshot(self, test_name):
        """ screenshot(test_name)
        This function do screenshot to failed test
        and save a photo in current folder.
        the photo name contains status, test name, and time.
        :param test_name:
        :return:
        """
        shot_date = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        photo_name = "FAILED" + "-" + test_name + "-" + shot_date
        self.driver.save_screenshot("../test/LOG_test_AutomationProjectPage/"+ photo_name +".png")
