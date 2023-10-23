"""

Rubén Blas Lario

12/09/2023

ASIXc M03 UF1 PR2

Descripció: E4. WorkingAge (2 punts)


 (2 punts)
Escriu un programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar, l'edat mínima per treballar legalment és 16 i suposarem l'edat màxima als 65.

"""

import math

# Solicitar el diámetro de la pizza al usuario
diametro = float(input("Ingrese el diámetro de la pizza en centímetros: "))

# Calcular el radio (la mitad del diámetro)
radio = diametro / 2

# Calcular la superficie de la pizza
superficie = math.pi * (radio ** 2)

# Imprimir la superficie de la pizza
print(f"La superficie de la pizza es {superficie:.2f} centímetros cuadrados")
