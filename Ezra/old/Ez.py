# Pandas for Data Sorting, Tkinter for Reading in Reports, OS supports Tkinter in reading in the files
import pandas as pd
import tkinter as tk
from tkinter import Label, filedialog, Text
import os
from tkinter.constants import COMMAND, Y
from subprocess import STDOUT, Popen
import subprocess

#declaring writer variable to output multiple sheets into on document

writer = pd.ExcelWriter(r'V:\code\seal-team\Ezra\output.xlsx', engine='xlsxwriter')

# Declaring and requesting user input for a backlog report and inv report
backlog = filedialog.askopenfilename(initialdir='/', title = "Select Backlog Report", filetypes=(("All Files","*.*"),("Excel","*.xls")))
inv_report = filedialog.askopenfilename(initialdir='/', title = "Select Inventory Report", filetypes=(("All Files","*.*"),("Excel","*.xls")))


#declaring data frames for both reports
backlog_df = pd.read_excel(backlog,index_col=False)
inv_df = pd.read_excel(inv_report,index_col=False)

#User input, this is going to be used for filtering DF below
SKU = input("Enter Exact SKU Name: ")

#Do sorting and filter work here
#Data Frame to Sort Inventory Report By BOM (Highest First)

inv_bom_sort = inv_df[inv_df['RM Master Parent'] == SKU]
inv_bom_sort = inv_bom_sort.sort_values(by=['BOM'], ascending=False)


#output to files

#writes to hard coded writer file above, outputs only the specified columns as specificed below
inv_bom_sort.to_excel(writer,sheet_name='Inv_DF',index=False,columns=['Item','RM Length','RM Width','RM Thickness', 'On Hand', 'BOM',])

#looping throught the above DF to make all of the columns at adjust width to not clip text
for column in inv_bom_sort:
    column_width = max(inv_bom_sort[column].astype(str).map(len).max(), len(column))
    col_idx = inv_bom_sort.columns.get_loc(column)
    writer.sheets['Inv_DF'].set_column(col_idx, col_idx, column_width)
writer.save()


