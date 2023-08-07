#print("heyy rachana")hello sis
from itertools import count
import pyautogui
import time
time.sleep(5)
count=0
while count<=5:
    pyautogui.typewrite("hello sis "+" "+str(count))
    pyautogui.press("Enter ")
    count=count+1