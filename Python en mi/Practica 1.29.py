#lee nom,edad
#si nom=" " hacer
#   nom="Desconocido"
#sino si edad<0 or edad>125
#      escribe Edad no valida
#sino
#vida=125-edad
#escribe Te llamas nom y tienes edad años, te quedan aún vida años por cumplir"
nom=input("Dime tu nombre: ")
edad=int(input("Dime tu edad: "))
if nom==" ":
    nom="Desconocido"
else:
    if edad<0 or edad>125:
        print("Edad no valida")
    else:
        vida=125-edad
        print(f"Te llamas {nom} y tienes {edad} años, te quedan aún {vida} años por cumplir")