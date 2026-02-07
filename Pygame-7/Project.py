from tkinter import *
from datetime import datetime

def calculate_age():
    name = name_entry.get()
    birth_date = birth_date_entry.get()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    age = datetime.now().year - birth_date.year - ((datetime.now().month, datetime.now().day) < (birth_date.month, birth_date.day))
    result_label.config(text=f"Hello {name}, you are {age} years old!")

root = Tk()
root.geometry("400x400")
root.title("Age Calculator App")

Label(root, text="Name:").grid(row=0, column=0)
Label(root, text="Birth Date (YYYY-MM-DD):").grid(row=1, column=0)

name_entry = Entry(root); name_entry.grid(row=0, column=1)
birth_date_entry = Entry(root); birth_date_entry.grid(row=1, column=1)

Button(root, text="Calculate Age", command=calculate_age).grid(row=2, columnspan=2)
result_label = Label(root); result_label.grid(row=3, columnspan=2)

root.mainloop()
