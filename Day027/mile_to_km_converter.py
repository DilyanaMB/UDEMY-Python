from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)

input = Entry(width=7)
input.grid(row=0, column=1)
input.focus_set()

label_miles = Label(text="Miles", font=("Arial", 24))
label_miles.grid(row=0, column=2)

label_is_equal_to = Label(text="is equal to", font=("Arial", 24))
label_is_equal_to.grid(row=1, column=0)


def convert_miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    label_km_number.config(text=km)


label_km_number = Label(text='0', font=("Arial", 24))
label_km_number.grid(row=1, column=1)
label_km_number.config(padx=10)

label_km = Label(text="Km", font=("Arial", 24))
label_km.grid(row=1, column=2)

button = Button(text="Calculate", command=convert_miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
