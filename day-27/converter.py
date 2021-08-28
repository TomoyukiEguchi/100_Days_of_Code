from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)


input = Entry(width=10)
input.grid(column=1, row=0)


output = Label(text="0")
output.grid(column=1, row=1)


def button_clicked():
    result = float(input.get()) * 1.609
    output.config(text=f"{result}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)



window.mainloop()
