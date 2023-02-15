from selenium.webdriver.common.by import By
from selenium import webdriver


class Locator(object):

    driver = webdriver.Chrome()
    driver.get('file:///C:/bootcamp ness/python/html/nextpage.html')
    change_title = (By.XPATH, "//button")
    ele = driver.find_element(By.XPATH, "//button")
    print(ele.text)




