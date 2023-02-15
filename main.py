import re
import time

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from page.AutomationProjectPage import HomePage


if __name__ == '__main__':
    url = "file:///C:/Users/rafae/PycharmProjects/pom_project/test/Automation%20Project.html"
    driver = webdriver.Chrome()
    # home_page = HomePage(url, driver)
    # home_page.driver.get(home_page.url)
    # # driver = webdriver.Chrome()
    driver.get(url)
    # # driver.find_element(By.CSS_SELECTOR, "a.btn").click()
    # # a = driver.window_handles
    # # driver.switch_to.window(a[0])
    # # print(driver.title)
    # print(home_page.driver.title)
    time.sleep(10)
    radio_button_female = driver.find_element(By.ID, "f").is_selected()
    print(radio_button_female)


