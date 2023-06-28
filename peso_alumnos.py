#estadistica peso alumnos


alumnos_menos40kg= 0
alumnos_40kg_50kg= 0
alumnos_mas50_menos60= 0
alumnos_mas_igual60= 0

total_alumnos= int(input("ingrese el numero total de alumnos:"))
for i in range (total_alumnos):
    peso= float (input("ingrese el peso del alumno {}:".format(i+1)))

if peso < 40:
    alumnos_menos40kg=1
elif 40 <= peso < 50:
    alumnos_40kg_50kg=1
elif 50 <= peso< 60:
    alumnos_mas50_menos60= 1
else:
    alumnos_mas_igual60=1

print ("estadisticas de pesos de los alumnos:")
print ("alumnos de menos de 40kg:", alumnos_menos40kg)
print ("alumnos entre 40 y 50kg:", alumnos_40kg_50kg)
print ("alumnos de mas de 50 y menos de 60kg:", alumnos_mas50_menos60)
print ("alumnos de mas o igual a 60 kg:", alumnos_mas_igual60)
