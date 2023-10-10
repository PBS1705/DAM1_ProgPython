
#inicio
#lee numero,incremento,total
#fin crea lista desde numero hasta total
# escribe fin
#fin  
numero=int(input("Dime tu número: "))
incremento=int(input("De cuanto va ha ser el incremento: "))
total=int(input("Dime hasta donde tiene que llegar: "))
fin=list(range(numero-1,total+1))
fin=fin[numero:total:incremento]
print(fin)
   