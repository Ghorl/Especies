import pandas as pd #43175 rows en lista iniciara desde 0 hasta 42174
from numpy import *

class Species:
  
  def __init__(self):
  #Leyendo el csv y dandole una variable
   datos=pd.read_csv('Index of Species.csv',header=0)
   self.DfSpecies=datos['Species']
   self.ListofSpecies=[]

  def Search_Specie(self):
    especie=input("Ingrese el nombre de la especie que desee buscar: ")
    
    if especie in self.DfSpecies:
      print("Especie encontrada. Agruegada a la lista")
      self.ListofSpecies.append(especie)
    else:
       print("Especie no encontrada")

  def Report(self):
     columns=["Especie"]

def Menu():
    especies=Species()
    while True:
        print("\n***** MENU *******")
        print("1. Buscar Especie")
        print("2. Crear Reporte")
        print("3. Salir")
        try:
            op = int(input("Elija una opción: \n"))
            match op:
                case 1:
                    especies.Search_Specie()
                case 2:
                    especies.Report()
                case 3:
                    print("Saliendo del programa.....")
                    break  
                case _:
                    print("Opción inválida. Vuelva a intentarlo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
Menu()