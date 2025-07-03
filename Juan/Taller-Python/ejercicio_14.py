# Una empresa categoriza a sus empleados según dos variables: evaluación de rendimiento
# (nota entre 0.0 y 5.0) y número de proyectos finalizados. Para ser considerado “Empleado
# destacado”, debe tener nota ≥ 4.5 y al menos 3 proyectos entregados. Si cumple solo uno de
# los dos criterios, es “Empleado competente”. Si no cumple ninguno, es “Empleado en
# formación”. Construye el algoritmo correspondiente.

nota = float(input("ingrese la nota de desempeño del colaborador (entre 0.0 y 5.0): "))
proyectos = int(input("Ingrese la cantidad de proyectos finalizados"))

if nota >= 4.5 and proyectos >= 3:
    print("Empleado destacado")
elif nota >= 4.5 or proyectos >= 3:
    print("Empleado competente")
else:
    print("Empleado en formacion.")
