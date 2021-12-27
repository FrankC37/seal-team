# Pandas for Data Sorting, Tkinter for Reading in Reports, OS supports Tkinter in reading in the files
import pandas as pd
import tkinter as tk
from tkinter import Label, filedialog, Text
import os
from tkinter.constants import COMMAND
from subprocess import STDOUT, Popen
import subprocess

# Declaring and requesting user input for a backlog report and inv report

backlog = filedialog.askopenfilename(initialdir='/', title = "Select Backlog Report", filetypes=(("All Files","*.*"),("Excel","*.xls")))
inv_report = filedialog.askopenfilename(initialdir='/', title = "Select Inventory Report", filetypes=(("All Files","*.*"),("Excel","*.xls")))

#printing out to check path
print(backlog)
print(inv_report)

