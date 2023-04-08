from tkinter import *


def save():
    with open('coba_input.txt', mode='a') as inp:
        plus = website_entry.get()
        inp.writelines(f'{plus}\n')
        website_entry.delete(0, END)

window = Tk()
window.title('coba input')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='password-manager-start/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

add_password = Button(text='add', width=36, command=save)
add_password.grid(column=1, row=4, columnspan=2)




window.mainloop()