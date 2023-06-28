# calificacion numerica a letra

calificacion= int (input("ingrese la calificacion (0-100):"))

if calificacion >=90:
    letra= "A"
elif calificacion >=80:
    letra= "B"
elif calificacion >=70:
    letra= "C"
elif calificacion >=60:
    letra= "D"
else:
    letra= "F"
print ("la calificacion en letra es:", letra)
