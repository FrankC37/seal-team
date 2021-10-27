import pandas as pd
sourcefile = r"C:\Users\fconiglio\git\seal-team\vinny\Ship Report V9 10.22.0.xlsx"

data = pd.read_excel(sourcefile, sheet_name = None)

for sheet_name, data in data.items():
    data.to_csv(f'{sheet_name}.csv')