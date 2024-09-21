from tkinter import *
from tkinter import messagebox, simpledialog

def add_task():
    task = ent.get()
    if task:
        List.insert(END, task)
        ent.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_task():
    try:
        selected_index = List.curselection()[0]
        selected_task = List.get(selected_index)
        new_task = simpledialog.askstring("Update Task", "Edit task:", initialvalue = selected_task)
        if new_task:
            List.delete(selected_index)
            List.insert(selected_index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

def delete_task():
    try:
        selected_task = List.curselection()[0]
        List.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

def delete_all_task():
    if messagebox.askyesno("Warning", "Are you sure you want to delete all tasks?"):
        List.delete(0, END)
        
myapp = Tk()
myapp.title("Daily Checklist")
myapp.config(bg = "green")
myapp.minsize(width = 550, height = 360)
myapp.maxsize(width = 550, height = 360)

lbl = Label(myapp, text = "Enter your task one-by-one:", bg = "green", fg = "white")
lbl.place(x = 10, y = 5)
ent = Entry(myapp, width = 87, bd = 5)
ent.place(x = 10, y = 30)

btn1 = Button(myapp, text = "Add Task", bg = "red", fg = "white", bd = 5, command = add_task)
btn1.place(x = 240, y = 70)

btn2 = Button(myapp, text = "Update Task", bg = "red", fg = "white", bd = 5, command = update_task)
btn2.place(x = 10, y = 310)

lbl1 = Label(myapp, text = "Today's Task:", bg = "green", fg = "white")
lbl1.place(x = 10, y = 100)
List = Listbox(myapp, width=87, height=10, bd = 5)
List.place(x = 10, y = 130)

btn3 = Button(myapp, text = "Delete Task", bg = "red", fg = "white", bd = 5, command = delete_task)
btn3.place(x = 460, y = 310)

btn4 = Button(myapp, text = "Delete All Task", bg = "red", fg = "white", bd = 5, command = delete_all_task)
btn4.place(x = 235, y = 310)

myapp.mainloop()
