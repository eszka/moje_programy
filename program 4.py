 #!/usr/bin/python
 # -*- coding: utf-8 -*-

__author__ = 'Agnieszka'
# jakos otworzyć dane z pliku
fhand = open("C:\Users\Agnieszka\Desktop\pretius.txt")

for line in fhand:
    if line != '\n':
        ee = line.split('@')
        print ee
new_list =[]
new_list.appened(ee[:-1])
print new_list
print ee

