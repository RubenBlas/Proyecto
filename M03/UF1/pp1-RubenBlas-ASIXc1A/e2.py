"""

   Rubén Blas Lario

   25/10/2022

   ASIXc M03 UF1 pp1

   Descripció: Exercici 2

    Crear un programa que sigui capaç de calcular la nota final de la UF2
    del mòdul 03 del Cicle de Grau Superior d'Administració de Sistemes Informàtics
    en Xarxa (CFGS ASIX). El programa només haurà de fer el càlcul per a 1 estudiant,
    i mostra'ls per pantalla. Les notes de cadascun dels estudiants s'haurà de
    demanar per pantalla. La fórmula de la UF2 és:

        QUF2 =1*RA1 a on  RA1= 0,15*Pt1.1 + 0,15*Pr1.2+0,70*Pp1.

    El pes de cada IA està fitxat a l'inici de curs per a no ser modificat.
    La nota final de les UF's es calcula amb 2 decimals.

"""

# Valores Input
Pt11 = float(input("Inserta la nota de Pt 1.1: "))
Pr12 = float(input("Inserta la nota de Pr 1.2: "))
Pp1 = float(input("Inserta la nota de Pp 1: "))

# Calculo de Valores
RA1 = float(0.15*Pt11+0.15*Pr12+0.7*Pp1)
QUF2 = round(RA1,2)

# Muestra en pantalla
print("La nota final del alumne és... "+ str(QUF2))




























# Extra
if QUF2 >= 5:
    print("Cada vez sois menos usuarios a los que torturar (<T-T)>")


