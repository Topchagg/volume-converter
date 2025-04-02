from VolumeConverter import VolumeConverter
from tkinter import *
from tkinter import ttk

def changeUnits(*args):
    units1["values"] = units[form.get()]
    units2["values"] = units[form.get()]

def convert():
    number = float(entry.get())
    number *= VolumeConverter.convert(form.current(), units1.get(), units2.get())
    result["text"] = number

units = {
    "Balk": ['mm3', 'cm3', 'dm3', 'm3', 'bushel', 'peck', 'quart'],
    "Liquid": ['nl', 'mkl', 'ml', 'l', 'dal', 'hl', 'm3', 'gal', 'barrel']
}
root = Tk()
root.geometry("300x300")
root.title("Converter")
form = ttk.Combobox(values=list(units.keys()), width=40)
form.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entry = Entry(width=30)
entry.grid(row=1, column=0, padx=5, pady=5)
units1 = ttk.Combobox(width=10)
units1.grid(row=1, column=1, padx=5, pady=5)
units2 = ttk.Combobox(width=10)
units2.grid(row=2, column=1, padx=5, pady=5)
result = Label(text="...............")
result.grid(row=2, column=0, padx=5, pady=5)
button = Button(text="Convert", width=30, command=convert)
button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
form.bind("<<ComboboxSelected>>", changeUnits)
root.mainloop()