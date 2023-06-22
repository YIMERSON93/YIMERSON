numero= int(input("ingresa el numero:"))
binario= ""
modulo= numero
while numero > 0:
    if numero % 2 == 0:
        binario= "0" +str(binario)
    else:
        binario = "1" + str(binario)
    numero= numero // 2
print ("el numero", modulo, "en binario es igual a", binario)

 
