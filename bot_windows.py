import pywhatkit
import pyautogui as pt
import  pyperclip as pc
from pynput.mouse import Button, Controller
from time import sleep
import webbrowser

webbrowser.open("https://web.whatsapp.com")
sleep(7)
mouse = Controller()
pt.FAILSAFE = True
def nav_to_image(image, clicks , off_x = 0, off_y = 0):
    position = pt.locateCenterOnScreen(image,confidence=0.8)
    if position is None:
        print(f'{image} no encontro la imagen xd lol')
        return 0
    else:
        pt.moveTo(position,duration=.2)
        pt.moveRel(off_x,off_y, duration=.2)
        pt.click(clicks=clicks,interval=.1)

def get_message():
    nav_to_image('C://Users//ruymo//programacion//xd//bot_whatsapp//imagenes//clip_wpss.png',0,off_x=50,off_y=-80)
    mouse.click(Button.left,3)
    pt.rightClick()
    sleep(1)
    pt.moveRel(20,-320)
    mouse.click(Button.left,2)
    sleep(.5)
    return pc.paste()
    
def check_if_new_message():
    check = nav_to_image('C://Users//ruymo//programacion//xd//bot_whatsapp//imagenes//no_leido.png',1,off_x=-30,off_y=0)

    if check == 0:
        return False
    else:
        return True

if check_if_new_message():
    mensaje = get_message()    
    print(mensaje)
    cocina_txt = open("cocina.txt","w")
    cocina_txt.write(mensaje)
    cocina_txt.close()


    

