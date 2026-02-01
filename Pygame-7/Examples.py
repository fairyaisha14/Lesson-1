from tkinter import *

window = Tk()
window.title("Sample Frame")
window.geometry("300x200")

# Frame1
f1 = Frame(master=window)
f1.pack()

# Assigning a widget in frame one
btn = Button(master=f1, text="click here", f="red")
btn.pack