#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:26:52 2021

@author: joshualeeman
"""


"""
R-AGI Interface Window

In this script, blah blah blah

Author: Joshua Leeman
Designer: Mohammed Elbadry
"""


# This is the stuff we imported
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import ttk 
from tkinter import filedialog


# This class C1 actually creates the the leftmost frame, which itself contains
# a grid on its own.
class C1(Frame):
    def __init__(self, p):
        super().__init__(p)

        self.initUI()

    # Allowing these columns/rows
    def initUI(self):
        self.columnconfigure(0, weight=1)
        for y in range(30):
            self.rowconfigure(y, weight=1)

        
        
        def openfile():
            filepath = filedialog.askopenfilename()
            chest = Image.open(filepath).resize((300, 300), Image.ANTIALIAS)
            chestjov = ImageTk.PhotoImage(chest) 
            label1 = Label(self, image=chestjov)
            label1.image = chestjov
            label1.grid(row=1, column=0, padx=30, pady=7)
        
        # The Browse button.
        abtn = Button(self, text="Browse",command=openfile)
        abtn.grid(row=2, column=0, pady=10)
        
        # The Process button, which begins the program.
        abtn = Button(self, text="Process",)    
        abtn.grid(row=3, column=0, pady=15)
        
'''       
class C2(Frame):
    def __init__(self, p):
        super().__init__(p)

        self.initUI()

    def initUI(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        
        
        
        # The three labels that show the progress of the program 
        lbl21 = Label(self, text="Overall Health Check", font=('Helvetica', 18))
        lbl21.grid(row=1, column=0, pady=18, padx=5)
        
        lbl22 = Label(self, text="Anomaly Check", font=('Helvetica', 18))
        lbl22.grid(row=2, column=0, pady=18, padx=5)
        
        lbl23 = Label(self, text="Deep Analysis (In Progress)", font=('Helvetica', 18))
        lbl23.grid(row=3, column=0, pady=18, padx=5)
'''
    
        
class C3(Frame):
    def __init__(self, p):
        super().__init__(p)

        self.initUI()

    def initUI(self):
        self.columnconfigure(0, weight=1)
        for y in range(30):
            self.rowconfigure(y, weight=1)
        
        
        
        # The text box showing the results
        #area = Text(self, height=8, width=32, font=("Helvetica", 18))
        area = Text(self, width=60, font=("Helvetica", 18))
        area.grid(row=4, column=0, padx=16, pady=10)



        
        
# This block of code combines the three frames under the master window
class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("R-AGI Interface")
        self.pack(fill=BOTH, expand=True)
        for x in range(30):
            self.columnconfigure(x, weight=1)
        #self.columnconfigure(1, weight=1)
        #self.columnconfigure(2, weight=1)
        #self.columnconfigure(3, weight=1)
        for y in range(30):
            self.rowconfigure(y, weight=1)
        #self.rowconfigure(1, weight=1)
        #self.rowconfigure(2, weight=1)
        #self.rowconfigure(3, weight=1)


        c1 = C1(self)
        c1.config(borderwidth=1,relief=RIDGE)
        c1.grid(row=0, column=0, rowspan=2, sticky=N+S+E+W, pady=18, padx=5)
        #c2 = C2(self)
        #c2.grid(row=0, column=1, pady=18, padx=5)
        c3 = C3(self)
        c3.config(borderwidth=1,relief=RIDGE)
        c3.grid(row=0, column=1, sticky=N+S+E+W, pady=18, padx=5)
        


def main():
    root = Tk()
    root.geometry("1000x600")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()