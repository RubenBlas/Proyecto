"""

Rubén Blas Lario

12/09/2023

ASIXc M03 UF1 PR2

Descripció: E5. Encript12345 (2 punts)


Demana una paraula per teclat i mostrar-la per pantalla, canviar les vocals per als numèrics 1, 2, 3, 4 o 5.
Tenint en compte, que la lletra a i A és l'1, consecutivament fins a la lletra u i U que és el 5.

"""


#Demana una paraula
palabra = input("inserte una palabra")



for letra in palabra:
    if letra in "aeiouAEIOU":
        posicion = "aeiouAEIOU".index(letra)
        letra = "1234512345"[posicion]


print(palabra)