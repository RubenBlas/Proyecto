"""
Rubén Blas Lario
31/01/2023
ASIXc M03 UF2 A1
Descripció: Yakisoba (焼きそば)
Implementar en Python l'algoritme per a preparar els fideus Yakisoba.

Fer només el nivell de descomposició 1

"""
from time import sleep



# region Declaració de Funcions ----------

def recopilar_ingredients():

   print("Comprar al supermercat")

   sleep(1)

   print("Disposar-los sobre el marbre")

   sleep(1)


def Cuinar_tallarines():

   Preparar_aigua()

   sleep(1)

   print("Bullir tallarines")

   sleep(1)

   print("Escórrer tallarines")

   sleep(1)

   print("Deixar-les preparades")

   sleep(1)


def Preparar_aigua():


   print("Escalfar aigua")

   sleep(1)

   print("Posar-hi sal")

   sleep(1)


def Cuinar_pastanagues():


   print("Tallar pastanagues")

   sleep(1)

   Fregir_pastanagues()

   sleep(1)

   print("Deixar pastanagues preparades")

   sleep(1)

def Fregir_pastanagues():

   print("Preparar paella per fregir")

   sleep(1)

   print("Rossejar pastanagues")

   sleep(1)

   print("Netejar oli de paella")

   sleep(1)

def Cuinar_cebes():

   print("Tallar cebes")

   sleep(1)

   Fregir_cebes()

   sleep(1)

   print("Deixar cebes preparades")

   sleep(1)


def Fregir_cebes():


   print("Preparar paella per fregir")

   sleep(1)

   print("Rossejar cebes")

   sleep(1)

   print("Netejar oli de paella")

   sleep(1)


def Preparació_final():


   print("Barrejar ingredients amb salsa yakitori")

   sleep(1)

   Saltar_ingredients()

   sleep(1)

   print("Deixar llest per servir")

   sleep(1)


def Saltar_ingredients():


   print("Preparar paella per saltar")

   sleep(1)

   print("Cuinar remenant ingredients")

   sleep(1)



# endregion



# region INICI: Preparar fideus Yakisoba

recopilar_ingredients()
Cuinar_tallarines()
Cuinar_pastanagues()
Cuinar_cebes()
Preparació_final()

# endregion

