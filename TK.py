__author__ = 'Agnieszka'
from Tkconstants import RAISED
import Tkinter
import time
import random


def helloCallBack():
    return rown
   # lista_rownan = random_digits()

   # time.sleep(0.1)
   # for row in lista_rownan :
   #      pass
       # var.set(row)

def random_digits():
    rownanie=[]
    for tries in range(15):
        global a
        a = random.randint(0, 300)
        b = random.randint(0, 300)
        rownanie.append( str(a) + ' + '+ str( b))
    return rownanie



def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()


counter = 0
def get_random(label):
    rown = random_digits()

    def count():
        global counter
        counter += 1
        label.config(text=str(rown[counter]))
        label.after(5000, count)

    count()

def getDate():
    print E1.get()


top = Tkinter.Tk()

label1 = Tkinter.Label( top, text="COOLATOR")
label1.pack()

E1 = Tkinter.Entry(top, bd =5)
E1.pack()
wynik = E1.get()

print wynik

submit = Tkinter.Button(top, text ="Submit", command = helloCallBack)
B = Tkinter.Button(top, text ="START", command = getDate)

B.pack()
submit.pack()

var = Tkinter.StringVar()
label = Tkinter.Label( top, fg= "dark green")
label2 = Tkinter.Label( top, fg= "dark green")
# label.after(1000, i)

label.pack()
counter_label(label)
label2.pack()
get_random(label2)

top.mainloop()