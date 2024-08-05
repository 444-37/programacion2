nombre=""
nacimiento=0
actual=0
edad=0

print("ingrese su nombre")
nombre=input()

print("Hola "+nombre+", podrías decirme tu año de nacimiento?")
nacimiento=int(input())

print("ahora podrías decirme el año actual?")
actual=int(input())

edad=(actual-nacimiento)
print("supongo que vas a cumplir ", edad)