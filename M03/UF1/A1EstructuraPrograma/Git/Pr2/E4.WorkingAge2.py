"""

Rubén Blas Lario

12/09/2023

ASIXc M03 UF1 PR2

Descripció: E4. WorkingAge (2 punts)


 (2 punts)
Escriu un programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar, l'edat mínima per treballar legalment és 16 i suposarem l'edat màxima als 65.

"""
"""
Ruben Blas Lario, Iker Blazquez Valverde, Oscar Bravo Lòpez
09/10/2023
Asixc 1A M01 UF1 Pr2
descripcion:Escriu un programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar, l'edat mínima per treballar legalment és 16 i suposarem l'edat màxima als 65.
"""
#variables
Edad=int(input("cuantos años tienes?\n"))
#codigo
if Edad>0 and Edad<150:
    if Edad>=16 and Edad<=65:
        print("puedes trabajar")
    elif Edad<16:
        print("eres muy joven")
    else:
        print("eres muy mayor")
else:
    print("edad invalida")