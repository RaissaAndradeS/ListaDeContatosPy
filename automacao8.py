## Instalar o pyautogui
import pyautogui
import time 

time.sleep(3)
pyautogui.hotkey('win')
time.sleep(2)
pyautogui.write('opera')
time.sleep(2)
pyautogui.press('enter')

time.sleep(5)


pyautogui.write('https://www.python.org')
time.sleep(2)
pyautogui.press('enter')

time.sleep(5)

