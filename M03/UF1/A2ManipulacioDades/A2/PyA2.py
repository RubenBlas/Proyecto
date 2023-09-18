# Import math Library
import math

# Valores Estaticos
Precio = 5.6
PrecioOfeta = 4.48
Unidades = 2
DiametroP = 20
PizzaArea = (DiametroP / 2) ** 2 * (math.pi)


# Calculo de Valores
PrecioTotal = Precio * Unidades
Descuento = (100 - PrecioOfeta / Precio * 100)

# Resultado
print("Gracias por comprar " + str(Unidades) + "xPizzas, el precio total equivale a " + str(PrecioTotal) + "€.")
print("En su proxima compra tendra una oferta del " + str(round(Descuento, 1)) + "%.")
print("Cada una de nuestras pizzas tiene un tamaño total de " + str(round(PizzaArea)) + " cm²!")


Longitud =