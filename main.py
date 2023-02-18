import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from locator.LocatorAutomationProjectPage import Locator as A_Locator
from locator.LocatorNextPagePage import Locator as N_Locator
import re

from page.BasePage import BasePage

if __name__ == '__main__':
    driver = Chrome()
    bs = BasePage(driver)
    time.sleep(10)
    print(bs.get_text_after_click_start_loading_button())
