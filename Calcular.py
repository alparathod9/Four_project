import tkinter as tk
from tkinter import messagebox
from tkinter.constants import SUNKEN
 
window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)
 
def click(number):
    entry.insert(tk.END, number)
 
def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showinfo("Error", "Syntax Error")
 
def clear():
    entry.delete(0, tk.END)
 
buttons = [
    ["C", "%", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["0", "1", "2", "3"],
    [".", "="]
]
 
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(master=frame, text=text, padx=15,
                           pady=5, width=3, command=lambda t=text: click(t))
        button.grid(row=i+1, column=j, padx=5, pady=5)
 
button_clear = tk.Button(master=frame, text="clear",
                         padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)
 
button_equal = tk.Button(master=frame, text="=", padx=15,
                         pady=5, width=9, command=calculate)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)
 
window.mainloop()