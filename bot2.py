import pyautogui, webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+5491170276273")
sleep(10)

pyautogui.typewrite("hola tai soy el segundo bot de ruy")
pyautogui.press("enter")