
#lee n1,n2
#si n1==n2 hacer
    #escribe Los números no pueden ser iguales 
#sino si n1>n2
#   mientras n2==n1
#       n2+=1
#       escribe n2
#  sino  mientras n2==n1
#       n1+=1
#       escribe n1
n1=int(input("Dame un número: "))
n2=int(input("Dame otro número: "))
cont=0
nc=n1
nc2=n2
if n1==n2:
    print("Los números no pueden ser iguales ")
if n1>n2:
        while n2<n1:
            n2+=1
            cont+=1
        print(f"El número menor es el {nc2} y entre ellos existen {cont} números enteros")
else:
    while n1<n2:
        n1+=1
        cont+=1
    print(f"El número menor es el {nc} y entre ellos existen {cont} números enteros")