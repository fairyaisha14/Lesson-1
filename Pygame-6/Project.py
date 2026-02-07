import tkinter as tk

def calculate_product():
    result_textbox.delete(1.0, tk.END)
    result_textbox.insert(tk.END, int(entry1.get()) * int(entry2.get()))

root = tk.Tk()
root.geometry("400x300")
tk.Label(root, text="Multiply two numbers").pack()
entry1 = tk.Entry(root); entry1.pack()
entry2 = tk.Entry(root); entry2.pack()
tk.Button(root, text="Calculate", command=calculate_product).pack()
result_textbox = tk.Text(root, height=2, width=20); result_textbox.pack()
root.mainloop()


