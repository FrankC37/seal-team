import pandas as pd
import tkinter as tk
from tkinter import Canvas, filedialog,Text
import sys
import os
#User input is taken for the path variable.
print("File path must be followed by file with extension") 
print("IE: " r"C:\Users\fconiglio\Converted ZCUS Template Rev1.xltm")


user_input = input("Enter the path of your file: ")

#user_profile = os.path.join(os.environ['USERPROFILE'], "My Documents")


assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)

#Used in a hardcoded only version
#sourcefile = r"C:\Users\fconiglio\git\seal-team\vinny\Ship Report V9 10.22.0.xlsx"

#reads in the user input file, skipping rows 2-7 (in excel), for all sheets

data = pd.read_excel(user_input,skiprows=[1,2,3,4,5,6],sheet_name = None)

#Each sheet in the data frame above will be printed to an indivual csv file, named as the sheet from the excel file
for sheet_name, data in data.items():
    data.to_csv(f'{sheet_name}.csv',index=False)