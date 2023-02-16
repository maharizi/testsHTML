from selenium.webdriver.common.by import By
from selenium import webdriver


class Locator(object):

    # driver = webdriver.Chrome()
    # driver.get('file:///C:/bootcamp ness/python/html/Automation Project.html')
    first_name = (By.NAME, 'fname')
    last_name = (By.NAME, 'lname')
    city = (By.NAME, 'City')
    email = (By.NAME, 'email')
    area_code = (By.NAME, 'areaCode')
    phone = (By.NAME, 'phone')
    female = (By.XPATH, "//tr[1]/td/input[@id='f']")
    male = (By.XPATH, "//tr[1]/td/input[@id='m']")
    other = (By.XPATH, "//tr[1]/td/input[@id='o']")
    math = (By.XPATH, "//tr[2]/td/input[@id='m']")
    physics = (By.XPATH, "//tr[2]/td/input[@id='p']")
    pop = (By.XPATH, "//fieldset/input[@id='m']")
    dud = (By.XPATH, "//fieldset/input[@id='o']")
    biology = (By.XPATH, "//fieldset/input[@id='b']")
    chemistry = (By.XPATH, "//fieldset/input[@id='c']")
    english = (By.XPATH, "//fieldset/input[@id='e']")
    ok = (By.XPATH, "//fieldset/fieldset/input[@value='OK']")
    clear = (By.XPATH, "//fieldset/fieldset/input[@id='CB']")
    send = (By.XPATH, "//fieldset/fieldset/input[@id='send']")
    #print(driver.find_element(*send).get_attribute('value'))




