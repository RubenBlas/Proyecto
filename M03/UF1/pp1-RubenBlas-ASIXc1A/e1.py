"""

   Rubén Blas Lario

   25/10/2022

   ASIXc M03 UF1 pp1

   Descripció: Exercici 1

    S'ha creat un nou embàs, amb forma de piràmide quadrangular, per omplir-la d'aliments. Com ara: gelats, xocolates, o qualsevol altre aliment cremós
    Ens demanen, crear un programa que mostri per pantalla, l’àrea i el volum d’una piràmide quadrangular (de base quadrada) on l'alçada i la mida dels costats es llegeix del teclat.
    Les fórmules són les que es mostren a la imatge.

"""

#Importar math Library
import math

# Valores Input
L = float(input("Inserta la Longitud de la base piramidal: "))
h = float(input("Inserta la Altura de la piramide: "))

# Calculo de Valores
A = L*(L+(math.sqrt(4*h**2+L**2)))
V = L**2*h/3

# Muestra en pantalla
print("La àrea es igual a: "+str(A))
print("El volum es igual a: "+str(V))
