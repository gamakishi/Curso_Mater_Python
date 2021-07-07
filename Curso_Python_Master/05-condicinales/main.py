"""
#Condicional IF
SI se cumple esta condicion:
	Ejecuta grupo de instrucciones
SI NO:
	Se ejecutan otro grupo de instrucciones

if condicion:
	instrucciones
else:
	otras instrucciones

# operadores de comparacion
==igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

"""
# Ejemplo 1
print("########## EJEMPLO 1 ##########")
color = "verde"

#color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
	print("EnHoraBuena")
	print("El color es ROJO")
	pass
else:
	print("Color Incorrecto !!")
	pass

print("########## EJEMPLO 2 ##########")

year = 2020
# year = int(input("en que anio estamos"))
if year >= 2021:
    print("estamos de 2021 en adelante")
    pass

else:
    print("estamos en un anio anterior a 2021")
    pass


print("########## EJEMPLO 3 ##########")

nombre = "Ovidio Urias"
ciudad = "Barcelona"
coninente = "Europa"
edad = 55
mayorida_edad = 18

if edad >= mayorida_edad:
    print(f"{nombre} es mayor de edad !!")
    if coninente != "Europa":
        print("El usuario no es europeo")
        pass
    else:
    	print(f"Es europeo y de la ciudad {ciudad}")
    pass
else:
    print(f"{nombre} no es mayor de edad")
    pass
