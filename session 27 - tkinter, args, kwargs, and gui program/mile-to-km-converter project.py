import tkinter as tk

window = tk.Tk()
window.title('mile to km converter')
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


# label
is_equal = tk.Label(text=" is equal to ", font=("Arial", 24))
# place
is_equal.grid(column=0, row=2)

miles = tk.Label(text=" miles ", font=("Arial", 24))
miles.grid(column=2, row=1)

km = tk.Label(text=" km ", font=("Arial", 24))
km.grid(column=2, row=2)

converted = tk.Label(text=' 0 ', font=("Arial", 24))
converted.grid(column=1, row=2)


# button
def miles_to_km():
    new_text = entry.get()
    convert = int(new_text) * 1.609344
    converted.config(text=convert)

button = tk.Button(text=' calculate ', command=miles_to_km, font=("Arial", 24))
button.grid(column=1, row=3)

# entry
entry = tk.Entry(width=10, font=("Arial", 24))
entry.get()
entry.grid(column=1, row=1)

window.mainloop()


