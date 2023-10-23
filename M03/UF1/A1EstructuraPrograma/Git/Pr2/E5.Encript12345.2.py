"""

Rubén Blas Lario

12/09/2023

ASIXc M03 UF1 PR2

Descripció: E5. Encript12345 (2 punts)


Demana una paraula per teclat i mostrar-la per pantalla, canviar les vocals per als numèrics 1, 2, 3, 4 o 5.
Tenint en compte, que la lletra a i A és l'1, consecutivament fins a la lletra u i U que és el 5.

"""

cadena = input("Dime una palabra")
nueva_cadena = ""

for letra in cadena:
    if letra in "aeiouAEIOU":
        # Obtén la posición de la vocal en "aeiouAEIOU"
        posicion = "aeiouAEIOU".index(letra)
        # Obtén el número equivalente en "1234512345"
        numero_correspondiente = "1234512345"[posicion]
        nueva_cadena += numero_correspondiente
    else:
        nueva_cadena += letra