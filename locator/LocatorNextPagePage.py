from selenium.webdriver.common.by import By


class Locator(object):
    id_combo_box = (By.ID, 'RESULT_RadioButton-9')
    xpath_first_option = (By.XPATH, "//option[@value='Radio-0']")
