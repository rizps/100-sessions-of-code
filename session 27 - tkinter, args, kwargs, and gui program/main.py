import tkinter as tk

window = tk.Tk()
window.title('my first gui program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = tk.Label(text="i'm a label", font=("Arial", 24))
# my_label.pack()

# place
# my_label.place(x= 0, y= 0)
my_label.grid(column=0, row=0)  # placing with grid

# change some property of the component
my_label['text'] = 'new text 1'
# or
my_label.config(text='new text 2')
my_label.config(padx=50, pady=50)

# button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tk.Button(text='click me', command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = tk.Button(text='click me2', command=button_clicked)
# button.pack()
button2.grid(column=2, row=0)

# entry
input = tk.Entry(width=10)
# input.pack()
input.get()
input.grid(column=3, row=2)

window.mainloop()


