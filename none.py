import pyautogui
import pyperclip
from time import sleep

while True:

    sleep(2)
    (pyautogui.click(506, 236))
    for c in range (0, 2):
      sleep(2)
      (pyautogui.click(640, 666))
      pyautogui.hotkey('ctrl', 'v')
      pyautogui.press('enter')
      sleep(1)
      pyautogui.click(882, 403)
    pyautogui.click(1312,105)


