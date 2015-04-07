__author__ = 'Agnieszka'

from Tkinter import *
root = Tk()

theLabel = Label(root,text = 'Culaator')
theLabel.pack()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()

root.mainloop()