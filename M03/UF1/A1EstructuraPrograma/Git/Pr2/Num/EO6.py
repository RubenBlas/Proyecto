"""
EOP 6
Com farieu un print del literal  ? “I a poder ser de color verd”

Correcto, en sistemas Unix (como Linux o macOS), puedes cambiar el color del texto en la consola utilizando códigos de escape ANSI. Estos códigos de escape permiten controlar el formato del texto, incluido el color. Aquí tienes algunos ejemplos de cómo cambiar el color del texto utilizando códigos de escape ANSI:

Texto rojo:
python
Copy code
print("\033[91mTexto en rojo\033[0m")
Texto verde:
python
Copy code
print("\033[92mTexto en verde\033[0m")
Texto amarillo:
python
Copy code
print("\033[93mTexto en amarillo\033[0m")
Texto azul:
python
Copy code
print("\033[94mTexto en azul\033[0m")
Texto morado:
python
Copy code
print("\033[95mTexto en morado\033[0m")
Texto cian:
python
Copy code
print("\033[96mTexto en cian\033[0m")
Texto blanco:
python
Copy code
print("\033[97mTexto en blanco\033[0m")
En estos ejemplos, \033[91m y \033[0m son códigos de escape ANSI que establecen el color del texto en rojo y luego lo restauran a su estado original. Puedes cambiar el número dentro de los corchetes para seleccionar diferentes colores. El 0 al final restablece el formato del texto al estado predeterminado.
"""
print("\033[92mI a poder ser de color verd\033[0m")

