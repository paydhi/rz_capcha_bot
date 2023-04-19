# Farm bot for rappelz space by paydhi

import matplotlib.pyplot as plt
import numpy as np
import cv2
import pytesseract
import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# image = pyautogui.screenshot()
image = cv2.imread(r"C:\\Untitled10.png")
image_BGR = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#text_image = image_BGR[255, 255, :]
b,g,r = cv2.split(image_BGR)
text_image = cv2.merge((b,g))
text_image = cv2.cvtColor(np.array(text_image), cv2.COLOR_BGR2RGB)
cv2.imwrite('result.png', image)
cv2.imwrite('result1.png', image_BGR)
cv2.imwrite('result2.png', text_image)
#black = (0, 0, 0)
#white = (255, 255, 255)
text_colour = (255, 255, 0)
text_colour_diff = (254, 254, 0)



black_and_white_mask = cv2.inRange(image_BGR, text_colour, text_colour_diff)
#result = cv2.bitwise_and(image, image, mask=black_and_white_mask)
#result = cv2.cvtColor(np.array(result), cv2.COLOR_BGR2RGB)
#text = pytesseract.image_to_string(result)
#print(text)
#cv2.imwrite('result.png', result)
#only_text_image = cv2.bitwise_and(black_and_white_mask)

# text = pytesseract.image_to_string(only_text_image)
