

numero_uno= int(input("ingrese el valor"))
numero_dos= int(input("ingrese el valor"))
numero_tres=int(input("ingrese el numero"))
                      
if numero_uno > numero_dos and numero_dos > numero_tres:
    print ("numero_uno", numero_uno, "numero_dos", numero_dos, "numero_tres", numero_tres  )
elif numero_dos > numero_uno and numero_uno > numero_tres:
    print ("numero_dos", numero_dos, "numero_uno", numero_uno, "numero_tres", numero_tres  )
elif numero_tres > numero_uno and numero_uno > numero_dos:
    print ("numero_uno", numero_uno, "numero_dos", numero_dos, "numero_tres", numero_tres  )
elif numero_tres > numero_dos and numero_dos > numero_uno:
     print ("numero_tres", numero_tres, "numero_dos", numero_dos, "numero_uno", numero_uno  )
elif numero_uno > numero_tres and numero_tres > numero_dos:
     print ("numero_uno", numero_uno, "numero_tres", numero_tres, "numero_dos", numero_dos )
elif numero_dos > numero_tres and numero_tres > numero_dos:
     print ("numero_dos", numero_dos, "numero_tres", numero_tres, "numero_uno", numero_uno  )

    


    



