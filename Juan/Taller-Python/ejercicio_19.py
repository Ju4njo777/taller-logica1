# Una cafetería universitaria tiene un menú fijo con tres platos principales, cada uno asignado
# a un número: - 1 → 'Desayuno completo' ($8.000) - 2 → 'Almuerzo ejecutivo' ($12.500) - 3 → 'Cena ligera' ($10.000)
# Escribe un algoritmo que muestre el menú, permita al usuario seleccionar una opción e
# indique el nombre del plato y su precio. Si el número ingresado no corresponde a ninguna
# opción, mostrar: 'Opción no válida'.


print("1 - 'Desayuno completo' ($8.000)")
print("2 - 'Almuerzo ejecutivo' ($12.500)")
print("3 - 'Cena ligera' ($10.000)")

opcion = int(input("Selecciona una opcion del menú"))

if opcion == 1:
    print("1 - 'Desayuno completo' ($8.000)")
elif opcion == 2:
    print("2 - 'Almuerzo ejecutivo' ($12.500)")
elif opcion == 3:
    print("3 - 'Cena ligera' ($10.000)")
else:
    print("no es una opcion valida")
