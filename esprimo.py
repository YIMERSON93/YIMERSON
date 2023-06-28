def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def imprimir_numeros_primos(n):
    print("Números primos hasta", n, ":")
    for numero in range(2, n + 1):
        if es_primo(numero):
            print(numero)


# Ejemplo de uso
numero = int(input("Ingrese un número natural: "))
imprimir_numeros_primos(numero)
