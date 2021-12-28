from numpy import int64
import pandas as pd
from tqdm import tqdm

inv=pd.read_excel('V:/code/seal-team/Ezra/EZProductionInvSearchResults752.xlsx')
user_input = input("Enter SKUs: ")

skus = user_input.split(",")


for x in skus:
    print(x)
    
print(inv.dtypes)