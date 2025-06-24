import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Simple To-Do List")
window.geometry("300x400")
tasks = []
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_index = selected[0]
        removed_task = tasks.pop(task_index)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")
title_label = tk.Label(window, text="My To-Do List", font=("Arial", 16))
title_label.pack(pady=10)

task_entry = tk.Entry(window, width=25)
task_entry.pack(pady=5)
add_button = tk.Button(window, text="AddTask", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(window, width=30, height=10)
task_listbox.pack(pady=10)
window.mainloop()



