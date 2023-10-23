#variables iniciales
cadena = input("Dime una palabra")
nueva_cadena = ""
i = 0  # Inicializa un índice para recorrer la cadena

while i < len(cadena):
    letra = cadena[i]
    
    if letra in "aeiouAEIOU":
        # Obtén la posición de la vocal en "aeiouAEIOU"
        posicion = "aeiouAEIOU".index(letra)
        # Obtén el número equivalente en "1234512345"
        numero_correspondiente = "1234512345"[posicion]
        nueva_cadena += numero_correspondiente
    else:
        nueva_cadena += letra
    
    i += 1  # Incrementa el índice para avanzar a la siguiente letra

print("La nueva cadena es:", nueva_cadena)