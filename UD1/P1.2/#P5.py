#P5
print("Dime el importe del producto :")
inp=float(input())
print("Dime si es tipo 1 (21%),2(10%),3(4%)")
tip=int(input())   
if(tip==1):
    print("Tu producto con iva: ",inp=+(inp*0.21))
else:
    if(tip==2):
       print("Tu producto con iva: ",inp=+(inp*0.1))
    else:
     if(tip==3):
        print("Tu producto con iva: ",inp=+(inp*0.04))
     else:
        print("ERROR")
