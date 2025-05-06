from tkinter import *


def calculate():
    miles = float(miles_entry.get())
    km_result = miles * 1.689
    km_output.config(text=km_result)

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", width=5)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", width=13)
equal_label.grid(column=0, row=1)

km_output = Label(text="0", width=13)  # text changes to km_result
km_output.grid(column=1, row=1)

km_label = Label(text="Km", width=5)
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", width=10, command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
