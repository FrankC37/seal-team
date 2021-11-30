import pandas as pd
import os
import sys
from tkinter import filedialog,Text
from datetime import datetime

from pandas.core.indexes.base import Index
from pandas.core.indexing import IndexSlice

writer = pd.ExcelWriter(r'C:\Users\fconiglio\Dropbox (USA Sealing)\USA Sealing Team Folder\USA Sealing Inc\Frank\Reallocate.xlsx', engine='xlsxwriter')


excel_file_path = filedialog.askopenfilename(initialdir="/", title= "Select File",
    filetypes=(("Excel Files (XLSX)","*.xlsx"),("All Files","*")))

df = pd.read_excel(excel_file_path)
#Time Conversions
df["Ship By Date"] = pd.to_datetime(df["Ship By Date"])
df["Ship By Date"] = df["Ship By Date"].dt.strftime('%m/%d/%Y')


skus = df['Product SKU']


for sku in skus:
    df1 = df[(df['Product SKU'] == sku)]
    df1.to_excel(writer,sheet_name= sku,index=False)

writer.close()
    



