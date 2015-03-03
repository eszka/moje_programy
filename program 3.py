 #!/usr/bin/python
 # -*- coding: utf-8 -*-

__author__ = 'Agnieszka'
# jakos otworzyć dane z pliku
fhand = open("C:\Users\Agnieszka\Desktop\pretius.txt")

amount = []

for line in fhand:
    if line != '\n':
        e = line.split('amount:')
        amount.append(e[1])
print amount

ss = ''.join(amount)
print ss

rr = ss.split('PLN\n')

rr_dots = []
for r in rr:
    r = r.replace(',', '.')
    rr_dots.append(r)

rr_dots = map(float,rr_dots)

result = sum(rr_dots)
print result

# PRZECINKI!!!
# for r in rr:
#         for char in r:
#             if char == ',':
#                 char = '.'
# print rr
# zmiana sring we float w liście
#1st try
#  for r in rr:
#      r = float(r)
# 2nd try
# rr = map(float,rr)
# print rr
# for item in amount:
#     for i in item:
#         if item in range(10) or item == ",":
#             print i




