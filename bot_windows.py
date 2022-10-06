import pywhatkit
import pyautogui as pt
import  pyperclip as pc
from pynput.mouse import Button, Controller
from time import sleep
import webbrowser



FIN_ARCHIVO = ['999999',0,0,0]
webbrowser.open("https://web.whatsapp.com")
sleep(7)
mouse = Controller()
pt.FAILSAFE = True

def leer_archivo(texto):
    linea = texto.readline().rstrip('\n')
    if linea:
        linea = linea.split(',')
    else:
        linea = FIN_ARCHIVO
    return linea

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
    check = nav_to_image('C://Users//ruymo//programacion//xd//bot_whatsapp//imagenes//no_leido.png',0,off_x=-40,off_y=0)
    mouse.click(Button.left,1)
    if check == 0:
        return False
    else:
        return True

def close_replybox():
    nav_to_image('C://Users//ruymo//programacion//xd//bot_whatsapp//imagenes//equis_wpps.png',1,off_x=0,off_y=0)

delay = 5
last_message = ''

def process_mesagge(mesagge):
    respuesta = ""
    if "hola" in mesagge.lower():
        respuesta = "hola"
    else:
        respuesta = "No te entiendo todavia."
        cocina = open("cocina.csv","r+")
        linea = leer_archivo(cocina)
        cocina.write("1")
        print(linea)
        cocina.close()
    return respuesta



sleep(3)
while True:
    if not check_if_new_message():
        print("no hay mensajes")
    else:
        print("recibi un mensaje")
        mensaje = get_message()
        last_message = mensaje
        pt.write(process_mesagge(last_message))
        #pt.press("enter")
    sleep(5)


