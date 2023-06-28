def imprimir_numeros_perfectos(m):
    count = 0
    numero = 1
    while count < m:
        if suma_divisores(numero) == numero:
            print(numero)
            count += 1
        numero += 1


# Ejemplo de uso
cantidad_numeros_perfectos = 4
imprimir_numeros_perfectos(cantidad_numeros_perfectos)
