# Import necessary libraries
from tkinter import *

# Create window
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a frame to organise elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# Add widgets
# Add Label
lbl1 = Label(frame, text = "Full Name", bg="#38895D3", fg = 'white', width=12)
lbl2 = Label(frame, text = "Email Id", bg="#38895D3", fg = 'white', width=12)
lbl3 = Label(frame, text = "Enter Password", bg="#38895D3", fg = 'white', width=12)

# Use Entry Widget to create a text box for user to enter details
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

# Function to display messages
def display():
    name = name_entry.get()
    greet = "Hey "+name
    message = "\nCongratulations for your new account!"
    textbox.inserty(END, greet)
    textbox.insert(END, message)

# Textbox to display message
textbox = Text(bg="#BEBEBE", fg="black")

# Add Button, when pressed, messag will be displayed
btn = Button(text = "Create Account", command=display, bg="red")

# Arrange all widgets
frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)