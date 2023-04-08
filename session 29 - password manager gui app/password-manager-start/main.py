import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def p_generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.choice([8, 9, 10])
    nr_symbols = random.choice([2, 3, 4])
    nr_numbers = random.choice([2, 3, 4])

    # for char in range(nr_letters):
    #     password += random.choice(letters)
    p_letters = [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_numbers):
    #     password += random.choice(numbers)
    p_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_symbols):
    #     password += random.choice(symbols)
    p_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    f_pass = p_letters + p_numbers + p_symbols
    random.shuffle(f_pass)
    password = ''.join(f_pass)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    we = website_entry.get()
    ee = email_entry.get()
    pe = password_entry.get()


    if len(we) == 0 or len(ee) == 0 or len(pe) == 0:
        messagebox.showinfo(title='oops', message="please don't send me a blank input")
    else:
        is_ok = messagebox.askokcancel(title=we, message=f"these are the details entered:\n"
                                                         f"email: {ee}\n"
                                                         f"password: {pe}\nit's ok to save?")
        if is_ok:
            with open('data.txt', mode='a') as inp:
                inp.write(f'{we} | {ee} | {pe}\n')
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(0, 'rizky@gmail.com')
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('password manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website = Label(text='website:')
website.grid(column=0, row=1)
email = Label(text='email/username:')
email.grid(column=0, row=2)
password = Label(text='password:')
password.grid(column=0, row=3)

# entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'rizky@gmail.com')

password_entry = Entry()
password_entry.grid(column=1, row=3, columnspan=1)

# buttons
generate = Button(text='generate password', command=p_generator)
generate.grid(column=2, row=3, columnspan=1)
add_password = Button(text='add', width=36, command=save)
add_password.grid(column=1, row=4, columnspan=2)


window.mainloop()
