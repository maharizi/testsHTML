import re
import time
import json

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
<<<<<<< HEAD









=======
    locator=Locator()
    driver=Chrome()
    a=BasePage(driver)

    #a.insert_text(*Locator.first_name,text='shlomo')
    #a.click_one_checkbox('Physics')
    #a.insert_text(*Locator.paragraph_set_text, text='shlomo')

    time.sleep(10)
    print(a.check_paragraph_content())

    input()
    # name="shlomo"
    # a.insert_text(*Locator.first_name,text='shlomo')
    # time.sleep(5)
    # print(a.get_text_from_text_box(*Locator.first_name))
    # print(a.get_title())
>>>>>>> 68d9fadb21e0db333b1b4f8cd56183008a78cef6

    #data=data_from_json()
    #print(data[1]['Buttons'][1])
    #testwriteToFile('refal','refal')

   # print(data_from_json())

    #url = "file:///C:/Users/rafae/PycharmProjects/pom_project/test/Automation%20Project.html"
    #driver = webdriver.Chrome()
    # home_page = HomePage(url, driver)
    # home_page.driver.get(home_page.url)
    # # driver = webdriver.Chrome()
    #driver.get(url)
    # # driver.find_element(By.CSS_SELECTOR, "a.btn").click()
    # # a = driver.window_handles
    # # driver.switch_to.window(a[0])
    # # print(driver.title)
    # print(home_page.driver.title)
    #time.sleep(10)
   #radio_button_female = driver.find_element(By.ID, "f").is_selected()
    #print(radio_button_female)




