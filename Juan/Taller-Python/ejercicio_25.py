# Recibe una nota entre 0 y 5 y una letra entre A y F. - Si la nota es menor a 3, debe coincidir con una letra D o F - Si la nota es 3 o más, debe coincidir con una letra A, B o C
# Si hay inconsistencia entre número y letra, se muestra un mensaje de advertencia: 'Nota y
# letra no coinciden'.

nota = float(input("ingrese la nota (0 a 5): "))
letra = input("ingrese la letra (A a F): ").upper()

if nota < 0 or nota > 5:
    print("nota fuera de rango")
elif nota < 3:
    if letra == "D" or letra == "F":
        print("nota y letra son coherentes")
    else:
        print("nota y letra no coinciden, favor revisar")
else:
    if letra == "A" or letra == "B" or letra == "C":
        print("nota y letra son coherentes")
    else:
        print("nota y letra no coinciden, favor revisar")
