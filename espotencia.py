def es_potencia_de_dos(numero):
    if numero <= 0:
        return False
    while numero > 1:
        if numero % 2 != 0:
            return False
        numero = numero // 2
    return True


def suma_potencias_de_dos(inicio, fin):
    suma = 0
    for numero in range(inicio, fin + 1):
        if es_potencia_de_dos(numero):
            suma += numero
    return suma


# Ejemplo de uso
numero = 16
if es_potencia_de_dos(numero):
    print(numero, "es una potencia de 2")
else:
    print(numero, "no es una potencia de 2")

inicio = 10
fin = 30
suma = suma_potencias_de_dos(inicio, fin)
print("La suma de las potencias de 2 en el rango", inicio, "-", fin, "es:", suma)
