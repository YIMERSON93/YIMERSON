# numero central
numero1= float(input("ingresa el primer numero:"))
numero2= float(input("ingresa el segundo numero:"))
numero3= float(input("ingresa el tercer numero:"))

if numero1 < numero2 < numero3 or numero3 < numero2 < numero1 :
    central= numero2

elif numero2 < numero1 < numero3 or numero3 < numero1 < numero2 :
    central= numero1
else:
    central=numero3
print ("el numero central es:", central)