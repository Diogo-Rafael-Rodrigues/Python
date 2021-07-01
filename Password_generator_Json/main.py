from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR -------------------------- #
def generator():
    entry_password.delete(0, END)

    password_random = [chr(random.randint(33, 123)) for n in range(10)]  # i'm using ascii table to sort the password
    password = "".join(password_random)  # remove spaces from list
    pyperclip.copy(password)  # copies the created password to the clipboard
    entry_password.insert(0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_site_txt = str(entry_web_site.get())
    password_txt = str(entry_password.get())
    email_txt = str(entry_email.get())

    new_data = {
        web_site_txt: {
            "Email": email_txt,
            "Password": password_txt,
        }
    }

    if len(web_site_txt) == 0 or len(password_txt) == 0 or len(email_txt) == 0:
        messagebox.showinfo(title="Error", message="All fields must be filed")
    else:
        try:
            with open("Data.json", "r") as data:
                # Reading old data
                data_file = json.load(data)
        except FileNotFoundError:
            with open("Data.json", "w") as data:
                # Saving updated data
                json.dump(new_data, data, indent=4)
        else:
            # Updating old data
            data_file.update(new_data)

            with open("Data.json", "w") as data:
                # Saving updated data
                json.dump(data_file, data, indent=4)
        finally:
            entry_password.delete(0, END)
            entry_web_site.delete(0, END)


# ----------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("Data.json", "r") as data:
            # Reading old data
            find_website = json.load(data)
            website = str(entry_web_site.get())
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in find_website.keys():
            email = find_website[website]["Email"]
            password = find_website[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No detaisl for {website} exists")


# ---------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# ------------- CANVAS -------------- #
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# ------------- LABELS -------------- #
web_site_label = Label(text="Web site: ")
web_site_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username: ")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# ------------- ENTRIES ------------- #


entry_web_site = Entry(width=20, font=('calibre', 14, 'normal'))
entry_web_site.focus()
entry_web_site.grid(column=1, row=1)

entry_email = Entry(width=30, font=('calibre', 14, 'normal'))
entry_email.insert(END, string="exemple@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=20, font=('calibre', 14, 'normal'))
entry_password.grid(column=1, row=3)

# ------------- BUTTONS ------------- #
button_gen_password = Button(text="Generate Password", command=generator, relief=GROOVE)
button_gen_password.grid(column=2, row=3)

button_add = Button(text="ADD", command=save, width=30, relief=GROOVE)
button_add.grid(column=1, row=4, columnspan=2)

button_search = Button(text="Search", command=find_password, relief=GROOVE, width=15)
button_search.grid(column=2, row=1)
window.mainloop()
