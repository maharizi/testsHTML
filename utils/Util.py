import inspect
import pyautogui
import cv2
import numpy as np
import json
import os
from datetime import datetime
import sys


def recorde_test():
    # Specify resolution
    resolution = (1920, 1080)

    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")

    # Specify name of Output file
    filename = str(inspect.currentframe().f_code.co_name) + ".avi"

    # Specify frames rate. We can choose any
    # value and experiment with it
    fps = 5.0

    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    # Create an Empty window
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    # Resize this window
    cv2.resizeWindow("Live", 480, 270)

    while True:
        # Take screenshot using PyAutoGUI
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert it from BGR(Blue, Green, Red) to
        # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write it to the output file
        out.write(frame)

        # Optional: Display the recording screen
        cv2.imshow('Live', frame)

        # Stop recording when we press 'q'
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the Video writer
    out.release()

    # Destroy all windows
    cv2.destroyAllWindows()


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
        string += datetime.now().strftime(" %d/%m/%Y %H:%M:%S\n")
        file.write(string)
        file.flush()
        file.close()
    except Exception as e:
        #writeToFile("Something went wrong: " + str(e))
        print("Exception: " + str(e))
        sys.exit(1)


class Util(object):
    pass
