def factorizar(k):
    # Inicializamos una lista vacía para almacenar los factores primos
    factores_primos = []
    
    # Iteramos desde 2 hasta la raíz cuadrada de k+1
    for i in range(2, int(k**0.5) + 1):
        # Si i es un factor de k, lo agregamos a la lista y reducimos k dividiéndolo por i
        while (k % i == 0):
            factores_primos.append(i)
            k = k // i
    
    # Si k es mayor que 1, significa que es un factor primo
    if k > 1:
        factores_primos.append(k)
    
    return factores_primos


# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Llamamos a la función factorizar() y obtenemos la descomposición en factores primos
factores = factorizar(numero)

# Imprimimos los factores primos
print("La descomposición en factores primos de", numero, "es:")
print(factores)
