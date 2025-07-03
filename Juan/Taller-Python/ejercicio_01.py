#  Múltiplos de 3 y 5 – Clasificación numérica múltiple
# Un sistema numérico automatizado necesita clasificar números según su divisibilidad por 3,
# por 5, o por ambos. Escribe un algoritmo que reciba un número entero y muestre en
# pantalla uno de los siguientes mensajes: - “Es múltiplo de 3 y 5” - “Es múltiplo solo de 3” - “Es múltiplo solo de 5” - “No es múltiplo de 3 ni     

# solicitar al usuario un numero entero 

numero = int(input("ingresa un numero entero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("es multiplo de 3 y 5")
elif numero % 5 == 0:
    print("es multiplo solo de 3")
elif numero % 5 == 0:
    print("es multiplo solo de 5")
else:
    print("no es multiplo de 3 y de 5")
