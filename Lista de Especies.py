import pandas as pd
from numpy import *

class Species:
  #Leyendo el csv y dandole una variable
  datos=pd.read_csv('Index of Species.csv',header=0)
  #La columna especie se ha metida en esta variable
  DfSpecies=datos['Species']
  DfFamily=datos['Family']
  DfCategory=datos['']
  DfGender=datos['']


  def Search_Specie():
    ListofSpecies=[]
    especie=input("Ingrese el nombre de la especie que desee buscar: ")
    ListofSpecies.append(especie)

  def Report():
    pass
  
def Menu():
    while True:  # Bucle infinito para mantener el menú activo
        print("\n***** MENU *******")
        print("1. Buscar Especie")
        print("2. Crear Reporte")
        print("3. Salir")
        try:
            op = int(input("Elija una opción: \n"))
            match op:
                case 1:
                    Species.Search_Specie()
                case 2:
                    Species.Report()
                case 3:
                    print("Saliendo del programa.....")
                    break  # Rompe el bucle y termina el programa
                case _:
                    print("Opción inválida. Vuelva a intentarlo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
Menu()