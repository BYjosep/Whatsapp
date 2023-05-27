import pyautogui
import time
#vars
t = int(input("Indique el tiempo de arranque.\n"))
mensaje = input("\nIndique el mensaje.\n") 
r = int(input("\n Indique el numero de veces que desea repetir el mensaje.\n"))
ts = float(input("\n Indique el tiempo de espera entr Mensajes en segundos.\n" ))
n = 0

time.sleep(t)
while r >= 1:
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')
    n = n + 1
    print("estas por el mensaje ", n, "\n") 
    r = r - 1
    time.sleep(ts)
