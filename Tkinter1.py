import Tkinter as tk

counter = 0
def counter_label(label):
  counter = 0
  # if counter < 15: continue
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()


root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()

how_many = 0
count = 0
while (count < 9):
   count = count + 1
   print 'The count is:', count

   if how_many == 2: break
   if count == 8:

       print 'The how_many is:', how_many
       how_many = how_many + 1
       count = 0
