__author__ = 'Agnieszka'
fhand = open(moja_strona_CSS.css)
for line in fhand:
    if line.startswith('}'):
        print line
