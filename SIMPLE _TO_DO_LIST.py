import tkinter as tk
from tkinter import messagebox

# Function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark task as completed
def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, f"{task} - Completed")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# GUI setup
root = tk.Tk()
root.title("Simple To-Do List App")
root.geometry("400x400")

# Create the listbox
listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 14))
listbox.pack(pady=20)

# Create the input field
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

# Create buttons
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 14))
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Arial", 14))
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark as Completed", command=mark_completed, font=("Arial", 14))
complete_button.pack(pady=5)

root.mainloop()
