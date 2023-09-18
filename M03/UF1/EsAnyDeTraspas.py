"""
Rubén Blas Lario
18/10/2022
ASIXc M03 UF1 A3
Descripció: EsAnyDeTraspas
El programa ha de mostrar un dels dos missatges possibles,
 que són Any de traspàs o Any comú, segons el valor ingressat.
 (Només llegir el número d'any, per facilitar l'algoritme)
"""

print("Entrada de mostra:")

Any = input()

if float(int(Any)/4) - int(int(Any)/4) == 0 or float(int(Any)/400) - int(int(Any)/400) == 0:
    print("Any Traspàs")
else:
    print("Any Comú")

