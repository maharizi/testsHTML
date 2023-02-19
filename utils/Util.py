import inspect
import pyautogui
import cv2
import numpy as np
import json
import os
from datetime import datetime
import sys


def data_from_json(path):
    # shlomo path - C:\\Users\\shlomo\\PycharmProjects\\pomProject\\utils\\ddt.json
    #maor path- C:\\Users\\User\\PycharmProjects\\SeleniumProjectNew\\pomProject\\utils\\ddt.json
    #with open('C:\\Users\\shlomo\\PycharmProjects\\pomProject\\utils\\ddt.json', 'r') as f:
    os.chdir(os.getcwd())
    with open(path, 'r') as f:
         data = json.load(f)
    return data


def testwriteToFile(string, filename):

    #os.chdir(os.getcwd())
    # shlomo path - C:\\Users\\shlomo\\PycharmProjects\\pomProject\\test\LOG_test_AutomationProjectPage
    #maor path- C:\\Users\\user\\PycharmProjects\\SeleniumProjectNew\\pomProject\\test\LOG_test_AutomationProjectPage
    #directory = 'C:\\Users\\shlomo\\PycharmProjects\\pomProject\\test\LOG_test_AutomationProjectPage'
    directory='LOG_test_AutomationProjectPage'
    try:
        date = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        filename += f"{date}.txt"
        filepath = os.path.join(directory, filename)
        file = open(filepath, 'a')
        string += datetime.now().strftime(" %d/%m/%Y %H:%M:%S\n------------\n")
        file.write(string)
        file.flush()
        file.close()
    except Exception as e:
        #writeToFile("Something went wrong: " + str(e))
        print("Exception: " + str(e))
        sys.exit(1)


class Util(object):
    pass
