"""
Ruben Blas Lario
28/09/2022
ASIXc M03 UF1 A2
Descripio: HowManyDaysInMonth

Demanar un enter a l'usuari que indica el número de més
Retorna el nombre de dies del mes.

Input
1

Output
31

IMPORTANT: No es poden fer servir mòduls ni funcions com ara Datetime
 """

#variables iniciales
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
# 28 o 29 depende del año bisiesto
mes = int(input("Dime un número del 1 al 12: "))

if 1 <= mes <= 12:
    print(f"El mes {mes} tiene {dias[mes - 1]} días.")
else:
    print("Número de mes inválido. Por favor, ingresa un número del 1 al 12.")

