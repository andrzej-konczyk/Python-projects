from tkinter import *
import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_text = website_entry.get()
    email_text = mail_user_entry.get()
    password_text = password_entry.get()

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Error", message=f"Field Website/Username or Password is empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[website_text] = {
            "email": email_text,
            "password": password_text,
        }

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


def search_password():
    website_text = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            websites = list(data.keys())
            if website_text in websites:
                messagebox.showinfo(title="Password exists", message=(
                    f"Password for {website_text} is:\n"
                    f"{data[website_text]['password']}\n"
                    f"and mail address is:\n"
                    f"{data[website_text]['email']}"
                )
                                    )
            else:
                messagebox.showerror(title="Error", message="Such website is not saved yet.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)

password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

website = tkinter.Label(text="Website:", font=("Times New Roman", 15))
website.grid(column=0, row=1)

mail_user = tkinter.Label(text="Email/Username:", font=("Times New Roman", 15))
mail_user.grid(column=0, row=2)

password = tkinter.Label(text="Password:", font=("Times New Roman", 15))
password.grid(column=0, row=3)

website_entry = tkinter.Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

mail_user_entry = tkinter.Entry(width=51)
mail_user_entry.grid(column=1, row=2, columnspan=2)
mail_user_entry.insert(0, "andrzej.konczyk@gmail.com")

password_entry = tkinter.Entry(width=32)
password_entry.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tkinter.Button(text='Search', width=14, command=search_password)
search_button.grid(column=2, row=1)

window.mainloop()
