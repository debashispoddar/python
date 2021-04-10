from tkinter import *

window = Tk()


def km_to_miles():
    print ( e1_value.get())
    ti.insert(END, float(e1_value.get())*1.6)


bi=Button(window, text="Execute", command=km_to_miles)
bi.grid(row=0 , column=0)

e1_value=StringVar()
ei=Entry(window, textvariable=e1_value)
ei.grid(row=0, column=1)

ti=Text(window, height=1, width=20)
ti.grid(row=0, column=2)


window.mainloop()