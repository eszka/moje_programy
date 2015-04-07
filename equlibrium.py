__author__ = 'Agnieszka'

A = [-1,3,-4,5,1,-6,2,1]
def solution(A):
    wynik = -1
    #ret =[]
    # write your code in Python 2.7

    for i in range(len(A)):

        if sum(A[:i])== sum(A[i+1:]):
            wynik = i
            #ret.append(i)


    #print ret
    return wynik

print solution(A)

#equlibrium 100% score solution from blog

b = [-1,3,-4,5,1,-6,2,1]
def equi ( b ):
    N = len(b)
    total = sum(b)
    lefts = 0
    for p, value in enumerate(b):
        partial = total - value
        if partial % 2 == 0 and lefts == (partial / 2) and 0 <= p < N:
            return p
        lefts += value
    return -1

print equi(b)