# diseñe e implemente un programa que genere un número aleatorio entre 1 y 20.
#el jugador tiene 6 intentos para adivinar el número. En cada intento indica si el
#número secreto es maor o menor que el ingesado por el usuario, si es igual el jugadorgana
# *añadir al programa al menos dos dificultades, eje: facil (1,20) con 6 intentos; dificil (1,200) con 7 intentos
#la dificultad debe ser elegida por el usuario, modificar variable  luego y ejecutar el
#mismo codigo pra e programa. definir una función (def) para star la dificultad


import random
numrandomF=random.randint(1,20)
numrandomD=random.randint(1,300)
dificultad=0
numingresado=0
vueltas=0

print("¿Desea iniciar e juego en nivel facil o dificil, presiona 1 para facil  2 para dificil?")
dificultad=int(input())
if (dificultad==1):
    while(vueltas<6):
        numrandomF=random.randint(1,20)
        print(" veo que elgiste el modo facil,muy bien, intente adivinar ingresando un número. Recuerda que cuentas con 6 vidas")
        numingresado=int(input())
        vueltas=vueltas+1
            if(numrandomF>numingresado):
                print("el número ingresado es menor al número aleatoreo")
            else:
                if(numrandomF<numingresado):
                    print("el numero ingresado es mayor al número aleatoreo")
                else:
                    if(numrandomF==numingresado):
                        print("FELICIDADES!! haz adivinado")
                        break
                    else:
                        print("lo lamentamos, no has adivinado en tus 6 intentos")
                        break
else:
    if (dificultad==2):
        while(vueltas<7):
            numrandomD=random.randint(1,300)
            print(" veo que elgiste el modo dificil,muy bien, intente adivinar ingresando un número. Recuerda que cuentas con 7 vidas")
            numingresado=int(input())
            vueltas=vueltas+1
                if(numrandomD>numingresado):
                    print("el número ingresado es menor al número aleatoreo")
                else:
                    if(numrandomD<numingresado):
                        print("el numero ingresado es mayor al número aleatoreo")
                    else:
                        if(numrandomD==numingresado):
                            print("FELICIDADES!! haz adivinado")
                            break
                        else:
                            print("lo lamentamos, no has adivinado en tus 7 intentos")
                            break:
    else:
        print("El número de dificultad no es valido")
        break:

