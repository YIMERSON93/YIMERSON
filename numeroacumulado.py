acumulado = 0

while True:
    numero = int(input("Ingrese un número (ingrese 0 para terminar): "))
    if numero == 0:
        break
    acumulado += numero

print("El número acumulado es:", acumulado)
