"""
Ruben Blas Lario
28/09/2022
ASIXc M03 UF1 A2
Descripio: WillWeFightForTheCookies

Introdueix el número de persones i el número de galetes.

Si a tothom li toquen el mateix número de galetes imprimeix "Let's Eat!", sinó imprimeix "Let's Fight"
 """
#Persones & Cookies
P = float(input("CUANTOS QUIEREN GALLETAS?!"))
C = float(input("CUANTAS GALLETAS?!"))
#Divisiones y comparacion
if P/C == P//C:
    #Muestra en pantalla
    print("Let's Eat!")