#P1
nom=input("Escribe tu nombre : ")
print("Hola, ",nom)
#P2
print("Horas de trabajo :")
horas=int(input())
print("Coste por hora:")
Coste=int(input())
Import=0
Import=horas*Coste
print("Importe total:",Import)
#P3
ancho = 17
alto = 12.0
ancho / 2
ancho // 2
alto / 3
1 + 2 * 5
#Resultado : ancho=float ,ancho=float , alto=float , int
#P4
print("Dime los grados Celsius y te los paso Fahrenheit :")
Celsi=float(input())
fahren= (Celsi * 9/5)+32
print("La temperatura en Fahrenheit",fahren) 
#P5
print("Dime el importe del producto :")
inp=float(input())
print("Dime si es tipo en % :")
tip=int(input())   
final=inp*(1+tip/100)
print("El precio final es :",final)


#P6
print("Dime el precio final :")
pre=float(input())
iva=pre/1.10

print("Precio sin IVA:",iva)

#P7
print("Dime tres numeros para sumar :")
prinum=float(input())
secnum=float(input())
trenum=float(input())
print(prinum+secnum+trenum)
#P8
print("Dime tres numeros para sumar :")
num=0
for x in range(3):
    num+=float(input())
print(num)
#P9
print(float(input("Primer num "))+float(input("Segundo num "))+float(input("Tercer num ")))

#P10

print(print(((3+2)/(2*5))**2))

#P11

print("Dime un numero :")
n=int(input())
sumar=0
for i in range(n):
   sumar=float((n*(n+1))/2)
   n=n-1
   print(sumar)

#P12

print("Dime un tu peso en Kg :")
Peso=float(input())
print("Dime un tu altura en M :")
Altu=float(input())
ICM=Peso/(Altu**2)
print("Tu índice de masa corporal es ",round(ICM,2))

#13

print("Dime el dividendo :")
num1=int(input())
print("Dime el divisor :")
num2=int(input())
print("Su resultado: ",num1//num2)
print("Su resto: ",num1%num2)

#usar el {:,2f}.format(variable) para coger 2 decimales y : coge todo.


