# Un sistema digital restringido solicita al usuario ingresar un nombre de usuario y una
# contraseña. Si ambos coinciden exactamente con los valores esperados ('admin' y '1234'), se
# debe mostrar 'Acceso concedido'. En caso contrario, mostrar 'Acceso denegado'. Crea el
# algoritmo para esta validación.

usuario = input("ingrese el usuario:")

contraseña = input("ingrese la contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("acceso concedido")
else:
    print("acceso denegado")

