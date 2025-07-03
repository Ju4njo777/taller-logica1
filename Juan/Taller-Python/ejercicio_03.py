# Para garantizar la seguridad, una montaña rusa permite el ingreso solo a personas que
# tengan una edad igual o mayor a 12 años y una estatura igual o mayor a 1.40 metros. Crea
# un algoritmo que reciba la edad y estatura de una persona y determine si puede subir o no a
# la atracción. 

# Solicitar datos al usuario
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura en metros: "))

if edad >= 12 and estatura >= 1.40:
    print("puedes subir")
else:
    print("no puedes montarte a la montaña rusa")
