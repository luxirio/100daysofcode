from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "+" ]

def password_generator():
    nr_letters = random.randint(4,8)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)

    pwd_list = []

    for _ in range(nr_letters):
        pwd_list.append(random.choice(letters))
    for _ in range(nr_numbers):
        pwd_list.append(random.choice(numbers))
    for _ in range(nr_symbols):
        pwd_list.append(random.choice(symbols))

    random.shuffle(pwd_list)

    password = ""

    for char in pwd_list:
        password = password + char

    password_entry.insert(0, password) 
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    save_website = website_entry.get()
    save_email = email_entry.get()
    save_pwd = password_entry.get()

    if save_website == "" or save_email == "" or save_pwd == "":
        empty_entry = messagebox.showinfo(message="Please do not try to add empty entries")
        return empty_entry

    is_ok = messagebox.askokcancel(title="Check out your inputs", message=f"The following data was given: \nWebsite: {save_website}\nEmail: {save_email}\nPassword: {save_pwd}")

    if is_ok:
        with open("data.txt", "a") as data:
            data.write(f"{save_website} | {save_email} | {save_pwd}\n")

        # Clear the entries
        website_entry.delete(0, END)
        #email_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Window config
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

# --- IMAGE
# Image and canvas config
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_image)
canvas.grid(row=0, column=1)


# --- LABELS
LABEL_FONT = {"font":("Arial", 13)}
# Website text
website_label = Label(text="Website:", **LABEL_FONT)
website_label.grid(row=1, column=0, sticky=W)

# Email/Username Text
email_username_label = Label(text="Email/Username", **LABEL_FONT)
email_username_label.grid(row=2, column=0, sticky=W)
# Password
password_label = Label(text="Password:", **LABEL_FONT)
password_label.grid(row=3, column=0, sticky=W)


# --- ENTRIES
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_entry.insert(0, "email@usp.br")

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky=W)

# --- BUTTONS
generate_pwd = Button(text="Generate", font=("Arial", 11), command=password_generator)
generate_pwd.grid(row=3, column=2, sticky=E)

add_button = Button(width=42, text= "Add", command=save)
add_button.grid(row=4,column=1, columnspan=2, sticky=W)

window.mainloop()