
# Una empresa de energía desea categorizar a sus clientes en tres rangos tarifarios según el
# consumo mensual de kilovatios-hora (kWh): - Menor a 100 kWh → 'Estrato bajo' - Entre 100 y 200 kWh → 'Estrato medio' - Mayor a 200 kWh → 'Estrato alto'
# Desarrolla un algoritmo que reciba el consumo y muestre la categoría correspondiente. 


consumo = float(input("Ingrese el consumo mensual en kWh: "))


if consumo < 100:
    print("Estrato bajo")
elif 100 <= consumo <= 200:
    print("Estrato medio")
else:
    print("Estrato alto")
