def mostrar_numeros_impares(inicio, fin):
    # Asegurarse de que el inicio sea impar
    if inicio % 2 == 0:
        inicio += 1

    # Mostrar los números impares en el rango
    for numero in range(inicio, fin + 1, 2):
        print(numero)


# Ejemplo de uso
inicio = 11
fin = 35
mostrar_numeros_impares(inicio, fin)
