import pandas as pd
#Variables for working files
sourcefile = r"C:\Users\fconiglio\git\seal-team\import\GraingerBacklogByProduct1021.xlsx"
destfile = r"C:\Users\fconiglio\git\seal-team\import\DestFile.xlsx"


data = pd.read_excel(sourcefile, sheet_name="Grainger Backlog by product", index_col=0)

data['Order date']=pd.to_datetime(data['Order date'])
data.sort_values(by=['Order date'], ascending=False)
data.to_excel(destfile,sheet_name='Dest')






# no longer looking to use this since it will wipe out the Ship Report
#data.to_excel(shiprep, sheet_name='EZ_Rem Parent Mapping(1)')

#
#df.sort_values(by=['Order date'], inplace=True, ascending=False)