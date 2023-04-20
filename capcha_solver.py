# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:51:10 2020

@author: Paydhi
"""

from time import sleep
import re
import logging
import numpy as np
import cv2
import pytesseract
import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
   
        
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen"
      ]
      for idx, word in enumerate(units):    
          numwords[word] = (1, idx)
    current = result = 0
    for word in textnum.split():
        scale, increment = numwords[word]
        current = current * scale + increment
    return result + current

def get_problem():
    #image_path = r"E:\\farm_bot\\test_to_crop.png"
    #image = cv2.imread(image_path)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = image[22:922, 3:1603] # Cropping to 1600 by 900
    image = image[100:230, 500:1100] # Cropping text only
    image[image[:, :] != [255, 255, 0]] = 254 # Make all non-cyan pixels white
    image[image[:, :] == [255, 255, 0]] = 0 # Make all cyan pixels black
    cv2.imwrite('result.png', image)
    problem = pytesseract.image_to_string(image)
    problem = problem.lower()
    return problem

def solve_math_problem(text_problem):
    math_prob_str = re.split(r' ', text_problem)
    if math_prob_str[0].isdigit():
        a = int(math_prob_str[0])
    else:
        a = text2int(math_prob_str[0])

    if math_prob_str[2].isdigit():
        b = int(math_prob_str[2])
    else:
        b = text2int(math_prob_str[2])
    
    if (math_prob_str[1] == '+') or (math_prob_str[1] == 'plus'):
        answer = a + b
    else:
        answer = a - b
    
    return answer
    

def press_button(a):
    pyautogui.keyDown('shift')
    pyautogui.press(str(a))
    pyautogui.keyUp('shift')
    pyautogui.keyDown('n')


while True:
    sleep(3)
    text = get_problem()
    if not text:
        continue
    print(text)
    try:    
        problem_result = solve_math_problem(text)
    except:
        logging.exception('error')
        continue
    print("Answer is", problem_result)
    press_button(problem_result)
    print("Button pressed")
    
















