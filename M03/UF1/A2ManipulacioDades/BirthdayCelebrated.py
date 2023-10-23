"""

Rubén Blas Lario

12/09/2023

ASIXc M03 UF1 A2

Descripció: BirthdayCelebrated

Digues si una persona ha celebrat l'aniversari enguany.  Suposarem les variables següents:

diaAniversari

mesAniversari

diaActual

mesActual

Fuente: https://docs.python.org/3/library/datetime.html
"""
import datetime
from datetime import datetime as dt
# Obtiene la fecha actual
diaActual, mesActual = dt.now().day, dt.now().month

# Define las variables del cumpleaños
diaAniversario, mesAniversario = int(input("¿Qué día es tu cumpleaños? ")), int(input("¿Qué mes es tu cumpleaños? "))


# Compara las variables
if diaAniversario == diaActual and mesAniversario == mesActual:
    print("¡Felicidades, capo!")
elif mesAniversario < mesActual or (mesAniversario == mesActual and diaAniversario < diaActual):
    print("El cumpleaños ya pasó.")
else:
    print("El cumpleaños aún no ha llegado.")


