acumulado = 0
cantidad_numeros = 0

while True:
    numero = int(input("Ingrese un número (ingrese 0 para terminar): "))
    if numero == 0:
        break
    acumulado += numero
    cantidad_numeros += 1

print("El número acumulado es:", acumulado)
print("La cantidad de números ingresados es:", cantidad_numeros)
