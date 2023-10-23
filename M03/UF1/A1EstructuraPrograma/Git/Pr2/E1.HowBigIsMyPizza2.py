"""
Ruben Blas Lario, Iker Blazquez Valverde, Oscar Bravo Lòpez
09/10/2023
Asixc 1A M01 UF1 Pr2
Demanar el diàmetre d'una pizza rodona i imprimeix la seva superfície.
Pots usar Math.PI per escriure el valor de Pi.
"""
#Variables

import math
pi=math.pi
diametrePizza= int(input("Dona'm el diametre de la pizza per trobar l'àrea:"))

#Operació

calcularArea= diametrePizza*pi

#utilitzo la comanda round(0,2) per rodonar a dos decimals.

print("El volum de la pizza és",round(calcularArea,2),"m^3")