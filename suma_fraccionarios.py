from fractions import Fraction
fraccion1= Fraction (input("ingresa la primera fraccion (en el formato a/b):"))
fraccion2= Fraction (input("ingresa la segunda fraccion (en el formato a/b):"))
fraccion3= Fraction (input("ingresa la tercera fraccion (en el formato a/b):"))

resultado= fraccion1 + fraccion2 + fraccion3
resultado2= float (resultado)

print ("la suma de las fracciones es:", resultado)
print ("la suma de las fracciones en decimal es:", resultado2)
