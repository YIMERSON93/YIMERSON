oracion = input("Ingrese una oración: ")
letra_buscada = input("Ingrese la letra que desea buscar: ")

contador = 0

for letra in oracion:
    if letra == letra_buscada:
        contador += 1

print("La letra", letra_buscada, "aparece", contador, "veces en la oración.")
