import json
import os
from datetime import datetime
import sys


def data_from_json(path):

    os.chdir(os.getcwd())
    with open(path, 'r') as f:
         data = json.load(f)
    return data


def testwriteToFile(string, filename):

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
        print("Exception: " + str(e))
        sys.exit(1)


class Util(object):
    pass
