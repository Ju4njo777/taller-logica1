# Crea un algoritmo que reciba tres números enteros y determine cuál es el mayor. Si dos o
# más son iguales y mayores, deberá informar que hay un empate entre esos valores. Por
# ejemplo: “El mayor es 15” o “Empate entre 22 y 22”.

a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
c = int(input("ingrese el tercer numero: "))

if a > b and a > c:
    print(f"el mayor es {a}")
elif b > a and b > c:
    print(f"el mayor es {b}")
elif c > a and c > b:
    print(f"El mayor es {c}")
elif a == b and a > c:
    print(f"Hay un empate entre {a} y {b}")
elif a == c and a > b:
    print(f"Hay un empate entre {a} y {c}")
elif b == c and b > a:
    print(f"Hay un empate entre {b} y {c}")
elif a == b and b == c:
    print(f"todos son iguales {a}")
