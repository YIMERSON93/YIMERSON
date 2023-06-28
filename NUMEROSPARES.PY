def mostrar_numeros_pares(inicio, fin):
    # Asegurarse de que el inicio sea par
    if inicio % 2 != 0:
        inicio += 1

    # Mostrar los números pares en el rango
    for numero in range(inicio, fin + 1, 2):
        print(numero)


# Ejemplo de uso
inicio = 10
fin = 30
mostrar_numeros_pares(inicio, fin)
