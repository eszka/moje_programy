__author__ = 'Agnieszka'
name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
words = list()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From'): continue
    w = line.split()
    if len(w) == 7 :continue
    #print w
    words.append(w[1])
    #print words

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] =  counts[word] + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount