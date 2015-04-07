__author__ = 'Agnieszka'
def median(li):
    lis = sorted(li)
    if len(lis)%2 != 0:
        return lis[(len(lis)/2)]
    else:
        h = int(len(lis)/2)
        print h
        print lis[h - 1]
        print lis[h]
        return (lis[h] + lis[h - 1])/2.0

print median([1,2,3,4,5,6])
