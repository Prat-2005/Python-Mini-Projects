from tkinter import *
from tkinter import messagebox
import random
import string

def create_app():
    app = Tk()
    app.iconbitmap("padlock.ico")
    app.config(bg="midnight blue")
    app.title("Random Password Generator")
    app.maxsize(width=400, height=260)
    app.minsize(width=400, height=260)
    return app

def generate_password(text, length):
    characters = string.ascii_letters + string.digits + string.punctuation
    remaining_length = length - len(text)
    if remaining_length < 0:
        raise ValueError("Length must be greater than the length of the text")
    random_part = ''.join(random.choice(characters) for _ in range(remaining_length))
    password = list(random_part)
    insert_index = random.randint(0, remaining_length)
    for i, char in enumerate(text):
        password.insert(insert_index + i, char)
    return ''.join(password)

def display_password():
    try:
        text = str(ent1.get())
        length = int(ent2.get())
        if len(text) < 4:
            raise ValueError("Text must contains atleast 4 characters")
        if length < 1:
            raise ValueError("Length must be positive")
        password = generate_password(text, length)
        res.config(text=password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def create_interface(app):
    Label(app, text=" Enter Text:", fg="light green", bg="midnight blue", bd=3, font=("Arial", 10)).place(x=160, y=5)
    Label(app, text=" Enter Password Length:", fg="light green", bg="midnight blue", bd=3, font=("Arial", 10)).place(x=130, y=80)

    global ent1, ent2
    ent1 = Entry(app, width=30, bd=3, font=("Arial", 10))
    ent1.place(x=90, y=35)

    ent2 = Entry(app, width=30, bd=3, font=("Arial", 10))
    ent2.place(x=90, y=110)

    btn = Button(app, text="Generate Password", fg="black", bg="light blue", bd=3, font=("Arial", 10), command=display_password)
    btn.place(x=140, y=200)

    global res
    res = Label(app, text="", fg="light green", bg="midnight blue", font=("Arial", 10))
    res.place(x=90, y=150)

if __name__ == "__main__":
    app = create_app()
    create_interface(app)
    app.mainloop()

