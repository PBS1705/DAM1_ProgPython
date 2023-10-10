numero=int(input("Dime tu número: "))
incremento=int(input("De cuanto va ha ser el incremento: "))
total=int(input("Dime hasta donde tiene que llegar: "))
pan=list(range(numero,total))
tot=pan[numero:total:incremento]
print(tot)