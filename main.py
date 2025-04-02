from VolumeConverter import VolumeConverter
from tkinter import *
from tkinter import ttk

def changeUnits(*args):
    units1["values"] = units[converters.get()]
    units2["values"] = units[converters.get()]

def convert():
    con = VolumeConverter()
    number = float(entry.get())
    unit1 = units1.get()
    unit2 = units2.get()
    number *= con.convert(unit1, unit2)
    result["text"] = number

units = {
    "Dry": [],
    "Liquid": []
}
root = Tk()
root.geometry("300x300")
root.title("Converter")
converters = ttk.Combobox(values=list(units.keys()), width=40)
converters.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
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
converters.bind("<<ComboboxSelected>>", changeUnits)
root.mainloop()