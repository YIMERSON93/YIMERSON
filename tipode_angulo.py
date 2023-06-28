#determinar el tipo de angulo

angulo= float (input("ingrese el valor del angulo en grados:"))

if angulo < 90:
    print ("el angulo es agudo.")
elif angulo > 90:
    print("el angulo es obtuso.")
else:
    print("el angulo es recto")
    
