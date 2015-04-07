__author__ = 'Agnieszka'
from Tkinter import *

root = Tk()


label1 = Label( root, text="Month(MM)")
E1 = Entry(root, bd =5)

def getDate():
    print E1.get()

submit = Button(root, text ="Submit", command = getDate)

label1.pack()
E1.pack()

submit.pack(side =BOTTOM)
root.mainloop()