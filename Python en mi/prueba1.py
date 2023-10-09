y=10
def suma(num1,num2):#funcion que puedes llamar 
        """Suma todo"""
        return num1 - num2
minum=(int(input("Dame un num ")))
minum2=(float(input("Dame un num ")))
print(f"hola mi rey {suma (minum,minum2)}")

#P21

cuant=int(input("¿Cuántas palabras tiene su frase?"))
fra=input("Dime la frase: ")
part=fra.split(" ")
for i in range(cuant):
    partit=part[cuant]
    cuant=cuant-1
    print(partit)