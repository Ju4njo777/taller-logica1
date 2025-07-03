# Un proveedor de servicios de Internet desea implementar una herramienta que clasifique el
# servicio que tiene un usuario. Se debe ingresar la velocidad del plan en Mbps y mostrar:
# - 'Muy lenta' si es menor a 10 Mbps - 'Aceptable' si es entre 10 y 30 Mbps - 'Buena' si es entre 31 y 100 Mbps - 'Alta velocidad' si es mayor a 100 M

velocidad = float(input("ingrese la velocida de su plan en Mbps: "))

if velocidad < 10: 
    print("muy lenta")
elif 10 <= velocidad <= 30: 
    print("aceptable")
elif 31 <= velocidad <= 100: 
    print ("buena")
else: 
    print("alta velocidad")
           
