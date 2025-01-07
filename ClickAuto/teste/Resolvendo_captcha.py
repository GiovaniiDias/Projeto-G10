import pyautogui
import pyscreeze

captcha = pyscreeze.locateCenterOnScreen('C:\Users\Giovani\Desktop\Projeto G10\ClickAuto\teste\recaptcha.png')

print(captcha)

captcha = pyautogui.locateCenterOnScreen('recaptcha.png')
pyautogui.click(captcha[0], captcha[1], duration=2)