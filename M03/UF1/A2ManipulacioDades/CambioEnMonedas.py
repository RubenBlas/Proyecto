# Pide la cantidad de billetes y monedas
billetes_500 = int(input("Número de billetes de 500 euros: "))
billetes_200 = int(input("Número de billetes de 200 euros: "))
billetes_100 = int(input("Número de billetes de 100 euros: "))
billetes_50 = int(input("Número de billetes de 50 euros: "))
billetes_20 = int(input("Número de billetes de 20 euros: "))
billetes_10 = int(input("Número de billetes de 10 euros: "))
billetes_5 = int(input("Número de billetes de 5 euros: "))
monedas_2 = int(input("Número de monedas de 2 euros: "))
monedas_1 = int(input("Número de monedas de 1 euro: "))
centimos_50 = int(input("Número de monedas de 50 céntimos: "))
centimos_20 = int(input("Número de monedas de 20 céntimos: "))
centimos_10 = int(input("Número de monedas de 10 céntimos: "))
centimos_5 = int(input("Número de monedas de 5 céntimos: "))
centimos_2 = int(input("Número de monedas de 2 céntimos: "))
centimos_1 = int(input("Número de monedas de 1 céntimo: "))

# Calcula el total en euros y centavos
total_euros = (billetes_500 * 500 + billetes_200 * 200 + billetes_100 * 100 + billetes_50 * 50 +
               billetes_20 * 20 + billetes_10 * 10 + billetes_5 * 5 + monedas_2 * 2 + monedas_1)
total_centavos = (centimos_50 * 50 + centimos_20 * 20 + centimos_10 * 10 + centimos_5 * 5 +
                  centimos_2 * 2 + centimos_1)

# Convierte los centavos en euros si es necesario
euros_totales = total_euros + total_centavos // 100
centimos_totales = total_centavos % 100

# Imprime el resultado
print(f"Total: {euros_totales:.2f} euros y {centimos_totales} céntimos.")
