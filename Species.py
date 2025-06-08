import pandas as pd 
from numpy import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Species:
  
  def __init__(self):
  #Leyendo el csv y dandole una variable
   self.datos=pd.read_csv('Index of Species.csv',header=0)
   self.List_of_Species=[]

  def Search_Specie(self):

    specie=input("Introduce the name of the specie to search: ")

    if specie in self.datos['Species'].values:
      print("Species Found. Add to the list")
      self.List_of_Species.append(specie)
    else:
       print("Specie not Found")

  
  def Read_Excel(self):
    Tk().withdraw()
    ruta_archivo = askopenfilename(title="Select an Excel file", filetypes=[("Excel files", "*.xlsx *.xls")])
    
    if ruta_archivo:
        try:
            df1 = pd.read_excel(ruta_archivo)

            if "Species" not in df1.columns:
                print("'Species' column not found in the Excel file.")
                return

            data_category = df1["Species"].dropna().reset_index(drop=True)

            found = False
            for specie in data_category:
                if specie in self.datos['Species'].values:
                    print(f"Species '{specie}' found. Adding to the list.")
                    self.List_of_Species.append(specie)
                    found = True
                else:
                    print(f"Species '{specie}' not found.")

            if not found:
                print("No valid species were found in the Excel file.")

        except Exception as e:
            print("Error reading the file:", str(e))
    else:
        print("A file was not selected.")


  def Report(self):
         filter=self.datos[self.datos['Species'].isin(self.List_of_Species)]
         result=filter[['Family','Class','Species']]

         df=pd.DataFrame(result)
         df.to_excel('./report.xlsx')
                 
            
def Menu():
    species=Species()
    while True:
        print("\n***** MENU *******\n")
        print("1. Search Specie")
        print("2. Read Excel")
        print("3. Create Report")
        print("4. Out")
        try:
            op = int(input("Choose a option: "))
            match op:
                case 1:
                    species.Search_Specie()
                case 2:
                    species.Read_Excel()
                case 3:
                    species.Report()
                case 4:
                    print("Exit of the program.....")
                    break  
        except ValueError:
            print("Please, introduce a valid number.\n")
    
Menu()