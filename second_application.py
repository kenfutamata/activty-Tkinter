import tkinter as tk 
from tkinter import *

class second_application:


    def __init__(self, fname, lname, status, gender):
        self.fname = fname
        self.lname = lname
        self.status = status
        self.gender = gender
    
    def display_credentials(self):
        newWindow = Toplevel()
        newWindow.geometry("500x450")
        newWindow.config(background='yellowgreen')
        firstName =Label(newWindow, text=f"First Name:{self.fname}", font=('Airal', 12), bg='yellowgreen')
        lastName =Label(newWindow, text=f"Last Name:{self.lname}", font=('Airal', 12),bg='yellowgreen')
        statusType =Label(newWindow, text=f"Status:{self.status}", font=('Airal', 12),bg='yellowgreen')
        genderType =Label(newWindow, text=f"Gender: {self.gender}", font=('Airal', 12),bg='yellowgreen')
        firstName.pack()
        lastName.pack()
        statusType.pack()
        genderType.pack()

