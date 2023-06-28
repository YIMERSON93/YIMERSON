oracion = input("Ingrese una oración: ")

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in oracion:
    if letra.lower() in vocales:
        vocales[letra.lower()] += 1

print("Cantidad de vocales:")
for vocal, cantidad in vocales.items():
    print(vocal, "=", cantidad)
