__author__ = 'Agnieszka'
l = [4, 2, 6, 1, 8, 12, 3, 10, 100, 50]


def sortowanie(l):
    pass


for j in range(len(l) -1, 0,  -1):

    for i in range(j):
        if l[i] > l[i+1]:
            temp = l[i]
            l[i] = l[i + 1]
            l[i + 1] = temp

print l

sortowanie(l)
print sortowanie(l)

for i in range(len(l) -1, 0,  -1):
    print i

