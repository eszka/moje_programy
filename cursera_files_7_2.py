__author__ = 'Agnieszka'


# Use the file path C:\Users\Agnieszka\Desktop\ITC\Python Cursera\mbox-short.txt
fname = raw_input("Enter file name: ")
fh = open(fname)
c = 0
result =0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
       continue
    if line.startswith("X-DSPAM-Confidence:"):
       c = c + 1
       a = line.find(':')
       b = float(line[a+1:])
       result = result + b
    #print line
    #print b
print "Average spam confidence:", result/c


#text = "X-DSPAM-Confidence:    0.8475"
#a = text.find(':')

#b = text[19:]

#print float(b)
