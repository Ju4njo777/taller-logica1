# Desarrolla un algoritmo que reciba una nota numérica entre 0.0 y 5.0 y muestre la
# equivalencia cualitativa según la siguiente escala: - 4.5 a 5.0 → 'Excelente' - 4.0 a 4.4 → 'Sobresaliente' - 3.0 a 3.9 → 'Aceptable' - 2.0 a 2.9 → 'Insuficiente' - 0.0 a 1.9 → 'Deficiente'
# Asegúrate de validar que la nota esté dentro del rango permitido.

# definimos la variable a analizar
nota = float(input("Ingrese la nota, recuerde que es entre 0.0 y 5.0: "))

if nota < 0 or nota > 5:
    print("nota fuera de rango")
elif nota >= 4.5:
    print("Excelente")
elif nota >= 4.0:
    print("Sobresaliente")
elif nota >= 3.0:
    print("aceptable")
elif nota >= 2.0:
    print("insuficiente")
else:
    print("deficiente")
