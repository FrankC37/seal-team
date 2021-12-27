# Pandas for Data Sorting, Tkinter for Reading in Reports, OS supports Tkinter in reading in the files
import pandas as pd
import tkinter as tk
from tkinter import Label, filedialog, Text
import os
from tkinter.constants import COMMAND
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

SKU = input("Enter Exact SKU Name: ")

#Data Frame to Sort Inventory Report By BOM (Highest First)

inv_bom_sort = inv_df.sort_values(by=['BOM'], ascending=False)
inv_bom_sort.to_excel(writer,sheet_name='Inv_DF',index=False)
writer.save()