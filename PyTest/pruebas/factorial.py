def factor():
    num=int(input("Dame un numero para hacerle el factoria: "))
    while num<0:
        num=int(input("Dame otro numero para hacerle el factoria: "))
    cont=num
    inicio=f"Tu {num}! => "
    guarda=str()
    while num>1:
        guarda+=str(num)
        num-=1
        cont*=num
        guarda+=" * "
    return inicio,guarda+"1 =",cont
print(factor())