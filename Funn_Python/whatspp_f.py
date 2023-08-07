from itertools import count
import pyautogui
import time
time.sleep(5)
#count=0

#while count<=20: 
for i in range (1,101):
    #pyautogui.typewrite("hello varsha  "+ str(count))
    pyautogui.typewrite(f"Heyy Bindu....   {i}")
    pyautogui.press("enter ")
    #count=count+1