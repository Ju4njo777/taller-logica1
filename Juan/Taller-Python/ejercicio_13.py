# Un año es bisiesto si es divisible entre 4, pero no entre 100, excepto si también es divisible
# entre 400. Escribe un algoritmo que reciba un año y determine si es bisiesto o no, aplicando
# estas reglas de forma precisa.

year = int(input("ingrese un año: "))

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("Es bisiesto")
else:
    print("no es bisiesto")
