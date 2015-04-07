__author__ = 'Agnieszka'

# C:\Users\Agnieszka\Desktop\ITC\Python Cursera\romeo.txt


fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    li = line.rstrip().split()
    # li = a.split()
    for item in li:
        if item in lst: continue
        else:
            lst.append(item)
print lst

print line
lst.sort()
print lst



# fname = raw_input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
# 	line = line.rstrip()
#   words = line.split()
#         for word in words:
#             if word in words: continue
#             else:
#                 lst.append(word)
#
# result = lst.sort()
# print result

# #initial code
# #first for loop
# #strip and split
# Second for loop: #iterate for all the words in the lists
#     if word is already in list:
#             #do nothing and move to the start of the loop (hint: we've done this in prev lecs)
#         else:
#             #append to the list if it is not already present there
# #sort the list
# #print the list
# Actually you shouldn't share code to graded assignments.
#


# You have two mistakes in your code:
#
# 1. You should create a new list to store result of  line.split()
# 2. append content of new list to word list(in your code newlist)
