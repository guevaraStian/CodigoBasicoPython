#  -*- coding: utf-8 -*-
"""20200305-preparcial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10TPeOZirkhlVDajsX-wKRIFVvCTMhupr
"""

palabra = ""

while (palabra != "SALIR" ):
  palabra= input("Digite la palabra: ")

igual, aux = 0, 0
texto= input("Digite la palabra: ")

for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1

if len(texto) == igual:
  print("El texto es palindromo!")
else:
  print("El texto no es palindromo!")

igual, aux = 0, 0
texto=""

while (igual ==0 ):
  texto= input("Digite la palabra: ")
  for ind in reversed(range(0, len(texto))):
    if texto[ind].lower() == texto[aux].lower():
      igual += 1
  aux += 1

import random

n=int(input("Digite el tama�o de la matriz: "))
salida=""

matriz= [[0 for x in range(n)] for y in range(n)]

for i in range(0,len(matriz)):
  for j in range(0,len(matriz)):
    matriz[i][j] =random.randint(0,9)



for fila in range (0,len(matriz)):
  for colum in range(0,len(matriz[0])):
    salida += "  "+str(matriz[fila][colum])+"  "
  salida +="\n"
print(salida)

numeroesconder=int(input("Digite el numero que va a ingresar en la matriz: "))

#if(len(numeroesconder)>=len(matriz)):
#  print("el numero es muy grande")


aleatorio = random.randint(0,3)
print(aleatorio)

if(aleatorio==0):
  for i in range(0,len(matriz)):
    for j in range(0,len(matriz)):
      matriz[i][0] =numeroesconder

import random

aleatorio = random.randint(0,3)
print(aleatorio)

if(aleatorio==0):
  for i in range(0,len(matriz)):
    for j in range(0,len(matriz)):
      matriz[i][0] =numeroesconder