"""

Rubén Blas Lario

12/09/2023

ASIXc M03 UF1 PR2

Descripció: E4. WorkingAge (2 punts)


 (2 punts)
Escriu un programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar, l'edat mínima per treballar legalment és 16 i suposarem l'edat màxima als 65.

"""
Edad = int(input("Edad?"))
Emin = 16
Emax = 65

if Emin <= Edad <= Emax:
    print("A trabajar!")
else:
    print("Tu no puedes trabajar")
