import pyautogui
import keyboard
from time import sleep


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(488,577,(0,152,0)):
        pyautogui.press('a')
        
    
    if pyautogui.pixelMatchesColor(582,576,(255,0,0)):
        pyautogui.press('s')
        
    
    if pyautogui.pixelMatchesColor(670,578,(244,244,2)):
        pyautogui.press('j')
        
    
    if pyautogui.pixelMatchesColor(757,580,(0,152,255)):
        pyautogui.press('k')
        
    
    if pyautogui.pixelMatchesColor(855,582,(255,101,0)):
       pyautogui.press('l')
       