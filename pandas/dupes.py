import pandas as pd

df =  pd.read_csv(r'C:/Users/fconiglio/git/seal-team/pandas/FItemBinCheckResults598.csv')

grouped = pd.concat(g for _, g in df.groupby('Name') if len(g) > 1)


grouped.to_csv('Grouped.csv', index= False)