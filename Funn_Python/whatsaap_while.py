from itertools import count
import pyautogui
import time
time.sleep(5)
count=0

while count<=100: 
    pyautogui.typewrite("hello Esakki "+ str(count))
  
    pyautogui.press("enter ")
    count=count+1