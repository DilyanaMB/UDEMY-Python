from tkinter import *

window = Tk()

window.title("My first GUI program")
window.minsize(500, 300)

# label
my_label = Label( text="I am a Label", font=("Arial", 24, "bold"))
# show the label
my_label.pack()

# both will change label's text
my_label['text'] = 'New text'

def button_clicked():
    input_text= save_input()
    my_label.config(text =input_text)

# button
button = Button( text="Click me", command=button_clicked)
button.pack()

# entry
input = Entry(width = 10)
input.pack()

# return the input in the field as String
def save_input():
    return input.get()

# equal to while True: listen...
window.mainloop()
