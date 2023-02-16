from selenium.webdriver.common.by import By
from selenium import webdriver


class Locator(object):

    # driver = webdriver.Chrome()
    # driver.get('file:///C:/bootcamp ness/python/html/AutomationProject.html')
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
    paragraph_set_text = (By.ID, 'pbyuser')
    button_set_text = (By.XPATH, "//fieldset/button[1]")
    # Strange - text doesn't change to 'Finish'
    paragraph_start_loading = (By.ID, 'startLoad')

    paragraph_start_loading_after_click = (By.ID, 'startLoad')
    button_start_loading = (By.XPATH, "//fieldset/button[2]")
    next_page = (By.LINK_TEXT, 'Next Page')
    windy = (By.LINK_TEXT, 'Windy')
    tera_santa = (By.LINK_TEXT, 'Tera Santa')
    java_book = (By.LINK_TEXT, 'Java Book')
    youtube = (By.LINK_TEXT, 'YouTube')
    # driver.find_element(*youtube).click()
    # input()
    # print(driver.find_element(*next_page).text)
    # print(driver.find_element(*button_set_text).get_attribute('value'))
