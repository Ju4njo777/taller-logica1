# Se necesita construir un programa que indique si un número tiene exactamente tres cifras.
# Esto se cumple si el número está entre 100 y 999, o entre -999 y -100. Crea un algoritmo
# que lo detecte y lo indique con un mensaje.

#definimos la variable que almacena el numero a validar.
numero = int(input("Ingresa un numero para verificar: "))

# debemos comparar los rangos para que se cumplan, recuerden que una comparacion de tipo and solo se cumple si las dos son True y una compatracion de tipo or solo se incumple si las dos son negativas.
if (numero >= 100 and numero <= 999) or (numero <= -100 and numero >= -999):
    print("El numero tiene exactamente 3 cifras")
else:
    print("El numero no cumple con el requisito.")
