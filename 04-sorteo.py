#SORTEO: los estudiantes deben pasar al frente a exponer, pero nadie quiere pasar
#primero. Diseñar un programa con una lista con los nombres de los estudiantes y de
#forma aleatorea generar otra lista que indique el orden en el que deben pasar.

import random

alumnoaux=""
alum=[]
otroalumn=0
o=[]
cantidad=0

print("Ingrese la cantidad de alumnos")
cantidad=int(input())
for i in range(0,cantidad):
    print("Ingrese el nombre del alumno")
    alumnoaux=input()
    alum.append(alumnoaux)
for i in range (len(alum)):
    otroalumn=random.randint(0,len(alum)-1)
    alumnos=alum[otroalumn]
    o.append(alumnos)
    del alum[otroalumn]
print("el orden en el que deberan pasar es:")
print (o)
