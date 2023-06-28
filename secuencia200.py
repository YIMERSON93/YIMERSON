numero = int(input("Ingrese un número: "))

for n in range(numero + 1):
    term_n = 2 ** n
    if term_n > numero:
        break
    print(term_n)
