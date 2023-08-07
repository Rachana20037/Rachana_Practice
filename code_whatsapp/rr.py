from time import time
import pyautogui as pg
time.sleep(5)
for i in range(1,5):
    pg.typewrite(f"varsha {i}")
    pg.press("Enter")
