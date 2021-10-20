import pandas as pd
#Variables for working files
sourcefile = r"C:\Users\fconiglio\git\seal-team\import\EZRemParentMapping.xlsx"
destfile = r"C:\Users\fconiglio\git\seal-team\import\DestFile.xlsx"

data = pd.read_excel(sourcefile, sheet_name="EZ_Rem Parent Mapping", index_col=0)

cleardata = pd.read_excel(destfile, sheet_name="EZ_Rem Parent Mapping")

cleardata.drop(2,*)

#cleardata.to_excel(destfile, sheet_name="EZ_Rem Parent Mapping")

#data.to_excel(destfile, sheet_name='EZ_Rem Parent Mapping')

