def calcular_factorial(numero):
    if numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial


# Solicitar al usuario el número
numero = int(input("Ingresa un número entero: "))

# Calcular y mostrar el factorial
factorial = calcular_factorial(numero)
print(f"El factorial de {numero} es: {factorial}")
