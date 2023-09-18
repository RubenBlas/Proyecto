"""
Rubén Blas Lario
18/10/2022
ASIXc M03 UF1 A3
Descripció: Tipus de dades Seqüència  i Diccionari
Donada una tupla de nombres sencers (sense decimals). Fer un programa de càlcul de temperatures.
Primer proveu si funciona usant aquesta tupla

"""



gener = (1, 12, 4, -5, 7, 3, 2,
        9, -6, 7, 8, 2, 14, -7,
        5, 13, 12, 4, 6, -7, 1,
        12, 4, -2, 3, 5, 2, 7,
        -2, 8,-15)

sgener = sorted(gener)
print("Temperatures Minimes Gener = ", sgener[0])
print("Temperatures Maximes Gener = ", sgener[30])

febrer = (4, 15, 7, -8, 10, 6, 5,
        12, -3, 10, 11, 5, 17, -4,
        8, 16, 15, 7, 9, -4, 4,
        15, 7, 1, 6, 8, 5, 10,
        1, 11,-12)

sfebrer = sorted(febrer)
print("Temperatures Minimes Febrer = ", sfebrer[0])
print("Temperatures Maximes Febrer = ", sfebrer[30])
mmarç = 0
for x in març:
        mmarç = mmarç + x
print("Temperatures Maximes Març = ", mmarç/30)


març = (6, 17, 9, 0, 12, 8, 7,
        14, -1, 12, 13, 7, 19, -2,
        10, 18, 17, 9, 11, -2, 6,
        17, 9, 3, 8, 10, 7, 12,
        3, 13,-10)

smarç = sorted(març)
print("Temperatures Minimes Març = ", smarç[0])
print("Temperatures Maximes Març = ", smarç[30])
mmarç = 0
for x in març:
        mmarç = mmarç + x
print("Temperatures Maximes Març = ", mmarç/30)
