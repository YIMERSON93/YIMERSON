import random

def adivinar_numero():
    # Generar un número aleatorio secreto entre 1 y 100
    numero_secreto = random.randrange(1, 101)

    while True:
        # Solicitar al usuario que ingrese un número
        numero_usuario = int(input("Ingresa un número: "))

        # Comparar el número del usuario con el número secreto
        if numero_usuario < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        elif numero_usuario > numero_secreto:
            print("El número es menor. Intenta de nuevo.")
        else:
            print("¡Felicidades! Adivinaste el número.")
            break


# Ejecutar la función
adivinar_numero()
