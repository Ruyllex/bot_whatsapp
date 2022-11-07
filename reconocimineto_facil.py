import pyautogui as pt
import webbrowser
import time

def seguir_cara(image,off_x = 0, off_y = 0):
    position = pt.locateCenterOnScreen(image,confidence=0.40) 
    if position is None:
        print(f'{image} no encontro la imagen xd lol')
        return 0
    else:  
        webbrowser.open('https://www.youtube.com/watch?v=bt_jOWmiiiU f',2)
        time.sleep(3)
        pt.press('space')
        pt.press('f')

while True:
    seguir_cara('C://Users//ruymo//programacion//xd//bot_whatsapp//imagenes//ruy.png',off_x=-40,off_y=0)