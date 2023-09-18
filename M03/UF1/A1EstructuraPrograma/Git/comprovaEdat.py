"""

Javier Amaya Boira

12/09/2023

ASIXc M03 UF1 A1

Descripció: Exemple dels apunts

El programa que realitzarem és el següent: Programa que demani l'edat i digui si és major d'edat. Després de realitzar l'anàlisi i el disseny realitzem un pseudocodi com aquest:

Procés major_edat

Definir edat com a sencer;

Escriure "Digues-me la teva edat:";

Llegir edat;

Si edat>=18 Llavors

Escriure "Ets major d'edat";

FinSi

Escriure "Programa acabat";

FinProceso
"""

# Programa que demana l'edat i diu si ets major d'edat.

edat=int(input("Quina edat tens?"))

if edat>=18:
    print("Ets major d'edat")

print("Programa Finalitzat")