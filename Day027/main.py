import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(500, 300)

# label
my_label = tkinter.Label( text="I am a Label", font=("Arial", 24, "bold"))
# show the label
my_label.pack()



# equal to while True: listen...
window.mainloop()
