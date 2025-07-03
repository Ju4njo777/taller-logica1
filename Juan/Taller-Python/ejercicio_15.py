# Crea un algoritmo que reciba tres valores numéricos que representan los lados de un
# triángulo. Primero debe verificar si los lados forman un triángulo válido (la suma de dos
# lados debe ser mayor al tercero). Si es válido, clasifica el triángulo como: - Equilátero (tres lados iguales) - Isósceles (dos lados iguales) - Escaleno (ningún lado igual).

a = float(input("Ingrese el primer lado: "))
b = float(input("Ingrese el segundo lado: "))
c = float(input("Ingrese el tercer lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("triangulo equilatero")
    elif a == b or a == c or b == c:
        print("triangulo isosceles")
    else:
        print("Triangulo escaleno")
else:
    print("no es un triangulo valido")
