def imprimir_secuencia():
    numero = int(input("Ingresa el número inicial de la secuencia: "))
    
    while True:
        print(numero)
        opcion = input("¿Deseas continuar? (s/n): ")
        if opcion.lower() != 's':
            break
        numero += 1


# Ejecutar la función
imprimir_secuencia()
