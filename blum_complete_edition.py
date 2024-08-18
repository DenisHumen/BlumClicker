from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')



mouse = Controller()
time.sleep(0.5)

def click(x,y):
    mouse.position = (x, y+random.randint(1,3))
    mouse.press(Button.left)
    mouse.release(Button.left)

window_name = True

if window_name == True:
    window_name = "TelegramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print(f"[❌] | Окно - {window_name} не найдено!")
else:
    print(f"[✅] | Окно найдено - {window_name}\n[✅] | Нажмите 'q' для остановки.")

telegram_window = check[0]

while keyboard.is_pressed('q') == False:
    window_rect = (
        telegram_window.left,telegram_window.top,telegram_window.width,telegram_window.height
    )

    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

    width, height = scrn.size
    pixel_found = False
    if pixel_found == True:
        break

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x+4, screen_y)
                time.sleep(0.001)
                pixel_found = True
                break

print(f"[\u2705] | Окно найдено - {window_name}\n[\u2705] | Нажмите 'q' для остановки.")



print('[✅] | Остановлено.')