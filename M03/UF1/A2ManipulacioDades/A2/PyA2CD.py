"""

   Rubén Blas Lario

   05/10/2022

   ASIXc M03 UF1 A2

   Descripció:

   CalculateDiscount
   Llegeix el preu original i el preu actual i imprimeix el discompte.

"""
PreuOriginal= float(input("Añade el precio original "))
PreuActual=float(input("Añade el precio Actual "))
Descuento = (100 - PreuActual / PreuOriginal * 100)
print("Su compra tiene un descuento del " + str(round(Descuento, 1)) + "%.")
