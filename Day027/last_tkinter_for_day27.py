from tkinter import *


def button_clicked():
    print('I\'ve got clicked')
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)
# add padding to all widgets
window.config(padx=20, pady=20)

# label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text='New text')
# my_label.place(x=0, y=0)
my_label.config(padx=70, pady=70)
my_label.grid(column=0, row=0)

# button
button = Button(text="Click me", command=button_clicked)
button.grid(column=2, row=0)

# second button
new_button = Button(text="Click me", command=button_clicked)
new_button.grid(column=1, row=1)

# entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

# NOTE! CAN'T mix grid and pack

# equal to while True: listen...
window.mainloop()
