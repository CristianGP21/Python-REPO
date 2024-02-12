import pyautogui as pag
import random
import time
import keyboard

while True:
    x = random.randint(600,700)
    y = random.randint(200,300)
    pag.moveTo(x,y,0.5)

    if keyboard.is_pressed('esc'):
        break

    time.sleep(0.2)
