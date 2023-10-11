def estaenmilista(lista,num):
    encontrado= num in lista 
    return encontrado


milist=[1,2,3,4,5,6,7,8]
minum=int(input("Dame un num "))
if (estaenmilista(milist,minum)== True ):
    print("Cacao")
else:
    print("Tonto")