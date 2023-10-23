def const():
   
    n=int(input("Dime un numero : "))
    sumar=0
    nom=str()
    while n!=0:
        sumar=float((n*(n+1))/2)
        n=n-1
        nom +=str(sumar)
        nom+=str("/")
    return nom

print(const())