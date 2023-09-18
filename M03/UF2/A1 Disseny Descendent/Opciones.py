from datetime import date
from datetime import datetime
from time import sleep


def obteOpcio():
    print("1.- Primera opcio")
    print("2.- Millor opcié")
    print("3.- Jo triaria aquesta")
    print("4.- La millor opcié")
    print("5.- Sortir")
    return int(input("Selecciona una opcio:"))

opcio = obteOpcio()
def opcioPrimera():
    print("Primera opcio")
    sleep(1)
def opcioMillor():
    print("Millor opcio")
    sleep(1)
def opcioJoTriariaAquesta():
    print("Jo triaria aquesta opcio")
    sleep(1)
def opcioLaMillor():
    print("La millor opcio")
    sleep(1)
def tractarError(missatge):
    print("Ha hagut algun error")
    sleep(1)
def tractamentFinal():
    print("Precesan")
    sleep(1)

#Programa principal

opcio = obteOpcio()

# Mentre no ens demanin sortir, atenem a L'opcid triada
while opcio != 5:...

#Tractament final

tractamentFinal()


# Mentre no ens demanin sortir, atenem a L'opcio triada
while opcio != 5:
    if opcio < 1 or opcio > 4:
            tractarError("opcid no valida")
    else:
        if opcio == 1:
            opcioPrimera()
        elif opcio == 2:
            opcioMillor()
        elif opcio == 3:
            opcioJoTriariaAquesta()
        elif opcio == 4:
            opcioLaMillor()
    #tornem a presentar el menu i a Llegir L'opcio triada
    opcio = obteOpcio()
    # Tractament final
tractamentFinal()

def tractamentFinal():
    for i in range (5):
        print(".",end="")
        sleep(1)
    print("See you")

