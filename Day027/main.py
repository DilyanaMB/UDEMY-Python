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
    my_label.config(text ='I\'ve got clicked')

# buttons
button = Button( text="Click me", command=button_clicked)
button.pack()

# entry

# equal to while True: listen...
window.mainloop()
