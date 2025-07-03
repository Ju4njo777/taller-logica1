# En una tienda de tecnología se aplican descuentos por el valor total de la compra: - Sin descuento si es menor a $100.000 - 5% si está entre $100.000 y $200.000 - 10% si supera los $200.000
# Crea un algoritmo que reciba el valor de la compra y muestre qué porcentaje de descuento
# aplica. 

valor_compra = float(input("ingrese el valor total de la compra: "))
if valor_compra < 100000:
    print("sin descuento")
elif 100000 <= valor_compra <= 200000: 
    print("aplica un 5% de descuento") 
else:
    print("aplica un 10% de descuento")
           
