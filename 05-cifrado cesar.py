
desp=0
cifrar=0
texto=""
print("ingrese el texto que desee cifrar")
texto=input()
print("cúal va a ser su desplazamiento?")
desp=int(input())
def cifrar(texto, desp):
    mensaje=""
    for i in texto:
        cifrar=ord(i)+desp
        if(cifrar<ord("A")):
            cifrar=cifrar+26
        if(cifrar>ord("Z")):
            cifrar=cifrar-26
    mensaje=mensaje+chr(cifrar)
    print(mensaje)
    

