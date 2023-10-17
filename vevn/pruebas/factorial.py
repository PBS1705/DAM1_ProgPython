
def factorial():
    num=int(input("Dame un numero para hacerle el factoria: "))
    while num<0:
        num=int(input("Dame otro numero para hacerle el factoria: "))
    cont=num
    while num>1:
        num-=1
        cont*=num
    print(f"Su factorial es : {cont}")
