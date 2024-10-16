import tkinter as tk
from tkinter import *
from second_application import second_application
root = tk.Tk()
#setting the size of the form
root.geometry("500x450")

#starting form at the center 
root.eval('tk::PlaceWindow . center')

#setting the title of the form 
root.title("My First application")

#setting the backgroundcolor of the form 
root.config(bg="yellowgreen")

# title of the form inside 

lab = Label(root, text="Data Entry Form", font=('Airal', 12, 'bold'), bg='yellowgreen')
lab.grid(row=0, column=0, columnspan=2, pady=10)
#information status label 
infolab = Label(root, text="Part 1: Personal Identification", font=('Airal', 12, 'bold'), bg='yellowgreen')
infolab.grid(row=1, column=0, columnspan=2, pady=10)
#placing the entry forms 

Label(root, text = "First Name: ", bg="yellowgreen").grid(row = 2, column=0, pady=5)
Label(root, text = "Last Name: ", bg ="yellowgreen").grid(row = 3, column=0, pady=5)
Label(root, text = "Status: ", bg ="yellowgreen").grid(row = 4, column=0, pady=5)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

e1.grid(row=2, column=1, pady=5)
e2.grid(row=3, column=1, pady=5)
e3.grid(row=4, column=1, pady=5)

#part 2, gender type 
genderlab = Label(root, text="Part 2: Gender Identification", font=('Airal', 12, 'bold'), bg='yellowgreen')
genderlab.grid(row=5, column=0, columnspan=2, pady=10)


#creating radio box for gender 
v = IntVar()
gender_display = Label(root, text="Gender: ", bg='yellowgreen', font=('Airal', 12))
gender_display.grid(row=6, column=0, columnspan=2, pady=10)

def selection():
    select_gender = "Male" if v.get() == 1 else "Female"
    gender_display.config(text=f"{select_gender}")
    return select_gender


male = Radiobutton(root, text="Male", variable=v, value=1, bg='yellowgreen', command=selection).grid(row=7, column=1, pady=5)
female = Radiobutton(root, text="Female", variable=v, value=2, bg='yellowgreen', command=selection).grid(row=8, column=1, pady=5)

#submitting credentials

def submit():
    firstName = e1.get()
    lastName = e2.get()
    status = e3.get()
    gender = selection()
    obj = second_application(firstName,lastName, status, gender)
    obj.display_credentials()

submitbutton = Button(root, text="Submit Button", command=submit)
submitbutton.grid(row = 9, column=0, columnspan=2, pady=10)
root.mainloop()