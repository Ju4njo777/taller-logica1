# Implementa un cajero automático que ofrezca 3 opciones:
# 1. Consultar saldo
# 2. Retirar dinero
# 3. Consignar dinero
# Usa 'switch' para el menú y 'if' para validar que el retiro no exceda el saldo. Muestra el saldo
# actualizado tras cada operación.

saldo = 1000000

print("1 - Consultar Saldo")
print("2 - Retirar dinero")
print("3 - Consignar dinero")

opcion = int(input("Selecciona una opcion: "))

if opcion == 1:
    print(f"Saldo Actual: {saldo}")
elif opcion == 2:
    retiro = int(input("ingrese la cantidad a retirar: "))
    if retiro <= saldo:
        saldo -= retiro
        print(f"Retiro exitoso, tu nuevo saldo es {saldo}")
    else:
        print("fondos insuficientes")
elif opcion == 3:
    consignacion = int(input("Ingrese la  cantidad a consignar"))
    saldo += consignacion
    print(f"Consignacion exitosa, su nuevo saldo es {saldo}")
else:
    print("opcion invalida")
