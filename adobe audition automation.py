import pyautogui
import time

print("press Ctrl+C to close")

#gehe zum audition icon (desktop)
pyautogui.size()
(1920, 1080)
pyautogui.moveTo(953, 872)
pyautogui.click(clicks=2)

#multitrack session starten
time.sleep(5)
pyautogui.moveTo(200, 60)
pyautogui.click()
pyautogui.moveTo(998, 415)
pyautogui.click()

print("15 seconds to type the name")
time.sleep(15)
pyautogui.moveTo(1043, 637)
pyautogui.click()




