import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title('TO DO LIST')
app.geometry('350x450')
app.config(bg='#09112e')

font1 = ('arial', 32, 'bold')
font2 = ('arial', 18, 'bold')
font3 = ('arial', 10, 'bold')

def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(0, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showerror('Error', 'Enter a task.')

def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Error', 'Choose a task to delete.')

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = tasks_list.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                tasks_list.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

title_label = tk.Label(app, font=font1, text='TO DO list', fg='#fff', bg='#09112e')
title_label.place(x=100, y=20)

add_button = tk.Button(app, command=add_task, font=font2, text='Add Task', fg='black', bg='greenyellow', cursor='hand2', width=12)
add_button.place(x=40, y=80)

remove_button = tk.Button(app, command=remove_task, font=font2, text='Remove Task', fg='#fff', bg='#96061c', cursor='hand2')
remove_button.place(x=180, y=80)

task_entry = tk.Entry(app, font=font2, fg='#000', width=28)
task_entry.place(x=40, y=120)

tasks_list = tk.Listbox(app, width=39, height=15, font=font3)
tasks_list.place(x=80, y=200)

load_tasks()

app.mainloop()