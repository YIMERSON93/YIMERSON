def solicitar_contrasena():
    # Contraseña inventada
    contrasena_correcta = "contrasena123"
    
    # Solicitar contraseña al usuario
    contrasena = input("Ingrese la contraseña: ")
    
    # Verificar si la contraseña es correcta
    while contrasena != contrasena_correcta:
        print("Contraseña incorrecta. Inténtelo nuevamente.")
        contrasena = input("Ingrese la contraseña: ")
    
    print("Contraseña correcta. Acceso concedido.")


# Llamar a la función para solicitar la contraseña
solicitar_contrasena()
