__author__ = 'Agnieszka'

from Tkinter import *
import random
for tries in range(15):
    a = random.randint(0, 300)
    b = random.randint(0, 300)
    print a, '+', b
    result = raw_input("The sum is:")
    c = a + b
    if float(result) == c:
        print "Your answer is correct :)"
    else:
        print "WRONG ANSWER"

# import Tkinter
# top = Tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()