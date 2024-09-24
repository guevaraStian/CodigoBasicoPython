#Primero se instala PyAutoGUI con el siguiente comando  "pip install PyAutoGUI"
import pyautogui
import time

#Con las 2 funciones siguientes, se mueve el mause hacia una coordenada exacta.
#Con moveTo, el puntero del mause llega rapido y con moverel, se demora su transporte
pyautogui.moveTo(300,300, duration=30)
pyautogui.press("enter")
pyautogui.moveRel(300,300, duration=30)
time.sleep(5)

pyautogui.moveTo(300,300, duration=30)
pyautogui.moveRel(300,300, duration=30)
time.sleep(5)

pyautogui.moveTo(300,300, duration=30)
pyautogui.moveRel(300,300, duration=30)

pyautogui.alert('Terminamos el script.')

