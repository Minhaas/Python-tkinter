from tkinter import *

window = Tk()

def km2miles():
    km = float(e1Var.get())
    miles = km*0.621
    print(f"The distance in miles is: {t1.insert(END, miles)}")


b1 = Button(master=None, text="Convert", highlightbackground="blue", command=km2miles)
b1.grid(row=0, column=0)

e1Var = StringVar()
e1 = Entry(window, textvariable=e1Var)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=300)
t1.grid(row=0, column=2)

window.mainloop()