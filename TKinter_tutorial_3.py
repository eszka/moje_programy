__author__ = 'Agnieszka'
from Tkinter import *

root = Tk()
one = Label(root, text = 'One', bg = 'red', fg ='white')
one.pack()
two = Label(root, text = 'Two', bg = 'blue', fg ='white')
two.pack(fill=X)
three = Label(root, text = 'Three', bg = 'green', fg ='white')
three.pack(side=LEFT, fill=Y)
root.mainloop()
