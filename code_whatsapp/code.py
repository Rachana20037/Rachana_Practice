import pyautogui as pg
import time

print("program will run in 5 sec")
time.sleep(5)

for i in range(100):
    pg.write("hi varsha")
    time.sleep(5)
    pg.press("Enter")