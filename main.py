import re
import time
import json
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
    url = "file:///C:/AutomationProject.html"
    driver = webdriver.Chrome()
    driver.get(url)
    # d = driver.find_element(By.ID, "send")
    driver.find_element(By.XPATH, "//button[text()='Start loading']").click()

    elem2 = WebDriverWait(driver, 20).until(ec.text_to_be_present_in_element((By.ID, "startLoad"), "Finish"))
    if elem2:
        print(driver.find_element(By.ID, "startLoad").text)

    # driver=Chrome()
    # a=BasePage(driver)
    # print(a.get_title())
    #data=data_from_json()
    #print(data[1]['Buttons'][1])
    #testwriteToFile('refal','refal')
    #data=data_from_json()
    #print(data_from_json())
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



