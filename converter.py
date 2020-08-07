from tkinter import *

#1 kg = 1000 grams  
#1 kg = 2.20462 pounds  
#1 kg = 35.274 ounces

window = Tk()

def con():
    kg = float(newVar.get())
    grams = kg*1000
    pounds = kg*2.20462
    ounces = kg*35.274
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)

l1=Label(window, text="Kilogram")
l1.grid(row=0,column=0)

b1=Button(window, text="Convert", command=con, highlightbackground="black")
b1.grid(row=0, column=1)    

newVar = StringVar()
e1=Entry(window, textvariable=newVar)
e1.grid(row=0, column=2)

t1=Text(window, width=20, height=1 )
t1.grid(row=1, column=1)

t2=Text(window, width=20, height=1 )
t2.grid(row=1, column=2)

t3=Text(window, width=20, height=1 )
t3.grid(row=1, column=3)

window.mainloop()