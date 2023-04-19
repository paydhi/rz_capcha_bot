# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:46:10 2020

@author: Paydhi
"""


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
print(text2int("two"))


'''
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
        "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
        "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать",
      ]
      tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
      scales = ["сто", "тысяч", "миллион", "миллиард", "триллион"]
      numwords["и"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)
    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Неверное слово: " + word)
        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    return result + current
print text2int("семьдесят тысяч пятьдесят три")
'''