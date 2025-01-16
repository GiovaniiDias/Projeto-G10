import pyautogui
import keyboard
import win32con # type: ignore
import win32api # type: ignore
from time import sleep

pyautogui.click(540,400, duration=1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0 , 0)


while keyboard.is_pressed('1')  == False:
    if pyautogui.pixelMatchesColor(440,400,(0, 0 , 0)):
        click(440,400)

    if pyautogui.pixelMatchesColor(508,400,(0, 0 , 0)):
        click(508,400)
    
    if pyautogui.pixelMatchesColor(568,400,(0, 0 , 0)):
        click(568,400)
    
    if pyautogui.pixelMatchesColor(629,400,(0, 0 , 0)):
        click(629,400)