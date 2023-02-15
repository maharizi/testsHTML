from selenium.webdriver.common.by import By
from selenium import webdriver


class Locator(object):

    driver = webdriver.Chrome()
    driver.get('file:///C:/bootcamp ness/python/html/nextpage.html')
    change_title = (By.XPATH, "//button")
    print(driver.find_element(*change_title).text)



