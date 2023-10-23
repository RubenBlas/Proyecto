"""
Ruben Blas Lario, Iker Blazquez Valverde, Oscar Bravo Lòpez
09/10/2023
Asixc 1A M01 UF1 Pr2
Escriu un programa que llegeixi 5 enters. El primer i el segon creen un rang,
el tercer i el quart creen un altre rang. Mostra True si el cinquè valor,
està comprès dins els dos rangs, si no False. (Els extrems dels rangs inclosos)
"""
#Variables
v1= int(input("Insereix el primer número per fer el primer rang:"))
v2= int(input("I el segón:"))
v3= int(input("Ara farem el segon rang, dona'm el primer número:"))
v4= int(input("I el següent és?:"))
v5= int(input("Insereix el número per veure si es troba en els rangs assignats:"))

#Construcció de rangs

if v5>=v1 and v5<=v2 or v5>=v3 and v5<=v4:
    print("True")
else:
    print("False")