transporte_campanario: int(input("ingrese el valor"))
cafe_campanario: int(input("ingrese el valor"))
cafe_terraplaza: int(input("ingrese el valor"))
total_campanario= transporte_campanario + cafe_campanario
    
if cafe_terraplaza > total_campanario:
    print ("si el costo es ", cafe_terraplaza, "no se debe escoger esta opcion")
else:
    print ("si el costo es", total_campanario, "se debe escoger esta opcion")
