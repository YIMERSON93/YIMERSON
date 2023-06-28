def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma


# Ejemplo de uso
numero = 12
suma = suma_divisores(numero)
print("La suma de los divisores de", numero, "es:", suma)
