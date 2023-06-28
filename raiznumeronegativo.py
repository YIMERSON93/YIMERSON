# calcular la raiz cuadrada de un numero negativo

import math

numero= float (input("ingrese un numero:"))

if numero>=0:
    raiz_cuadrada = math.sqrt(numero)
    print ("la raiz cuadrada de", numero, "es", raiz_cuadrada)
else:
    raiz_cuadrada= match. sqrt (abs(numero))
    print ("el numero es negativo. la raiz cuadrada de su valor absoluto es:", raiz_cuadrada)