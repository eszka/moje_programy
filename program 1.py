__author__ = 'Agnieszka'
# -*- coding: utf-8 -*-
fhand = open("C:\Users\Agnieszka\Desktop\strona.txt", 'r')
e = fhand.read()
list = e.split ('}')
for item in list:
    print item + "}"


