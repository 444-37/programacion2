col=4
sumadp=0
multdp=1
sumacd=0
multcd=1
M=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(4):
    for j in range(4):
        if (i==j):
            print(M[i][j])
            sumadp=sumadp+M[i][j]
            multdp=multdp*M[i][j]
        if (i==col-1-j):
            sumacd=sumacd+M[i][j]
            multcd=multcd*M[i][j]
print("la suma de la diagonal principal es: ",sumadp, "y la multiplicación de la misma es: ",multdp)
print("la suma de la contra diagonal es: ",sumacd, "y la multiplicación de la misma es: ",multcd)

            
            
            
