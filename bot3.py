import pyautogui as pt
import  pyperclip as pc
from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()
pt.FAILSAFE = True
def nav_to_image(image, clicks , off_x = 0, off_y = 0):
    position = pt.locateCenterOnScreen(image,confidence=0.8)
    if position is None:
        print(f'{image} not found')
        return 0
    else:
        pt.moveTo(position,duration=.2)
        pt.moveRel(position,off_y, duration=.2)
        pt.click(clicks=clicks,interval=.1)

def get_message():
    nav_to_image('/home/ruy/programacion/proyectos/bot_whatsapp/imagenes/clip_wpss.png',0)