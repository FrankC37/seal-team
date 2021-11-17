import pandas as pd
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

#this needs to clear out rows 2-6 in the sheet before convering to csv

data = pd.read_excel(user_input,skiprows=[2,3,4,5,6],sheet_name = None)

for sheet_name, data in data.items():
    data.to_csv(f'{sheet_name}.csv')