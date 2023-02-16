import inspect
import pytest
#from selenium.webdriver import Chrome, ActionChains
from page.BasePage import *
import time
from locator.LocatorAutomationProjectPage import Locator
from dotenv import load_dotenv
import os
import sys


url_title=os.getenv('Automation Project')
#driver = Chrome()
#base=BasePage(driver)

#class AutoTest():
@pytest.fixture()
def base():
      #driver1 = Chrome()
      return BasePage()

def test_gete(base):
   # print(base.base_url)
    #assert base.get_title()=='affa'
    assert base.printa()==5






