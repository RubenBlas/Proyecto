"""

   Rubén Blas Lario

   04/10/2022

   ASIXc M03 UF1 A2

   Descripció:

   Dades booleanes

   IsLegalAge
L'usuari escriu un enter amb la seva edat i s'imprimeix True si és major d'edat, i False en qualsevol altre cas.

"""

print("Inserte su edad")
Edad = input()
if int(Edad) < 18:
    print("False")
else:
    print("True")

#O

print(bool(int(Edad) >= 18))





