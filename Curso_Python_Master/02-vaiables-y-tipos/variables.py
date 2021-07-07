"""
Una variables es un contenedor de informacion
que dentro guarda un dato, se pueden crear
muchas variables y cada una tenga un dato distinto.
"""


# crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "Con Victor Robles"
numero = 45
decimal = 6.7

#mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------------------")

# Sustituri el valor de algunas variables / reasignando valores
numero = 77
decimal = 8.9

print(numero)
print(decimal)

print("------------------------------")

# Concatenacion

nombre = "Ovidio"
apellidos = "Urias"
web = "ovidio.com"

print(nombre +" "+ apellidos + " - "+ web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} i mi web es: {}".format(nombre, apellidos, web))
print(nombre, apellidos, web)