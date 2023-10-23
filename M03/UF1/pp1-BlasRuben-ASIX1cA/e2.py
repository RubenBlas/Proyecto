"""

   Rubén Blas Lario

   20/10/2023

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
Pt = float(input("Inserta la nota de Pt 1.1: "))
Pr = float(input("Inserta la nota de Pr 1.2: "))
Pp = float(input("Inserta la nota de Pp 1: "))

# Calculo de Valores
RA = float(0.15*Pt+0.15*Pr+0.7*Pp)
QUF = round(1*RA,2)

# Muestra en pantalla
print("La nota final del estudiante és... "+ str(QUF))




























# Extra
if QUF > 5:
    print("Cada vez sois menos usuarios a los que torturar (<T-T)>")
elif QUF < 5:
    print("Cada vez sois más usuarios a los que torturar (\ºUº)/")
else:
    print("Salvado por los pelos de un calvo ( -_-)")




