import pandas as pd
import tkinter as tk
from tkinter import Canvas, Frame, filedialog,Text
import os
import sys


root = tk.Tk()
root.title("ZCUS CSV Formatter")

files = []

def addFile():
    for widget in frame.winfo_children():
        widget.destroy()
        
    filename = filedialog.askopenfilename(initialdir="/", title= "Select File",
    filetypes=(("Excel Files (XLTM)","*.xltm"),("All Files","*")))
    files.append(filename)
    print(filename)

    for file in files:
        label = tk.Label(frame, text=file,bg="white")
        label.pack()

def csvConvert():
    x= 0
    while x < len(files):
        for file in files:
            os.chdir("C:/temp")
            data = pd.read_excel(file,skiprows=[1,2,3,4,5,6],sheet_name = None)
            for sheet_name, data in data.items():
                data.to_csv(f'{sheet_name}.csv',index=False)
        x+=1 


def quitting():
    quit()

#    data = pd.read_excel(files,skiprows=[1,2,3,4,5,6],sheet_name = None)
#    for sheet_name, data in data.items():
#        data.to_csv(f'{sheet_name}.csv',index=False)

canvas = tk.Canvas(root,height=250,width=600,bg="#143a2a")
canvas.pack()

frame = tk.Frame(root,bg= "grey")
frame.place(relwidth=0.8,relheight=0.6,relx=0.1,rely=0.1)

open_file = tk.Button(root, text="Load Excel Files",padx=10,pady=5,fg="white",bg="black",command=addFile)
open_file.pack()

convert = tk.Button(root, text="Convert to CSV",padx=10,pady=5,fg="white",bg="black", command= csvConvert)
convert.pack()

quitter = tk.Button(root, text="Quit",padx=10,pady=5,fg="white",bg="red", command= quitting)
quitter.pack()


root.mainloop()
