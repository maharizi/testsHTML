import re
import time
import json

from selenium.webdriver.common.alert import Alert

from locator.LocatorAutomationProjectPage import Locator

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from utils.Util import *
from page.BasePage import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from page.AutomationProjectPage import HomePage
from page.BasePage import BasePage


if __name__ == '__main__':
    driver = webdriver.Chrome()
    time.sleep(5)
    driver.get("file:///C:/AutomationProject.html")
    # time.sleep(5)
    #
    # time.sleep(5)
    # alert = Alert(driver)
    # time.sleep(5)
    # obj = driver.switch_to.alert
    # obj.accept()
    # time.sleep(5)
    # print(obj.text)
    # time.sleep(5)

    try:
        driver.find_element(By.XPATH, "//fieldset/button[1]").click()
        WebDriverWait(driver, 5).until(ec.alert_is_present())
        alert = driver.switch_to.alert
        alert.send_keys('560085')
        time.sleep(3)
        alert.accept()
        driver.implicitly_wait(5)
    except TimeoutException as e:
        print(e)


