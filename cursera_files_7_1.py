__author__ = 'Agnieszka'

# Use words.txt as the file name
# File name C:\Users\Agnieszka\Desktop\ITC\Python Cursera\words.txt
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    li = line.rstrip()
    lin = li.upper()
    print lin
