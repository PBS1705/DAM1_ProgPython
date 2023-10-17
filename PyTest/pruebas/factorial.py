def factorial(num):
    num=int(input("Dame un numero para hacerle el factoria: "))
    while num<0:
        num=int(input("Dame otro numero para hacerle el factoria: "))
    cont=num
    while num>1:
        num-=1
        cont*=num
    return cont
