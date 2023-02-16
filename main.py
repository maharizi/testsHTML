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



